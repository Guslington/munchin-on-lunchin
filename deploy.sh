#!/bin/bash

set -e

mkdir -p build

echo "cleaning build directory"
rm -rf build/*

cp -R api/* build

echo "installing python dependencies"
pip install -r requirements.txt -t build

echo "packaging lambdas"
cd build
zip api.zip -r ./*
cd ..

echo "Testing"
# sam local invoke "WhatsForLunch" # -e event.json --env-vars env.json

echo "packaging cloudformation"
aws cloudformation package \
  --force-upload \
  --template-file template.yaml \
  --s3-bucket source.reference.ci.base2.services \
  --s3-prefix cloudformation/munchinonlunchin \
  --output-template-file packaged-template.yaml

echo "updating/creating cloudformation stack $1-munchinonlunchin"
aws cloudformation deploy \
  --force-upload \
  --no-fail-on-empty-changeset \
  --template-file ./packaged-template.yaml \
  --stack-name $1-munchinonlunchin \
  --parameter-overrides Environment=$1 \
  --capabilities CAPABILITY_IAM
