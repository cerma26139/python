l1 = ['a','b','c']
t1 = ('a','b','c')
l1[1]= 'B'
print(type(l1),type(t1))
print(l1,t1)
t2 = tuple(l1)
l2 = list(t1)
print(t2,l2)
l2[0]='A'
print(l2)
# t2[0]='A'
print(t2)