#!/bin/bash
source venv/bin/activate

if [ "$#" == "1" ]; then
    echo $1
    export PYTHON_ENV=$1
fi

python turing_content/project_updater.py
