def generator():
   yield "Welcome"
   yield "to"
   yield "Simplilearn"
# end generator

gen_object = generator()

print(type(gen_object))

for i in gen_object:
   print(i)