#!/bin/bash

python setup.py sdist --formats=gztar
gsutil cp dist/trainer-0.1.tar.gz gs://$CLOUD_STORAGE_BUCKET/training/trainer-0.1.tar.gz
