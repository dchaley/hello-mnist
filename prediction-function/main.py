import base64
from io import BytesIO
import os

from google.cloud import aiplatform
import numpy
from PIL import Image

PROJECT = os.environ['CLOUD_PROJECT']
ENDPOINT_ID = os.environ['CLOUD_ENDPOINT_ID']
LOCATION = os.environ['CLOUD_LOCATION']

def endpoint_predict(project: str, location: str, instances: list, endpoint: str):
    aiplatform.init(project=project, location=location)

    endpoint = aiplatform.Endpoint(endpoint)

    prediction = endpoint.predict(instances=[instances])
    return prediction

def image_to_pixels(base64_string):
    decoded_bytes = base64.b64decode(base64_string)
    img = Image.open(BytesIO(decoded_bytes))
    # TODO: grayscale + resize to 28x28
    normalized_image = (numpy.array(img) / 255)
    return normalized_image.tolist()

def handler(request):
    content_type = request.headers["content-type"]
    if content_type == "application/json":
        request_json = request.get_json(silent=True)
        if request_json and "image_b64" in request_json:
            image_b64 = request_json["image_b64"]
        else:
            raise ValueError("JSON is invalid, or missing a 'image_b64' property")
    elif content_type == "application/octet-stream":
        image_b64 = request.data
    elif content_type == "text/plain":
        image_b64 = request.data
    else:
        raise ValueError(f"Unknown content type: {content_type}")

    pixels = image_to_pixels(image_b64)
    prediction = endpoint_predict(PROJECT, LOCATION, pixels, ENDPOINT_ID)
    return str(numpy.argmax(prediction.predictions))
