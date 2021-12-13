
myDictionary = {
   1:"one",
   2:"two",
   3:"three",
   4:"four",
   5:"five"
}

print('printing myDictionary')
print(myDictionary)
print('')

myDictionaryCopy = {}

for key, value in myDictionary.items():
   if key != 3:
       myDictionaryCopy[key] = value

print('printing myDictionaryCopy')
print(myDictionaryCopy)
print('')

print('printing myDictionaryCopy after mod')
myDictionaryCopy[3] = 'three'
print(myDictionaryCopy)         # Notice that dictionary is no longer in order by key
print('')

myDictionary = {}

for key, value in sorted(myDictionaryCopy.items()):            # This is a way to get key and value at the same time
    myDictionary[key] = value

print('printing myDictionary after sort')
print(myDictionary)
print('')

print('printing myDictionaryCopy after set equal to myDictionary')
myDictionaryCopy = myDictionary
print(myDictionaryCopy)
print('')
    