import json

# with open('E:\PythonLearning\sampleJSON.txt', 'r') as f:
#
jsonfile = open('E:\PythonLearning\sampleJSON.txt','r')
jsonobj=json.load(jsonfile)

print(jsonobj["address"]["streetAddress"])

# print in pretty format
print(json.dumps(jsonobj,indent=4))

