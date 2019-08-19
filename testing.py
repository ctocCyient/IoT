import sched, time
import requests

import simplejson as json
my_list = [ 'a', 'b', 'c']
with open('configuration.json') as f:
  data = json.load(f)
print(data)
""""
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print("Doing stuff...")
    # do your stuff
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()

"""


#requests.post(url="http://localhost:3290/sitesurvey_rest/update_data", data=device_data)
