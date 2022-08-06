placeholder_resp = {
  "records": [
    {
      "id": "50eb75f1-a8ab-4057-ac87-016008e2da37",
      "name": "Example Sensor",
      "type": "moisture",
      "device": "352b9755-e7de-4a15-bedc-d6af2eb9c755"
    },
    {
      "id": "5bd42985-8655-456a-9b9e-bdc0a30c8e48",
      "name": "Example Sensor 2",
      "type": "temperature",
      "device": "352b9755-e7de-4a15-bedc-d6af2eb9c755"
    },
    {
      "id": "d7023769-6080-4784-9a53-bb7fa79e54e0",
      "name": "Example Sensor 3",
      "type": "humidity",
      "device": "352b9755-e7de-4a15-bedc-d6af2eb9c755"
    }
  ]
}

placeholder_resp_specific = {
  "record": {
    "id": "50eb75f1-a8ab-4057-ac87-016008e2da37",
    "name": "Example Sensor",
    "type": "moisture",
    "device": "352b9755-e7de-4a15-bedc-d6af2eb9c755"
  }
}


def get(self, *args, **kwargs):
    data, errors = self._get_request()
    if errors:
        resp = self._build_response({'errors': errors}, 400)
        return resp
    
    alert_id = self._request.parameters.path.get('sensorId')

    resp = self._build_response(placeholder_resp_specific, 200) \
        if alert_id \
        else self._build_response(placeholder_resp, 200)
    
    return resp
