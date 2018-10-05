import os
import json

"""
Check for the existance of generic API keys
to send data to. It fetches them and do the 
required set up for each platform
"""

# Getting API keys from file
with open("api_keys.json") as f:
	api_keys = json.load(f)
	print "Printing dict:"
	print json.dumps(api_keys, indent=4)

# Getting API keys from environment vars in system
# do in bash:
# 	$ export api_username=Javier
# 	$ export api_key=my_api_key

api_username = os.environ.get("api_username")
api_key = os.environ.get("api_key")

print "Printing api keys from environment vars:"
print "api_username: " + str(api_username)
print "api_key: " + str(api_key)