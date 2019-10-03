# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("CoreElectronics/test", "Hello", hostname="192.168.240.131")
publish.single("CoreElectronics/topic", "World!", hostname="192.168.240.131")
print("Done")