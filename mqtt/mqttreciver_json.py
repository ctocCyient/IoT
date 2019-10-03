# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
 
import paho.mqtt.client as mqtt
import json
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("CoreElectronics/test")
    client.subscribe("CoreElectronics/topic")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    json_var = json.loads(json.loads(json.loads(json.dumps(msg.payload.decode("utf-8")))))
    print(type(json_var))
    print(json_var["name"])
    print(userdata)
    print(msg.topic)


# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
#client = mqtt.Client(transport="websockets")
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("172.16.53.52",1883, 60)
 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()
