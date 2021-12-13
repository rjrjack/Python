
def printer(a, b, c):
    print(a, b, c)
    
    # Lists or tuples can be unpacked into arguments with one asterisk (*) 
    # if the container count matches the number of function parameters.
packedArgs = [1,2,3]    # or (1,2,3)  
print()
printer(*packedArgs)

    # Dictionaries can be unpacked into arguments with two asterisks (**) 
    # if the the count and the keys match the function parameters.
packedKwargs = {'a':4, 'b':5, 'c':6}
print()
printer(**packedKwargs)

# my_dict = {'a': 1, 'b': 2, 'd': 3}    # not possible since wrong keyword
