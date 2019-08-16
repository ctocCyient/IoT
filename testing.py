import sched, time
import simplejson as json
my_list = [ 'a', 'b', 'c']
my_json_string = json.dumps(my_list)
print(my_json_string)
""""
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print("Doing stuff...")
    # do your stuff
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()

"""