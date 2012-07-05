APP_ID = "APP_ID"

import json as j

def valid(**params):
    app_id_key, app_name = get_id_pair(**params)
    return not (app_name == "" or not params[app_id_key])


def as_json(**params):
    return j.JSONEncoder().encode(params)


def list_as_json(data):
    result = ''.join(s.jsoned_params + "," for s in data)
    return "[" + result[:-1] + "]"


def get_id(**param):
    for x in param.keys():
        if x.upper() == APP_ID:
            return param[x]

    return ""


def get_id_pair(**param):
    for x in param:
        if x.upper() == APP_ID:
            return x, param[x]

    return "", ""
