

Stack = ['Alfa', 'BMW', 'Cadillac', 'Dodge', 'Edsel', 'Ford', 'GMC', 'Hyundai', 'Infiniti']
print(Stack)
print('')

Stack.append('Chevrolet')
Stack.append('Kia')
print(Stack)
print('')

Stack.pop()
print(Stack)
print('')

Stack.pop(2)       # You wouldn't actually do this with a stack, as the latest addition is the first to come off in a stack...
print(Stack)
print('')