
a = int(input("aaaaa"))
b = 350
for x in range(1, a):
    y = a - x
    if 2 * x + 4 * y == b:
        print("鸡有" + str(x) + "只，兔有" + str(y) + "只。")