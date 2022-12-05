a = int(input('Введите первое значение: '))
b = int(input('Введите второе значение: '))

try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print('На ноль делить нельзя!')
print(f'Результат:  {str(result)}')

#ZereDevisionError
