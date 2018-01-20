import os
import json


"""
Env specific app config get initialized here.
It reads the config file from environment variable.
"""

env_name = os.getenv('APP_CONFIG') or 'prod'

file_name = 'config/' + env_name + '.json'

config = None
with open(file_name, 'r') as cfg_file:
    config = json.load(cfg_file)
