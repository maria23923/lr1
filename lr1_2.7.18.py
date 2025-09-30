# Python 2 code
# -*- coding: utf-8 -*-

# 1. Print statement
print "1. Print without parentheses"

# 2. Integer division
print "2. 5 / 2 =", 5 / 2  # gives 2, not 2.5

# 3. Unicode strings
s = u"3. Unicode string in Python 2"
print s

# 4. range returns a list
print "4. range(5):", range(5)

# 5. input and raw_input
name = raw_input("5. Enter your name: ")
number = input("Enter a number: ")

# 6. Exception syntax
try:
    1 / 0
except ZeroDivisionError, e:
    print "6. Exception:", e

# 7. dict.keys() returns a list
d = {'a': 1, 'b': 2}
print "7. dict.keys():", d.keys()

# 8. Iteritems for dictionary
print "8. dict.iteritems():"
for k, v in d.iteritems():
    print k, v

# 9. long type for big numbers
big = 12345678901234567890L
print "9. Long number:", big

# 10. cmp function exists
print "10. cmp(3, 5):", cmp(3, 5)
