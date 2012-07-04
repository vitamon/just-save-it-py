APP_ID = "APP_ID"

import json as j

def valid(**params):
    return APP_ID in [x.upper() for x in params.keys()]


def as_json(**params):
    return j.JSONEncoder().encode(params)


def get_id(**param):
    for x in param.keys():
        if x.upper() == APP_ID:
            return param[x]

    return ""
