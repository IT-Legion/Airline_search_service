

all_flights = ''
while True:
    print('Главное меню\n')
    print('1 - ввод рейсов')
    print('2 - вывод всех рейсов')
    print('3 - поиск рейса по номеру')
    print('0 - завершение')
    item = int(input('\nВведите номер пункта меню: '))
    if item == 0:
        print('0')
        break

    elif item == 1:
        flight_number = input('XXXX - Введите номер реса: ')
        date = input("ДД/ММ/ГГГГ - дата рейса: ")
        time = input('ЧЧ:MM - Время рейса: ')
        duration = input('XX.XX - длительность перелёта: ')
        flight_from = input('XXX - аэропорт вылета: ')
        flight_to = input('XXX - аэропорт вылета: ')
        price = input('.XX - стоимость билета (> 0): ')
        temp = flight_number, date, time, duration, flight_from, flight_to, price
        all_flights += f'{temp}\n'
        print(f'Информация о рейсе {temp} добавлена')

    elif item == 2:
        print(f'Информация орейсе: {all_flights}\n')
    elif item == 3:
        num = input('Введите номер рейса в формате XXXX')
        print('3')
