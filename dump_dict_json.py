import json

api_auth_dict = {
	"api_user_id" : 123456789,
	"api_user_name" : "user_name_example",
	"api_key" : "api_key_example"
}

with open('api_keys.json', 'w') as outfile:
	# Writing to file
	json.dump(api_auth_dict, outfile, indent=4)
	# Printing to terminal
	print json.dumps(api_auth_dict, indent=4)
