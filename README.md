# MQTT Device Manager

In summer of 2022 I did research into IoT device managers, and was rather disapointed by the offerings. I couldn't find anything that met my needs for 1) runs on a Raspberry Pi, 2) integrates easily with Portainer, and 3) handled MQTT messaging. As such, since I'm a glutton for punishment I decided to write my own, and here it is!

As time goes on I'll slowly work my way through the development of this application, using all the design techniques and project management approaches I've learned given my history. Expect this repo to evolve over time as I slowly chip away at the work.

## Roadmap
I have a Trello board set up, Kanban style, to help guide my work on this, located [here](https://trello.com/b/bZsH2kNa/mqtt-device-manager).

### Phase 1
Phase 1 of the project will support my monitoring of soil moisture and climate sensors for indoor plants. This should cover the collection, monitoring, alerting, and storage of MQTT data submitted through a MQTT broker across multiple devices, with each device having multiple sensors/measurements.

#### Minimum Viable Product Specification
1. Manage MQTT broker subscriptions
2. Store MQTT data in a database
3. Set alert/action thresholds for incoming data
