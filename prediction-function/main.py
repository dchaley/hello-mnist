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

    prediction = endpoint.predict(instances=instances)
    return prediction

def image_to_pixels(base64_string):
    decoded_bytes = base64.b64decode(base64_string)
    img = Image.open(BytesIO(decoded_bytes)).convert('L')
    # TODO: resize to 28x28
    normalized_image = (numpy.array(img) / 255)
    return normalized_image.tolist()

def handler(request):
    content_type = request.headers["content-type"]
    if content_type == "application/json":
        request_json = request.get_json(silent=True)
        if request_json and "b64_images" in request_json:
            b64_images = request_json["b64_images"]
        else:
            raise ValueError("JSON is invalid, or missing a 'b64_images' property")
    else:
        raise ValueError(f"Unknown content type: {content_type}")

    image_pixels = [image_to_pixels(x) for x in b64_images]
    prediction = endpoint_predict(PROJECT, LOCATION, image_pixels, ENDPOINT_ID)
    return str([numpy.argmax(x) for x in prediction.predictions])
