per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=input('money = ')
deposit=list(per_cent.values())
deposit[:] = [round (x / 100 * int(money)) for x in deposit]
print ('deposit =', deposit)
print ('Максимальная сумма, которую вы можете заработать —', max(deposit))
