import json

# some JSON
x = '{"name":"David","age":28,"city":"Nairobi"}'

# parse x
y = json.loads(x)

# the result is a python dictionary
print(y["age"])

# Convert from python to json

# a Python obejct (dict)
x = {"name":"David","age":28,"city":"Nairobi"}

# convert into JSON
y = json.dumps(x, indent=4, sort_keys=True)

# the result is a JSON string
print(y)