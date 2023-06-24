#!/usr/bin/env python

import os
import sys

from google.cloud import aiplatform
import numpy
from PIL import Image

if len(sys.argv) < 2:
    sys.exit("Usage: get-prediction.py <png file>")

project = os.environ['CLOUD_PROJECT']
endpoint_id = os.environ['CLOUD_ENDPOINT_ID']
location = os.environ['CLOUD_LOCATION']

def endpoint_predict_sample(
    project: str, location: str, instances: list, endpoint: str
):
    aiplatform.init(project=project, location=location)

    endpoint = aiplatform.Endpoint(endpoint)

    prediction = endpoint.predict(instances=[instances])
    return prediction

def image_to_pixels(filename: str):
    im = Image.open(sys.argv[1])
    normalized_image = (numpy.array(im) / 255)
    return normalized_image.tolist()

input_data = image_to_pixels(sys.argv[1])

prediction = endpoint_predict_sample(project, location, input_data, str(endpoint_id))

print(prediction)
print(numpy.argmax(prediction.predictions))

