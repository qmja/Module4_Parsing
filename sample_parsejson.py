import json
import yaml

x = '{"name": "John", "age": "30", "City": "New York City"}'

# parse json

y = json.loads(x)
print("The output of json file is ", y)
print("Name:", y["name"])
print("Age:", y["age"])
print("City:", y["City"])