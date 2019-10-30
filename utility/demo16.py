from decimal import Decimal as Dec
from decimal import ROUND_HALF_UP, \
    ROUND_HALF_DOWN, ROUND_HALF_EVEN

digits = [Dec(1), Dec('0.1'), Dec('0.01'),
          Dec('0.001')]
x1 = Dec(1 / 6)
print(x1)
for d in digits:
    y1 = x1.quantize(d)
    print('1/6 will become', y1)
# x2 = Dec(0.5)
# print(x2)
# x3 = Dec(0.4)
# print(x3)
# rounds = [ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN]
# for r in rounds:
#     print(r)
#     x4 = Dec(1.5)
#     print(type(x4), x4)
#     y4 = x4.quantize(Dec(1), r)
#     print(y4)
#     x5 = Dec(2.5)
#     print(type(x5), x5)
#     y5 = x5.quantize(Dec(1), r)
#     print(y5)
# print("finish loop, do something else")