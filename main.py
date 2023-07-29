ABC_l = "abcdefghijklmnopqrstuvwxyz"
ABC_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
all_flights = ''

def validation(string,chek):
    """
    :param string: Обьект
    :param chek: Значение проверки
    :return: Допуск
    """
    count = 0
    for _ in string:
        count += 1
    if count != chek:
        print('Не Верный формат')
    return count

def index(s):
    """
    Определяет индекс символа из алфавита:
    :param s: Переменная
    :return: Индекс
    """
    index = 0
    for i in ABC_l:
        index += 1
        if s == i:
            return index

def up(index):
    """
     Заменяет символ
    :param index: Принимает из вспомогательной функции
    :return: Верхний регистор
    """
    i = 0
    for symbol in ABC_up:
        i += 1
        if index == i:
            return symbol
def uppper(string):
    '''
    Заменяем все символы.
    :param string:
    :return: Верхний регистор
    '''
    temp = ''
    for symbol in string:
        if symbol in ABC_l:
            temp += up(index(symbol))
        else:
            temp += symbol
    return temp

def search(num,string):
    """
    функция проверки номера рейса;
    :param num: номер рейса
    :param string: Общая переменная
    :return:
    """
    temp = ''
    count = 0
    flag = False
    for i in string:
        if '\n' not in temp:
            count += 1
            temp += i
            if count == 4 and temp == num:
                flag = True
            elif i not in num and flag == False:
                count = 0
                temp = ''
            elif count == 4 and flag == False:
                count = 0
                temp = ''
        elif temp == '':
            temp = f'Рейс {num} не найден'
    return temp

def show_all_flights(string):
    """Функция чтения всех данных из общей переменной;"""
    temp = ''
    for i in string:
        if i == '\n':
            print('Информация о рейсе: ',temp)
            temp = ''
        elif i != '\n':
            temp += i
    print('')


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
            if validation(flight_number,4) == 4:
                break
        while True:
            date = input("ДД/ММ/ГГГГ - дата рейса: ")
            if validation(date,10)== 10:
                break
        while True:
            time = input('ЧЧ:MM - Время рейса: ')
            if validation(time,5) == 5:
                break
        while True:
            duration = float(input('XX.XX - длительность перелёта: '))
            if validation(duration,5) == 5 and duration > 0:
                break

        while True:
            departure = input('XXX - аэропорт вылета: ')
            if validation(departure,3) == 3:
                break
        while True:
            arrival = input('XXX - аэропорт назначения: ')
            if validation(arrival,3) == 3:
                break
        while True:
            price = float(input('.XX - стоимость билета (> 0): '))
            if price > 0:
                break
        temp = uppper(f"{flight_number} {date} {time} {duration} {departure} {arrival} {price}")
        all_flights += f'{temp}\n'
        print(f'Информация о рейсе {temp} добавлена')

    elif item == 2:
        show_all_flights(all_flights)

    elif item == 3:
        num = input('Введите номер рейса в формате XXXX: ')
        validation(num, 4)
        print(search(uppper(num), all_flights))

