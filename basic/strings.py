n = 35
# 35 / 2 = 17.5
print("{0} / 2 = {1}".format(n, n / 2))
# 35 // 2 = 17
print("{name} // 2 = {result}".format(name=n, result=(n // 2)))

a = '234\n\t234\'8\''
print("a = {av}".format(av=a))

b = '''234
4567
abc
hello
'''

print("b = {0}".format(b))
print("{vn} turn to UPPER: {upper}".format(upper=b.upper(), vn='b'))
print("{0} turn to Title: {1}".format("b".title(), "b"))
print(b.title())

c = '123'
print(len(c + a))

print(c * 3)


