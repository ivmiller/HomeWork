try:
    k=int(input('Введите общее количество билетов\n'))
except ValueError:
    print('Вы ввели некорректные данные.\nВыходим из программы...')
else:
    if k<0:
        print('Количество билетов должно быть положительным.')
    else:
        summ=0.0
        for i in range(1, k+1):
            try:
                age=int(input(f'Введите возраст {i}-го посетителя\n'))
            except ValueError:
                print('Вы ввели некорректные данные.\nВыходим из программы...')
                break
            else:
                if 18<=age<=25:
                    summ += 990
                elif age>25:
                    summ += 1390
                elif age<0:
                    print('Возраст посетителя должен быть больше 0.\nВыходим из программы...')
                    break
        if k>3:
            summ *= 0.9
        print(f'Сумма к оплате: {summ}р')
