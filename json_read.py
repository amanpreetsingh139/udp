import json

# Read a JSON file
with open('/home/aman/Downloads/600.json') as f:
    data = json.load(f)
# print('data{}'.format(data))
a = json.dumps(data, indent=4, sort_keys=True)
print(a)
print(type(a))

f.close()
