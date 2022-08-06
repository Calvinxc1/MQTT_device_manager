placeholder_resp = {
  "name": "Example Alert",
  "conditions": [
    {
      "type": "less",
      "value": 0.25
    }
  ],
  "sensor": "50eb75f1-a8ab-4057-ac87-016008e2da37",
  "status": "disabled"
}

def put(self, *args, **kwargs):
    data, errors = self._get_request()
    if errors:
        resp = self._build_response({'errors': errors}, 400)
        return resp

    resp = self._build_response(placeholder_resp, 200)
    return resp
