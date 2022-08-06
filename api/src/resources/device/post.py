placeholder_resp = {
  "message": "Device successfully created",
  "record": {
    "id": "352b9755-e7de-4a15-bedc-d6af2eb9c755",
    "name": "Example Device",
    "location": "Garden"
  }
}

def post(self, *args, **kwargs):
    data, errors = self._get_request()
    if errors:
        resp = self._build_response({'errors': errors}, 400)
        return resp

    resp = self._build_response(placeholder_resp, 200)
    return resp
