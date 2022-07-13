#!/bin/bash
docker build -t  eu.gcr.io/krzysiek-master-project/kak-microservice-connector:1.0 .
docker push eu.gcr.io/krzysiek-master-project/kak-microservice-connector:1.0
