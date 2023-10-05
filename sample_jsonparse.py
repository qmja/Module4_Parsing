import json

with open('sample.json', 'r') as json_file:
    json_data = json.load(json_file)
    print(json_data)
    print(json.dumps(json_data, indent=4))

    for certification in json_data["certifications"]:
        print("Courses:", certification["courses"])
