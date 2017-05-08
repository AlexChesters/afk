import dlib
import base64
import time
from skimage import io
import boto3

client = boto3.client('rekognition', region_name='eu-west-1')

def count_faces(image_path):
    img = io.imread(image_path)
    detector = dlib.get_frontal_face_detector()
    dets = detector(img, 1)
    return len(dets)

def compare_faces(source_image_path, target_image_path):
    source_image = open(source_image_path, 'rb')
    target_image = open(target_image_path, 'rb')
    response = client.compare_faces(
        SourceImage={'Bytes': bytearray(source_image.read())},
        TargetImage={'Bytes': bytearray(target_image.read())}
    )
    return response['FaceMatches']
