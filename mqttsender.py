# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("CoreElectronics/test", "Hello", hostname="172.16.53.52")
publish.single("CoreElectronics/topic", "World!", hostname="172.16.53.52")
print("Done")