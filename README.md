# TSL_CatDog_YOLOv8_ObjDet

Training and Deployment code for an object detection model to recognize cat and dog in an image

An Object Detection Application using YOLOv8 (PyTorch and Django Implementation).

Django implementation for Webpage as well as REST API

# Introduction

A web application that provides object detection using YOLOv8 and also generates REST API. It's implemented using Django framework and PyTorch (for YOLO model).

I have developed Django API which accepts an image as request. The input image is converted to float32 type NumPy array and passed on to the YOLOv8 object detection model. The model performs object detection for the image and generates a JSON object with predictions of all the cats and dogs. The Response of the API is the JSON object.

# Required Libraries

The libraries required along with thier version are mentioned below:

* Python  (3.10)

* Django  (4.2)

* ultralytics (8.0.78) 

- whitenoise (6.4.0)

# Required files for Detection

For object detection using Pre-Trained model, we need one important files :

* best.pt - The weights file for the trained model. The file is provided in the GitHub repo.

# Steps to Follow (Working)

This repository can do two things:

1. Implementation web-application

2. Generation of REST API (API testing is done using POSTMAN)

## 1) Webpage Implementation

1.  Clone the GitHub repository

2. Change the directory to the cloned Repository folder.
3. Install all the required libraries from the requirement.txt.
4. Change directory to the catdog_detection api
5.  Execute the code below: (This command needs to be executed only once)
   - `python manage.py collectstatic`
   
   - This command initiates Django and collects all the static files.

6- Then, Execute:
   
   - `python manage.py runserver`
   
   - This command starts Django server. Now we are all set to run the application.

7-  Click on the link. This will direct you to the web browser.

8- Select an image via Drag-&-Drop or Browse mode. and Click on ”Detect Object”

9- Input to Django Web-app is an image. This input image is converted to float32 type NumPy array and passed on to the YOLOv8 model. The model performs object detection for the image and generates a JSON object with names of all the objects and their respective bounding boxes in the image.

10- The Form Response is the JSON object. This JSON object is displayed as a result.

11- Now, click on “Show Predictions” to see the image with Bounding Boxes.

12- To try on other images, click on “Choose a New File”.

## 2) REST API Implementation - POSTMAN

Postman is a scalable API testing tool. The steps to be followed are:

1.  Follow the first 6 steps as mentioned above.

2.  Make sure the server runs properly
3. Open POSTMAN and select POST option. Enter the server link and append /detect/api_request/ to it.
   - For Example : 127.0.0.1:8000/detect/api_request/

4- Click on Body. Enter key value as “Image”. Choose the image file and click on “SEND”.

5. The input image is converted to float32 type NumPy array and passed on to the YOLOv8 model. The model performs object detection for the image and generates a JSON object with names of all the objects and their respective bounding boxes in the image.
6. The HttpResponse is the JSON object. This JSON object is returned.

## 3) Model Training

For training the model we will use roboflow datasets. The datasets used for training are provided as a zip file in the Training folder. A python script is also provided to carry out the training by hand. During training the mAP50-95 metric was used to gain an understanding of the best model. The final is as follows:

```
Ultralytics YOLOv8.0.78 🚀 Python-3.9.16 torch-2.0.0+cu118 CUDA:0 (Tesla T4, 15102MiB)
Model summary (fused): 168 layers, 11126358 parameters, 0 gradients, 28.4 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 6/6 [00:07<00:00,  1.31s/it]
                   all        163        294      0.755      0.757      0.797      0.439
                   cat        163        153      0.805      0.732      0.786      0.456
                   dog        163        141      0.705      0.781      0.808      0.422
Speed: 6.1ms preprocess, 7.5ms inference, 0.0ms loss, 5.4ms postprocess per image
```

 the training was done for 500 epochs on the provided Dataset. To run the train.py file, please change directory to the `Train` folder and execute `python .\train.py -d './cat-and-dog-detection-1.zip' -k`. 



Thank you.  
