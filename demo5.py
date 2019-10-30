import numpy

# print(numpy.pi)
# print(numpy.e)

import sys
def dib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a + b
    print()
dib(int(sys.argv[1]))




