l1 = ['Apple', 'Banana', 'Citron']
l2 = ['Purple', 'Queen', 'Rabbit']
print('apple id=', hex(id(l1[0])),
    ',banana id=', hex(id(l1[1])))
l3 = l1 # same list, different name
#print(type(l1), type(l2), type(l3))
print(hex(id(l1)), hex(id(l2)), hex(id(l3)))
l1[0] = 'printer'
l3[1] = 'scanner'
print(l1)
print(l3)
print(hex(id(l1)), hex(id(l3)))
v1 = 'Apple'
print('apple id=', hex(id(v1)))
v1 = 'Banana'
print('banana id=', hex(id(v1)))

