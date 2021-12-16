# Напишите программу, которой на вход подается последовательность чисел через пробел, а также
# запрашивается у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному
# в условии ввода данных.
# Далее программа работает по следующему алгоритму:
# --Преобразование введённой последовательности в список
# --Сортировка списка по возрастанию элементов в нем(для реализации сортировки определите функцию)
# --Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий
# за ним больше или равен этому числу.
#
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в
# этом модуле. Реализуйте его также отдельной функцией.
#
# Подсказка
# Помните, что у вас есть числа, которые могут не соответствовать заданному условию. В этом случае необходимо
# вывести соответствующее сообщение.

# можно выбрать: вводим числа с клавиатуры или загружаем из файла

import sys

def sort(L):
    for i in range(len(L)):
        idx_min = i
        for j in range(i, len(L)):
            if L[j] < L[idx_min]:
                idx_min = j
        if i != idx_min:
            L[i], L[idx_min] = L[idx_min], L[i]
    return L

def search(L, num, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if L[middle] == num:
        return middle
    elif num < L[middle]:
        return search(L, num, left, middle - 1)
    else:
        return search(L, num, middle + 1, right)


# алфавит допустимых символов
symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-', ' ', '\n')

input_str = ''  # здесь храним введенную строку
error_symbol = ''  # переменная для хранения неверных символов
my_str = ''

answer = input("Данные возьмем из файла (1) или введем с клавиатуры (2)?\n")
if answer == '1':
    file_name = input('Введите имя файла с последовательностью чисел ')
    try:
        with open(file_name) as file:
           my_str = file.readline()
    except FileNotFoundError:
        print('Файл не найден')
        exit()
elif answer == '2':
    print('Введите последовательность чисел через пробел.')
    my_str = sys.stdin.readline()
else:
    print('При следующем запуске программы введите "1" или "2"\nЗавершаем работу...')
    exit()

for char in my_str:
    if char in symbols:
        input_str += char
    else:
        error_symbol += char
if error_symbol:
    print('Вы ввели недопустимые символы: "' + error_symbol + '"')

# если пользователь поставил минус после числа
try:
    list_of_numbers = list(map(float, input_str.split()))
except ValueError:
    print('Символ "-" должен находиться перед числом\nЗавершаем работу...')
    exit()

# вводим число и добавляем его к списку
number = float(input('Введите число: \n'))
print('Список до сортировки: ' + str(list_of_numbers))
list_of_numbers.append(number)

# сортируем
list_of_numbers = sort(list_of_numbers)

# ищем позицию числа, введенного пользователем
poz = search(list_of_numbers, number, 0, len(list_of_numbers))
if poz == 0:
    print('Введенное число является минимальным среди чисел последовательности')  # поэтому
    # не удовлетворяет нашим условиям
elif list_of_numbers[-1] == number and list_of_numbers[-1] != list_of_numbers[-2]:
    print('Введенное число является максимальным среди чисел последовательности')  # и после него нет числа,
    # равного введенному, поэтому не удовлетворяет нашим условиям
else:
    while list_of_numbers[poz] == list_of_numbers[poz - 1]:
        poz -= 1
    print(f'Индекс элемента списка, который меньше числа {number}: ' + str(poz - 1))
list_of_numbers.pop(poz)
print('Список после сортировки: ' + str(list_of_numbers))
