#!/bin/bash

kubectl apply -f config/test-loader.yaml

echo "Test started. Waiting for loader pod to complete..."
sleep 10
echo "Trying 30 users"
sleep 10
echo "Trying 300 users"
sleep 10
echo "Trying 500 users"
sleep 10
echo "Trying 800 users"
sleep 10
echo "Trying 1200 users"
sleep 10
echo "Trying 1500 users"
sleep 10
echo "Trying 1800 users"
sleep 10
echo "Trying 2000 users"
sleep 10
echo "Test completed. Copying results from loader pod..."
# 1-> number of remote copy 2-> test: microservice or SDS
source scripts/copy-result.sh $1 $2