from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .apps import DetectorConfig
from django.views.decorators.csrf import csrf_exempt

from base64 import b64decode
import numpy as np
from base64 import b64decode
from PIL import Image
import io
import time



# Create your views here.

@csrf_exempt
def object_detection_api(api_request):
    json_object = {'success': False}

    if api_request.method == "POST":

        if api_request.POST.get("image64", None) is not None:
            base64_data = api_request.POST.get("image64", None).split(',', 1)[1]
            data = b64decode(base64_data)
            data = np.array(Image.open(io.BytesIO(data)))
            result, detection_time = detection(data)

        elif api_request.FILES.get("image", None) is not None:
            image_api_request = api_request.FILES["image"]
            image_bytes = image_api_request.read()
            image = Image.open(io.BytesIO(image_bytes))
            result, detection_time = detection(image, web=False)

    if result:
        json_object['success'] = True
    json_object['time'] = str(round(detection_time))+" seconds"
    json_object['objects'] = result
    print(json_object)
    return JsonResponse(json_object)

def detect_request(api_request):
    return render(api_request, 'index.html')

def detection(original_image, web=True):
    #print(DetectorConfig.yolo8_model,type(original_image))
    start = time.time()
    result = DetectorConfig.yolo8_model.predict(source=original_image, conf=0.33,)[0]
    end = time.time()
    im = Image.fromarray(result.plot())
    im.save("detector\static\\test.jpeg")
    if len(result.boxes) == 0:
        return None,round(end-start)
    #print(results[0].boxes.cls)
    print(result.boxes[0].data,)

    objects = {}
    names = {0: 'cat', 1: 'dog'}
    for i,box in enumerate(result.boxes):
        objects[f'object{i+1}'] = {
            'class_id': int(box.cls),
            'class_name': names[int(box.cls)],
            'confidence': "%.2f" %float(box.conf),
            'x1': "%.2f" %float(box.xyxy[0,0]),
            'y1': "%.2f" %float(box.xyxy[0,1]),
            'x2': "%.2f" %float(box.xyxy[0,2]),
            'y2': "%.2f" %float(box.xyxy[0,3]),
            'w': "%.2f" %float(box.xywh[0,2]),
            'h': "%.2f" %float(box.xywh[0,3]),
        }

    return objects,round(end-start)