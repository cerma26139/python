l1 = list('ABCDEFG')
s1 = "ABCDEFG"
print(type(l1), len(l1), l1)
print(type(s1), len(s1), s1)
s2 = s1
print(s1, s2)
l2 = l1
print(l1, l2)
l1[0] = '*'
l1[1] = 'O'
print(l1, l2)
s1 = 'hello'
s2 = 'world'
print(s1, s2)
