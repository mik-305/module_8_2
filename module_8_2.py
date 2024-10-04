result = 0                                  #   Предварительная версия на 4 окт
incorrect_data = 0
def personal_sum(self):
    global result
    global incorrect_data
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data +=1
        except IndexError:
            print('Неверный тип данных по индексу - >', i)
    return print(result, incorrect_data)
def calculate_average(self):
    personal_sum(numbers)
    sredn = 0
    try:
        sredn = result / len(numbers)                   # Высичляем среднее значение по списку
        print('Среднее значение :', sredn)
    except ZeroDivisionError:
        print('Деление на ноль!')
    return sredn


numbers = ("1, 2, 3")
print(f'Результат 1: {calculate_average(numbers)}')







#numbers = (10, 2, 0, 4)
#numbers = ('B','C', 3, 4,'A')
#numbers = (7, 2, 3, 'A', 4, 10)
#personal_sum(numbers)
#calculate_average(numbers)
#print('Результат = ', result)
#print('Количество incorrect_data = ', incorrect_data)