# 1. Print function
print("1. Print with parentheses")

# 2. Division
print("2. 5 / 2 =", 5 / 2)  # gives 2.5
print("   5 // 2 =", 5 // 2)  # integer division

# 3. Unicode strings by default
s = "3. Unicode string in Python 3"
print(s)

# 4. range returns a range object
print("4. range(5):", list(range(5)))

# 5. input always returns string
name = input("5. Enter your name: ")
print("Hello,", name)

# 6. Exception syntax changed
try:
    1 / 0
except ZeroDivisionError as e:
    print("6. Exception:", e)

# 7. dict.keys() returns a view
d = {'a': 1, 'b': 2}
print("7. dict.keys():", list(d.keys()))

# 8. items() replaces iteritems()
print("8. dict.items():")
for k, v in d.items():
    print(k, v)

# 9. long type removed, all int can be big
big = 12345678901234567890
print("9. Big number:", big)

# 10. cmp removed, use (a>b)-(a<b)
print("10. cmp(3, 5):", (3 > 5) - (3 < 5))
