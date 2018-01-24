#!/bin/bash

while(true); do
    python3 -m unittest "$1"
    sleep 2
done

