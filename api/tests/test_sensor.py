import json as js

from src import app

sensor_id = '50eb75f1-a8ab-4057-ac87-016008e2da37'

body_post = {
  "name": "Example Sensor",
  "type": "moisture",
  "sensor": "352b9755-e7de-4a15-bedc-d6af2eb9c755"
}

body_put = {
  "name": "Example Sensor",
  "type": "moisture",
  "sensor": "352b9755-e7de-4a15-bedc-d6af2eb9c755"
}

def test_sensor_get():
    resp = app.test_client().get('/sensor')
    assert resp.status_code == 200

def test_sensor_post():
    resp = app.test_client().post('/sensor', json=body_post)
    assert resp.status_code == 200

def test_sensor_get_specific():
    resp = app.test_client().get(f"/sensor/{sensor_id}")
    assert resp.status_code == 200
    assert js.loads(resp.data)['record']['id'] == sensor_id

def test_sensor_put_specific():
    resp = app.test_client().put(f"/sensor/{sensor_id}", json=body_put)
    assert resp.status_code == 200
    assert js.loads(resp.data)['record']['id'] == sensor_id

def test_sensor_delete_specific():
    resp = app.test_client().delete(f"/sensor/{sensor_id}")
    assert resp.status_code == 200
    assert js.loads(resp.data)['record']['id'] == sensor_id
