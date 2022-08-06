from .alert import Alert
from .device import Device

resource_map = {
    Alert: ['/alert', '/alert/<alertId>'],
    Device: ['/device', '/device/<deviceId>']
}
