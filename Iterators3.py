
print()

theList = [1,2,3,4,5,6]

theIter = iter(theList)
for x in theIter:
    print(str(x) + '')
print()

theIter = iter(theList)         # the above iteration through iterable 'theIter' consumes theIter, so it must be re-established...
ndx = 0
while ndx < len(theList) - 1:
    print(str(next(theIter)))
    ndx += 1
    
