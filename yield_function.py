import math

def cubes(number):
    return int(math.pow(number,3))
# end cubes

def getCubes(range_of_nums):            # a generator can yield (call) a function
    for i in range(range_of_nums):
        yield cubes(i)
# end getCubes      
       
cube_object = getCubes(5)

print(list(cube_object))