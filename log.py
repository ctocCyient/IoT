# importing module
import logging
import simplejson as json
import time
with open('configuration.json') as f:
  data = json.load(f)

# Create and configure logger
logging.basicConfig(filename=time.strftime("logs/M2M-%Y-%m-%d.log"),format='%(asctime)s %(message)s')

print(type(int(data["configuration"]["Data_interval"])))
# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("Harmless debug Message")
logger.info(data)
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
