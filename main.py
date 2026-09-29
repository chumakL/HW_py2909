# Рівень 1: розминка
a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
# // при діленні відкидає дробову частину
print(a % b)
# % показує залишоки при діленні
print(2 ** 10)
print(10 ** 3)
price = 249.99
count = 3
total = price * count
print(total)
print(type(7 / 2))
print(type(7 // 2))
print(type(7.0 // 2))
name = "Python"
print(name * 3)
m = "Привіт, "
q = "світ!"
result = m + q
print(result)
# Рівень 2: практичні обчислення
s = 28
p = 6
rows = s // p
rem = s % p
print("Повних рядів: ", rows)
print("Залишок учнів: ",rem)
seconds = 3725
hours = seconds // 3600
minutes = (seconds % 3600) // 60
r_seconds = seconds % 60
print(hours, "год")
print(minutes, "хв")
print(r_seconds, "сек")
minutes2 = 150
hours2 = minutes2 // 60
r_minutes = minutes2 % 60
print(hours2, "год")
print(r_minutes, "хв")
c = 36.6
f = c * 9 / 5 + 32
print("температура по F", f)
side1 = 12.5
side2 = 8
area = side1 * side2
perimeter = 2 * (side1 + side2)
print("Площа:", area)
print("Периметр:", perimeter)
r = 7
pi = 3.14159
area1 = pi * r ** 2
length1 = 2 * pi * r
print("Площа кола:", area1)
print("Довжина кола:", length1)
price1 = 1200
discount = 15
discount_amount = discount * price1 / 100
final_price1 = price1 - discount_amount
print("Знижка: ", discount_amount,"грн")
print("Фінальна ціна: ", final_price1,"грн")
salary = 25000
tax = 19.5
tax_amount = salary * tax / 100
net_salary = salary - tax_amount
print("Податок:", tax_amount, "грн")
print("На руки:", net_salary, "грн")
speed = 90
time = 2.5
distance = speed * time
print("Відстань:", distance, "км")
a1 = 10
b1 = 11
c1 = 8
average = (a1 + b1 + c1) / 3
print("Середнє арифметичне:", average)
# Рівень 3: цифри та числа
n = 7
n2 = 2
result1 = n % n2
if result1 == 0:
    print("Парне")
if result1 == 1:
    print("НЕпарне")
n3 = 473
print(n3 % 10)
num = 473
hundreds = num // 100
tens = num // 10 % 10
units = num * 10
print(hundreds, tens, units)
num1 = 859
total = num1 // 100 + num1 // 10 % 10 + num1 % 10
print(total)
print(144 ** 0.5)
print(365 *24 * 60 * 60)
# Рівень 4: типи данних і хитрощі
x = "5"
y = "3"
# в 106 склеїли рядки
print(x + y)
# в 108 їхня сума
print(int(x) + int(y))
num2 = 9.99
# int це цілі числа
print(int(num2))
print(True + True + True)
print(True * 10)
# тому що bool(true = 1) підклас int
a2 = 5
b2 = 10
a2 = a2 + b2
b2 = a2 - b2
a2 = a2 - b2
print(a2, b2)
deposit = 10000
rate = 0.12
years = 3
sum = deposit * (rate + 1) ** years
print(sum)
print(int(sum))
line = '-'
print(line *20)
print("Результат: " + str(2 **20))
