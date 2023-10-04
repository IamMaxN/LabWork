a = int(input())
b = int(input())
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

