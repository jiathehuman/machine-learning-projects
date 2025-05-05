#! /usr/bin/python

import sys
import os

sys.path.insert(0, "/var/www/flask_predict_api")
sys.path.insert(0, '/opt/conda/lib/python3.6/site-packages')
sys.path.insert(0, "/opt/conda/bin/")

os.environ['PYTHONPATH'] = '/opt/conda/bin/python'

from flask_predict_api import app as application
