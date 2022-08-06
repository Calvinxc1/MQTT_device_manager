from .alert import Alert
from .device import Device
from .sensor import Sensor

resource_map = {
    Alert: ['/alert', '/alert/<alertId>'],
    Device: ['/device', '/device/<deviceId>'],
    Sensor: ['/sensor', '/sensor/<sensorId>'],
}
