placeholder_resp = {
  "message": "Sensor successfully deleted",
  "record": {
    "id": "50eb75f1-a8ab-4057-ac87-016008e2da37",
    "name": "Example Sensor",
    "type": "moisture",
    "device": "352b9755-e7de-4a15-bedc-d6af2eb9c755"
  }
}

def delete(self, *args, **kwargs):
    data, errors = self._get_request()
    if errors:
        resp = self._build_response({'errors': errors}, 400)
        return resp

    resp = self._build_response(placeholder_resp, 200)
    return resp
