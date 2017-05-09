import boto3

client = boto3.client('rekognition', region_name='eu-west-1')

def compare_faces(source_image_path, target_image_path):
    source_image = open(source_image_path, 'rb')
    target_image = open(target_image_path, 'rb')
    response = client.compare_faces(
        SourceImage={'Bytes': bytearray(source_image.read())},
        TargetImage={'Bytes': bytearray(target_image.read())}
    )
    return response['FaceMatches']
