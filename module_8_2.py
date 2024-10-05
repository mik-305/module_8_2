def personal_sum(self):
    global result
    global incorrect_data
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print('Некорректный тип данных для подсчёта суммы -', i)
            incorrect_data +=1
        except IndexError:
            print('Неверный тип данных по индексу - >', i)
def calculate_average(self):
    if type(numbers) == int: #  Проверка типа входных данных(коллекция или нет)
       print('В numbers записан некорректный тип данных ') # На входе не коллеция
       return               # Прекращаем выполение функции
    personal_sum(numbers)
    sredn = 0
    try:
        if result == 0:
            return result
        sredn = result / (len(numbers) - incorrect_data)              # Cреднее значение по списку - только числа!)
    except ZeroDivisionError:
        print('Деление на ноль!')
    return sredn 


numbers = ("1, 2, 3")
print(f'Результат 1: {calculate_average(numbers)}')
numbers = ([1, "Строка", 3, "Ещё Строка"])
print(f'Результат 2: {calculate_average(numbers)}')
numbers = (567)
print(f'Результат 3: {calculate_average(numbers)}')
numbers = [42, 15, 36, 13]
print(f'Результат 4: {calculate_average(numbers)}')
