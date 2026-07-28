import json
import os

js_temp=""

js_file = r'C:\Users\mohit\personal-mydata\git\python-practices\intermediate\temp.json'
with open(js_file, 'r') as f :
    file = f.read()
    js_temp = json.loads(file)
    print(js_temp)


print(os.getcwd())

# Dict to json

p1 = {"name": "Prashant", "age": 25}
p2 = json.dumps(p1)

print(p2)
print(type(p2))