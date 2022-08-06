placeholder_resp = {
  "records": [
    {
      "id": "352b9755-e7de-4a15-bedc-d6af2eb9c755",
      "name": "Example Device",
      "location": "Garden",
      "status": "active"
    },
    {
      "id": "365213d0-449e-4ddc-af12-1922a787f1b8",
      "name": "Example Device 2",
      "location": "Greenhouse",
      "status": "inactive"
    }
  ]
}

placeholder_resp_specific = {
  "record": {
    "id": "352b9755-e7de-4a15-bedc-d6af2eb9c755",
    "name": "Example Device",
    "location": "Garden",
    "status": {
      "type": "active",
      "timestamp": 1647896752
    },
    "sensors": [
      "50eb75f1-a8ab-4057-ac87-016008e2da37",
      "5bd42985-8655-456a-9b9e-bdc0a30c8e48",
      "d7023769-6080-4784-9a53-bb7fa79e54e0"
    ]
  }
}

def get(self, *args, **kwargs):
    data, errors = self._get_request()
    if errors:
        resp = self._build_response({'errors': errors}, 400)
        return resp
    
    alert_id = self._request.parameters.path.get('deviceId')

    resp = self._build_response(placeholder_resp_specific, 200) \
        if alert_id \
        else self._build_response(placeholder_resp, 200)
    
    return resp
