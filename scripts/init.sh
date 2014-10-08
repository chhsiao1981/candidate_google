#!/bin/bash

git submodule update --init --recursive

virtualenv __

source ./bin/activate

pip install -r requirements.txt

