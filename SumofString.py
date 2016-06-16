total = 0
s = "1.23, 2.4, 3.123"

for c in s.split(","):
    total = total + float(c)
print(str(total))
