val = input()
l = len(val)
s = 0
for i in val:
    s += int(i)**l

if s == int(val):
    print("Number is Armstrong !!")
else:
    print("Number is not Armstrong !!")
