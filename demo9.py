a9 = '5+3j'
a10 = complex(a9)
print(type(a9), type(a10))
print(a10.real, a10.imag)
print(a10.conjugate())
a11 = 1
a12 = complex(a11)
print(type(a12), a12)
a13 = -1
a14 = (-1)**0.5
print(type(a14), a14)
#complex arithmatic
a15 = a10.conjugate()
# a+bi ==> (a**2+b**2)**0.5
print(abs(a15), abs(a10))