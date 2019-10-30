#functional programming
#Tuple 只能新增，不能更改
#
#
t1 = ('A','B','C','D','E','F')
#t1[1]='b'
for t in t1:
    print(t)
l1 = ['A','B','C','D','E','F']
for l in l1:
    print(l)
sales = {'iphone11':500,'ipad':300}
for (k,v) in sales.items():
    print(f'key={k},value={v}')

