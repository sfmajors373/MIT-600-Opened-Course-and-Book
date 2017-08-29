"""  identifying vowels in string s  """


count = 0
s = abebibobu
for char in s:
    if char in [a, e, i, o, u]:
        count += 1
print("Number of vowels: " + str(count))
