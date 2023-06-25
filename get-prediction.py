#!/usr/bin/env python

import base64
import io
import json
import os
from pathlib import Path
import sys

from google.cloud import functions_v1

if len(sys.argv) < 2:
    sys.exit("Usage: get-prediction.py <png file 1> [png file 2] ...")

project = os.environ['CLOUD_PROJECT']
location = os.environ['CLOUD_LOCATION']
function_name = 'handler'

client = functions_v1.CloudFunctionsServiceClient()
full_function_name = client.cloud_function_path(project, location, function_name)

# For each file in the args:
# - read the bytes
# - encode into b64 byte string,
# - decode into a regular string for JSON
data = {
    'b64_images': [
        base64.b64encode(Path(x).read_bytes()).decode('UTF-8')
        for x in sys.argv[1:]
    ]
}

response = client.call_function(name=full_function_name, data=json.dumps(data))

print(response.result)

