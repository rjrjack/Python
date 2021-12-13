def fibonacci(n):
    temp1, temp2 = 0, 1
    total = 0
    while total < n:
        yield temp1
        temp3 = temp1 + temp2
        temp1 = temp2
        temp2 = temp3
        total += 1
# End generator fibonacci()

fib_object = fibonacci(20)

print(list(fib_object))
print()

fib_object = fibonacci(20)

comma = ''
numbers = list(fib_object)
for number in numbers:
    print(comma + str(number), end = '')
    comma = ', '