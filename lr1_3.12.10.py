# 1. Функція print
print("1. Print with parentheses")  # Виводимо текст у консоль

# 2. Ділення
print("2. 5 / 2 =", 5 / 2)       # Звичайне ділення, результат float (2.5)
print("   5 // 2 =", 5 // 2)     # Цілочисельне ділення, результат int (2)

# 3. Unicode рядки за замовчуванням
s = "3. Unicode рядок у Python 3"
print(s)

# 4. range повертає об’єкт range
print("4. range(5):", list(range(5)))  # перетворюємо на список для виводу

# 5. input завжди повертає рядок
name = input("5. Введіть ваше ім'я: ")  # користувач вводить текст
print("Привіт,", name)

# 6. Синтаксис обробки виключень змінився
try:
    1 / 0
except ZeroDivisionError as e:
    print("6. Виняток:", e)

# 7. dict.keys() повертає view
d = {'a': 1, 'b': 2}
print("7. dict.keys():", list(d.keys()))  # перетворюємо view на список

# 8. items() замість iteritems()
print("8. dict.items():")
for k, v in d.items():  # перебираємо ключі і значення словника
    print(k, v)

# 9. Тип long видалено, всі int можуть бути великими
big = 12345678901234567890
print("9. Велике число:", big)

# 10. cmp видалено, можна використати (a>b)-(a<b)
print("10. cmp(3, 5):", (3 > 5) - (3 < 5))  # результат -1
