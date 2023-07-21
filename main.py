def show_all_flights(string):
    temp = ''
    for i in string:
        if i == '\n':
            print('Информация о рейсе: ',temp)
            temp = ''
        elif i != '\n':
            temp += i
    print('')

def chek_data(string):
    count = 0
    for _ in string:
        count += 1
    return count

def search(num,string):
    temp = ''
    count = 0
    for i in string:
        if i in num:
            temp += i
            count += 1
            if count == 4 and temp == num:
                print('1')
    print('')




all_flights = '504N 02/05/2023 18:30 03.30 KUF led 7500\n211U 05/05/2023 10:15 07.20 KZN MMK 15000\n'

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
        while True:
            flight_number = input('XXXX - Введите номер реса: ')
            count = chek_data(flight_number)
            if count == 4:
                break
            print('Не Верный формат')
        while True:
            date = input("ДД/ММ/ГГГГ - дата рейса: ")
            count = chek_data(date)
            if count == 10:
                break
            print('Не Верный формат')
        while True:
            time = input('ЧЧ:MM - Время рейса: ')
            count = chek_data(time)
            if count == 5:
                break
            print('Не Верный формат')
        while True:
            duration = input('XX.XX - длительность перелёта: ')
            count = chek_data(duration)
            if count == 5:
                break
            print('Не Верный формат')
        while True:
            flight_from = input('XXX - аэропорт вылета: ')
            count = chek_data(flight_from)
            if count == 3:
                break
            print('Не Верный формат')
        while True:
            flight_to = input('XXX - аэропорт вылета: ')
            count = chek_data(flight_to)
            if count == 3:
                break
            print('Не Верный формат')
        while True:
            price = float(input('.XX - стоимость билета (> 0): '))
            if price > 0:
                break

        temp = f"{flight_number} {date} {time} {duration} {flight_from} {flight_to} {price}"
        all_flights += f'{temp}\n'
        print(f'Информация о рейсе {temp} добавлена')

    elif item == 2:
        show_all_flights(all_flights)

    elif item == 3:
        num = input('Введите номер рейса в формате XXXX: ')
        search(num,all_flights)
