l1 = ['A', 'B', 'C']
t1 = ('A', 'B', 'C')
print("l1=", hex(id(l1)))
print("t1=", hex(id(t1)))
l1 += ['D']
t1 += ('D',)
print("l1=", hex(id(l1)))
print("t1=", hex(id(t1)))
print("l1=", l1)
print("t1=", t1)

print(t1)