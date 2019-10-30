l1 = ['A', 'B', 'C']
s1 = "ABC"
print("l1=%s,s1=%s"%(hex(id(l1)),
                     hex(id(s1))))
# mutable
l1[1] = 'b'
print(l1)
# immutable
#s1[1] = 'b'
s1 = "AbC"
print(s1)
print("l1=%s,s1=%s"%(hex(id(l1)),
                     hex(id(s1))))
