import json
from pprint import pprint

with open('test2.json', mode='r') as f:
    jsondata = json.loads(f.read())
    pprint(jsondata)

    
