from django.apps import AppConfig
from ultralytics import YOLO


class DetectorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'detector'
    yolo8_model = YOLO('detector\weights\\best.pt')
