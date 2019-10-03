import paho.mqtt.client as mqtt
import threading 
from threading import Thread
from datetime import datetime
import json

appDict = {
  'name': 'messenger',
  'playstore': True,
  'company': 'Facebook',
  'price': 100
}
app_json = json.dumps(appDict)
print(app_json)

# This is the Publisher

def collect_data():
	threading.Timer(5, collect_data).start()
	client = mqtt.Client()
	client.connect("172.16.53.52",1883,60)
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	client.publish("CoreElectronics/test",json.dumps(app_json));
	print("Done")
	client.disconnect();

if __name__ == '__main__':
    Thread(target = collect_data).start()