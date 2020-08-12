n = int(input())
a, b = 0, 1
c = a+b
print(a)
print(b)
for i in range(2, n):
    print(c)
    a, b = b, c
    c = a+b
