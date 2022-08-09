import json as js

from src import app

alert_id = '17acc6d4-fdb7-4d43-957c-f70cdca84bd5'

body_post = {
  "name": "Example Alert",
  "conditions": [
    {
      "type": "less",
      "value": 0.25
    }
  ],
  "sensor": "50eb75f1-a8ab-4057-ac87-016008e2da37"
}

body_put = {
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

def test_alert_get():
    resp = app.test_client().get('/alert')
    assert resp.status_code == 200

def test_alert_post():
    resp = app.test_client().post('/alert', json=body_post)
    assert resp.status_code == 200

def test_alert_get_specific():
    resp = app.test_client().get(f"/alert/{alert_id}")
    assert resp.status_code == 200
    assert js.loads(resp.data)['record']['id'] == alert_id

def test_alert_put_specific():
    resp = app.test_client().put(f"/alert/{alert_id}", json=body_put)
    assert resp.status_code == 200
    assert js.loads(resp.data)['record']['id'] == alert_id

def test_alert_delete_specific():
    resp = app.test_client().delete(f"/alert/{alert_id}")
    assert resp.status_code == 200
    assert js.loads(resp.data)['record']['id'] == alert_id
