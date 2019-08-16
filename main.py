import sensor_data as IoT
import simplejson as json
import requests
import time;

data={}
# the result is a Python dictionary:
server_data = []
with open('example_1.json') as f:
  data = json.load(f)

for (k, v) in data.items():

   if(k!="configuration"):
       if(v.get("DeviceType")=="Analog"):
           device_data = {}
           value = IoT.read_data_rs485_holding(data['configuration'],v)
           if v.get("Threshold")==value:
               print("send alarm")
           else:
               device_data['Gatewayname']=v.get("Gatewayname")
               device_data['parameter']=k
               device_data['timestamp']=time.time()
               device_data['value']=value
               server_data.append(device_data)

       if (v.get("DeviceType") == "Digital"):
           device_data = {}
           value = IoT.read_data_IO(v.get("PIN"),v.get("Mode"))
           if v.get("Threshold") == value:
               print("send alarm")
           else:
               device_data['Gatewayname'] = v.get("Gatewayname")
               device_data['parameter'] = k
               device_data['timestamp'] = time.time()
               device_data['value'] = value
               server_data.append(device_data)


print(server_data)


#IoT.read_data_rs485(data['configuration'],data['Temperature_Temperature'])