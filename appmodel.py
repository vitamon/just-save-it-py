APP_ID = "APP_ID"

import json

def valid(**params):
    return APP_ID in params.keys()

def as_json(params):
    json.dumps(params)
    return params