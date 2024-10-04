result = 0                                  #   Предварительная версия на 4 окт
incorrect_data = 0
def personal_sum(self):
    global result
    global incorrect_data
    for i in numbers:
        try:
            result += i
        except TypeError:
            print('Некорректный тип данных для подсчёта суммы -', i)
            incorrect_data +=1
        except IndexError:
            print('Неверный тип данных по индексу - >', i)
    return print(result, incorrect_data)
def calculate_average(self):
    personal_sum(numbers)
    sredn = 0
    try:
        if result == 0:
            print('("', numbers, '")')
            print('Коллекция либо пуста, либо не содержит чисел :')
            return
        sredn = result / len(numbers)                   # Высичляем среднее значение по списку
        print('Среднее значение :', sredn)
    except ZeroDivisionError:
        print('Деление на ноль!')
    return sredn


numbers = ("1, 2, 3")
#print(f'Результат 1: {calculate_average(numbers)}')
#numbers = ([1, "Строка", 3, "Ещё Строка"])
print(f'Результат 2: {calculate_average(numbers)}')
