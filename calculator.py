a = float(input('Введите первое число  '))  # ввод первого числа
op = input('Введите символ операции  ')  # операция,которую требуется выполнить
b = float(input('Введите второе число  '))  # ввод второго числа
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '/' and b != 0:
    print ('%.2f' % (a / b))  # в ответе выводит 2 цифры после запятой
elif op == '/' and b == 0:
    print('Деление на 0!')
elif op == '*':
    print(a * b)
elif op == '%':
    print(a % b)
elif op == '**':
    print(a ** b)
elif op == '//' and b == 0:
    print('Деление на 0!')
elif op == '//':
    print(a // b)
else:
    print('Ошибка! Повторите попытку!')

