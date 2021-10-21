#!/usr/bin/env bash

pip install virtualenv
virtualenv venv
source venv/bin/activate.sh
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
pip install -r requirements.txt
python main.py
