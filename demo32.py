l1=[3,1,4,59,26,37,32,50,100]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
l2=list('QWERTYUIOP')
l2.sort()
print(l2)
l3 = list('AabcdBCD123456')
l3.sort()
print(l3)
l3.sort(key=str.lower)
print(l3)
l3.sort(key=str.lower,reverse=True)
print(l3)