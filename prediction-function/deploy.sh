#!/bin/bash

echo CLOUD_PROJECT: \"$CLOUD_PROJECT\" > env.yaml
echo CLOUD_ENDPOINT_ID: \"$CLOUD_ENDPOINT_ID\" >> env.yaml
echo CLOUD_LOCATION: \"$CLOUD_LOCATION\" >> env.yaml

gcloud functions deploy handler --region $CLOUD_LOCATION --runtime python311 --trigger-http --env-vars-file env.yaml
