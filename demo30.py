l1 = ['iphoneXS', 'iphone11', 'ipadPro', 'applewatch4',
      'airpodPro']
x1 = 'htc'
#print(x1 in l1)

print(x1 in l1 and l1.index(x1))








items = ['iphoneXS','galaxy','htc','ipadPro','applewatch4',
         'iphone9']
for i in items:
      print(i in l1 and l1.index(i))
# print(x1 in l1)
# print(l1.index(x1))

print('type1', True and True)
print('type2', True and False)
print('type2', True and 3.14)
print('type2', True and 'hello world')
print('type2', True and [1, 3, 5])
print('Or_type1', False or True)
print('Or_type2', False or False)
print('Or_type3', False or 100)
print('Or_type4', False or [1,3,5])
print('Or_type5', False or 'hello world')
print('Or_type6', False or None)