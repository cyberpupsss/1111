import random

#проверка ввода
def int_inp(inp, min_val=None, max_val=None):

    while True:
        try:
            val = int(input(inp))
            if min_val is not None and val < min_val:
                print(f"Ошибка: Число должно быть не меньше {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"Ошибка: Число должно быть не больше {max_val}")
                continue
            return val
        except:
            print("Ошибка: Введите целое число")


def print_matrix(matrix):
    rows = len(matrix)
    if rows == 0:
        print("[]")
        return
    cols = len(matrix[0])

    for i in range(rows):
        row_str = ""
        for j in range(cols):
            row_str += f"{matrix[i][j]:4} "
        print(row_str)



def t1():
    print("Задание 1: Перестановка диагоналей")
    N = int_inp("Введите размерность матрицы N (N > 0): ", 1)

#генерим
    A = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(random.randint(10, 99))
        A.append(row)

    print("Исходная матрица:")
    print_matrix(A)

#перестановка элементов главной и побочной диагоналей
    for i in range(N):
        matrix = A[i][i]
        A[i][i] = A[i][N - 1 - i]
        A[i][N - 1 - i] = matrix

    print("Измененная матрица (диагонали переставлены):")
    print_matrix(A)



def DigitCountSum(K):
    if K < 0:
        K = -K

    count = 0
    total_sum = 0
    ism_K = K

    if ism_K == 0:
        return 1, 0

    while ism_K > 0:
        digit = ism_K % 10
        total_sum += digit
        count += 1
        ism_K //= 10

    return count, total_sum



def t2():
    print("Задание 2: Количество и сумма цифр")
    print("Введите 5 целых положительных чисел")

    for i in range(1, 6):
        num = int_inp(f"Введите число {i}: ", 0)

        C, S = DigitCountSum(num)

        print(f"Число: {num}, количество цифр: {C}, сумма цифр: {S}")



def t3():
    print("Задание 3: Словарь определений")
    n = int_inp("Введите количество слов в словаре (n): ", 1)

    dict = {}

    print(f"Введите {n} строк в формате 'Слово: определение'")
    for i in range(n):
        while True:
            line = input(f"Запись {i + 1}: ")
            if ":" in line:
                parts = line.split(":", 1)
                word = parts[0].strip()
                key = parts[1].strip()
                dict[word] = key
                break
            else:
                print("Используйте двоеточие для разделения слова и определения")

    print("Словарь создан")
    print(f"Словарь: {dict}")

    search_word = input("Введите слово, значение которого хотите узнать: ").strip()

    key = dict.get(search_word)

    if key:
        print(f"Определение: {key}")
    else:
        print("Такого слова нет в словаре")



while True:
    print("1. Задание 1 - Матрица, диагонали")
    print("2. Задание 2 - Сумма и количество цифр")
    print("3. Задание 3 - Словарь")
    print("0. Выход")

    c = input("Выберите номер задания: ")

    if c == '1':
        t1()
    elif c == '2':
        t2()
    elif c == '3':
        t3()
    elif c == '0':
        print("До новых встреч, пользователь <3")
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите пункт меню от 0 до 3")
