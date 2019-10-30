l1 = [1, 3, 5, 7, 9]
#l1,l2相同位置
l2 = l1
print(l1 == l2, hex(id(l1)), hex(id(l2)))
#l3,l4 值一樣，不同位置
l3 = l1[:]
l4 = list(l1)
l5 = l1.copy()
print(hex(id(l3)),hex(id(l4)),hex(id(l5)))
