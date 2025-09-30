# 1. Друк без дужок
print "1. Print без дужок"  # Виводимо текст у консоль

# 2. Цілочисельне ділення
print "2. 5 / 2 =", 5 / 2  # Звичайне ділення int/int → 2, не 2.5

# 3. Unicode рядки
s = u"3. Unicode рядок у Python 2"
print s  # Виводимо Unicode рядок

# 4. range повертає список
print "4. range(5):", range(5)  # Створюємо список від 0 до 4

# 5. input та raw_input
name = raw_input("5. Введіть ваше ім'я: ")  # користувач вводить текст
number = input("Введіть число: ")           # користувач вводить число (int)

# 6. Синтаксис обробки виключень
try:
    1 / 0
except ZeroDivisionError, e:  # В Python 2 виняток пишеться так
    print "6. Виняток:", e

# 7. dict.keys() повертає список
d = {'a': 1, 'b': 2}
print "7. dict.keys():", d.keys()  # Виводимо список ключів словника

# 8. Iteritems для словника
print "8. dict.iteritems():"
for k, v in d.iteritems():  # Перебираємо ключі та значення словника
    print k, v

# 9. long тип для великих чисел
big = 12345678901234567890L
print "9. Long число:", big

# 10. cmp функція існує
print "10. cmp(3, 5):", cmp(3, 5)  # Повертає -1, 0 або 1
