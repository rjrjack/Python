
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

        # convert into JSON:
person_json = json.dumps(person)

        # use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", " = "), sort_keys=True)

        # the result is a JSON string:
print()
print(person_json) 
print()
print(person_json2) 

print()
print('*********************')
print()

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

with open('D:\DriveD\Study\Python\Files\person.json', 'w') as f:
    json.dump(person, f)                                                            
    
with open('D:\DriveD\Study\Python\Files\person2.json', 'w') as f2:
    json.dump(person, f2, indent=4, separators=("; ", "= "), sort_keys=True)

print()
print('*********************')
print()

        # Convert a JSON string into a Python object with the 
        # json.loads() method. The result will be a Python dictionary.

person_json = """
{
    "age": 30, 
    "city": "New York",
    "hasChildren": false, 
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""

person = json.loads(person_json)        # Notice that this uses json.loads(), while the
print(person)                           # below 'from file' uses json.load()
print(type(person))

print()
print('*********************')
print()

        # Load data from a file and convert it to a Python object 
        # with the json.load() method.
        
with open('D:\DriveD\Study\Python\Files\person.json', 'r') as f:
    person = json.load(f)
    print(person)
    print(type(person))