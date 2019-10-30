s1 = 'ABC'
s2 = s1
s3 = 'PQR'
s4 = 'ABC'
s5 = s2
s5 = "aaa"
print(hex(id(s1)), hex(id(s2)),
      hex(id(s3)), hex(id(s4)))
