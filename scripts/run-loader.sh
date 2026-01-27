#!/bin/bash

kubectl apply -f test-loader.yaml

echo "Test started. Waiting for loader pod to complete..."
sleep 10
echo "Increasing 30 users up to 30 users"
sleep 10
echo "Increasing 30 users up to 60 users"
sleep 10
echo "Increasing 30 users up to 90 users"
sleep 10
echo "Increasing 30 users up to 120 users"
sleep 10
echo "Increasing 30 users up to 150 users"
sleep 10
echo "Increasing 30 users up to 180 users"
sleep 10
echo "Test completed. Copying results from loader pod..."
# 1-> number of remote copy 2-> test: microservice or SDS
source ./copy-result.sh $1 $2