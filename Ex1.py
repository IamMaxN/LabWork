a = int(input('введите первое число'))
b = int(input('введите второе чисто'))
#1
print('Сумма: ',a+b)
#2
print('Разность: ',a-b)
#3
print('Произведение: ',a*b)
#4
print('Среднее арифметическое: ',(a+b)/2)
#5
print('Разность максимального и минимального по модулю: ',max(abs(a),abs(b))-min(abs(a),abs(b)))
#5hard
if a < 0:
    a = a * -1
if b < 0:
    b = b * -1
c = a - b
if c < 0:
    c = c * -1
print('hard 5: ', c)

# вывод частного введенных чисел с точность до сотых
ch = float(input("Введите числитель: "))
zn = float(input("Введите знаменатель: "))

if zn == 0:
    print("Невозможно делить на ноль")
else:
    rez = round(ch / zn, 2)
    print("Частное чисел:", rez)
