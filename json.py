import simplejson as json
# some JSON:
data_iot = {}
data_iot["key"]="Value"
data={}
# the result is a Python dictionary:
print(data_iot["key"])
with open('example_1.json') as f:
  data = json.load(f)
print(data)