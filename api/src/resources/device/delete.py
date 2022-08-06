placeholder_resp = {
  "message": "Device successfully deleted",
  "record": {
    "id": "352b9755-e7de-4a15-bedc-d6af2eb9c755",
    "name": "Example Device",
    "location": "Garden",
    "status": {
      "status": "active",
      "timestamp": 1647896752
    },
    "sensors": [
      "50eb75f1-a8ab-4057-ac87-016008e2da37",
      "5bd42985-8655-456a-9b9e-bdc0a30c8e48",
      "d7023769-6080-4784-9a53-bb7fa79e54e0"
    ]
  }
}

def delete(self, *args, **kwargs):
    data, errors = self._get_request()
    if errors:
        resp = self._build_response({'errors': errors}, 400)
        return resp

    resp = self._build_response(placeholder_resp, 200)
    return resp
