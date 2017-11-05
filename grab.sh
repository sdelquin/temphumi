#!/bin/bash

cd "$(dirname "$0")"
source $HOME/.virtualenvs/temphumi/bin/activate
python grab.py
