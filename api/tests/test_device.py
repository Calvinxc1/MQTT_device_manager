import json as js

from src import app

device_id = '352b9755-e7de-4a15-bedc-d6af2eb9c755'

body_post = {
  "name": "Example Device",
  "location": "Garden"
}

body_put = {
  "name": "Example Device",
  "location": "Garden",
  "status": "active",
  "sensors": [
    "50eb75f1-a8ab-4057-ac87-016008e2da37",
    "5bd42985-8655-456a-9b9e-bdc0a30c8e48",
    "d7023769-6080-4784-9a53-bb7fa79e54e0"
  ]
}

def test_device_get():
    resp = app.test_client().get('/device')
    assert resp.status_code == 200

def test_device_post():
    resp = app.test_client().post('/device', json=body_post)
    assert resp.status_code == 200

def test_device_get_specific():
    resp = app.test_client().get(f"/device/{device_id}")
    assert resp.status_code == 200
    assert js.loads(resp.data)['record']['id'] == device_id

def test_device_put_specific():
    resp = app.test_client().put(f"/device/{device_id}", json=body_put)
    assert resp.status_code == 200
    assert js.loads(resp.data)['record']['id'] == device_id

def test_device_delete_specific():
    resp = app.test_client().delete(f"/device/{device_id}")
    assert resp.status_code == 200
    assert js.loads(resp.data)['record']['id'] == device_id
