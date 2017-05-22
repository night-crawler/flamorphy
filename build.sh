#!/usr/bin/env bash

docker build -t docker.force.fm/ncrawler/flamorphy:latest \
             -t docker.force.fm/ncrawler/flamorphy:0.1.2 \
             -t ncrawler/flamorphy:latest \
             -t ncrawler/flamorphy:0.1.2 \
             .
