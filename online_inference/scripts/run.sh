#!/bin/bash

docker build -t maksima1ist/online_inference:1.0.2 .
docker run -p 5000:5000 maksima1ist/online_inference:1.0.2
