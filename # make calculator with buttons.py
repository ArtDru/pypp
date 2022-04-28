# калькулятов 
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("Выберите действие: ")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
c = int(input("Введите номер действия: "))
if c == 1:
    print(a + b)
elif c == 2:
    print(a - b)
elif c == 3:
    print(a * b)
elif c == 4:
    print(a / b)
else:
    print("Неверный ввод")