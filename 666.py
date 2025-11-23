import random

#целое положительное для t3
def int_inp(arg):
    while True:
        try:
            inp = input(arg)
            n = int(inp)
            if n > 0:
                return n
            else:
                print("Ошибка: число должно быть положительным")
        except:
            print("Ошибка: введено не целое число")



#понижение регистра
def lower(c):
    r1 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    r2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    e1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    e2 = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(r1)):
        if c == r1[i]:
            return r2[i]

    for i in range(len(e1)):
        if c == e1[i]:
            return e2[i]

    return c



#модуль
def abs(x):
    return x if x >= 0 else -x



#максимальное
def max(a, b):
    return a if a >= b else b



def t1():
    print("Задание 1: Буква, с которой начинается больше всего слов")
    inp = input("Введите текст: ")

    resultcount = {}
    startword = True
    separator = " ,.!?;:-()[]{}\"\n\t"

    for c in inp:
        letter = ('a' <= lower(c) <= 'z') or ('а' <= lower(c) <= 'я')

        if startword and letter:
            firstletter = lower(c)

            if firstletter in resultcount:
                resultcount[firstletter] += 1
            else:
                resultcount[firstletter] = 1

            startword = False

        elif c in separator:
            startword = True


    mostletter = None
    maxcount = 0
    if not resultcount:
        r = "В тексте нет слов, начинающихся с букв."
    else:
        for letter, count in resultcount.items():
            if count > maxcount:
                maxcount = count
                mostletter = letter
        r = f"Больше всего слов начинается на букву: '{mostletter}' ({maxcount} раз(а))"

    print("Исходный текст:", inp)
    print("Результат:", r)



def t2():

    print("Задание 2: Количество строчных латинских и русских букв")
    inp = input("Введите строку: ")

    ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    en = "abcdefghijklmnopqrstuvwxyz"

    count = 0
    for c in inp:
        if c in ru or c in en:
            count += 1

    print("Исходная строка:", inp)
    print("Результат: Общее количество строчных русских и латинских букв:", count)



def t3():
    print("Задание 3: Операции со списком")
    n = int_inp("Введите размер списка (n): ")
    list = []
    for i in range(n):
        list.append(random.randint(-50, 50))

    print("Исходный список:", list)
    if n == 0:
        print("Список пуст, операции невозможны")
        return


    max_index = 0
    max_abs = abs(list[0])

    for i in range(1, n):
        current_abs = abs(list[i])

        new_max_abs = max(current_abs, max_abs)
        if new_max_abs != max_abs:
            max_abs = new_max_abs
            max_index = i

    print(f"Номер максимального по модулю элемента: {max_index} (элемент: {list[max_index]})")


    sum = 0
    first_positive = False

    for i in range(n):
        element = list[i]
        if first_positive:
            sum += element
        elif element > 0:
            first_positive = True

    if not first_positive:
        print("В списке нет положительных элементов. Сумма равна 0")
    else:
        print(f"Сумма элементов после первого положительного элемента: {sum}")



while True:
    print("1. Задание 1 - Самая частая первая буква в словах")
    print("2. Задание 2 - Подсчет строчных букв")
    print("3. Задание 3 - Операции со списком")
    print("0. Выход")

    c = input("Выберите номер задания: ")

    if c == '1':
        t1()
    elif c == '2':
        t2()
    elif c == '3':
        t3()
    elif c == '0':
        print("До новых встреч, пользователь <3.")
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите пункт меню от 0 до 3.")