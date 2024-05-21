n = int(input('Введите первое число кода от 3 до 20:'))
print('Ваш пароль:')
if n in range(1, 21):
    for i in range(1, n-1):
        for j in range(i + 1, n):
            sum_ = i + j
            if n % sum_ == 0:
                for result in (i, j):
                    print(result, end='')
