l1 = ['Apple','Banana','Citron','Donut','Banana']
print('Apple' in l1)
print('Elephant' in l1)
print('Elephant' not in l1)
for l in l1:
    print(len(l),l)

x1,x2,x3,x4,x5 = l1
print(l1.index('Apple'))


print(l1[l1.index('Banana')+1:].index('Banana'))
