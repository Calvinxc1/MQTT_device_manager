placeholder_resp = {
    'records':[{
        "id": "17acc6d4-fdb7-4d43-957c-f70cdca84bd5",
        "name": "Example Alert",
        "sensor": "50eb75f1-a8ab-4057-ac87-016008e2da37",
        "status": "active",
    },{
        "id": "d8539d6a-c397-4208-87de-926ae61eb7be",
        "name": "Example Alert 2",
        "sensor": "d7023769-6080-4784-9a53-bb7fa79e54e0",
        "status": "inactive",
    }],
}

placeholder_resp_specific = {
    'record': {
        "id": "17acc6d4-fdb7-4d43-957c-f70cdca84bd5",
        "name": "Example Alert",
        "conditions": [{
            "type": "less",
            "value": 0.25,
        }],
        "sensor": "50eb75f1-a8ab-4057-ac87-016008e2da37",
        "status": {
            "type": "active",
            "timestamp": 1647896752,
        },
    }
}

def get(self, *args, **kwargs):
    data, errors = self._get_request()
    if errors:
        resp = self._build_response({'errors': errors}, 400)
        return resp
    
    alert_id = self._request.parameters.path.get('alertId')

    resp = self._build_response(placeholder_resp_specific, 200) \
        if alert_id \
        else self._build_response(placeholder_resp, 200)
    
    return resp
