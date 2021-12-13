
import json

print()
theList = [1, 'simple', 'list']

print(json.dumps(theList))  # do an edit                                            # JSON string representation
print()

with open('D:\DriveD\Study\Python\Files\JSON.txt', 'wt') as theFile:    # Serialize the object to a text file.
    json.dump(theList,theFile)

with open('D:\DriveD\Study\Python\Files\JSON.txt', 'rt') as theFile:    # Deserialize the object again
    theObject = json.load(theFile)
    print(theObject)
    print(type(theObject))
    print()
    
with open('D:\DriveD\Study\Python\Files\JSON.txt', 'rt') as theFile:    # Can do this too...
    aLine = theFile.read()
    print(aLine)
