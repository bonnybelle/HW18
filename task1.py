# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерирования по генератору необходимо проверять строки на уникальность.
# Если строка уже была выведена ранее - то мы её прпускаем, иначе выводим на экран.

path = 'C:/Users/bonny/PycharmProjects/FirstPrj/advanced/HW18/task1_file.txt'


def task(path):
    with open(path, 'r', encoding='UTF-8') as file:
        a = [line for line in file][::-1]
        result = [a[i] for i in range(len(a)) if a[i] not in a[i+1:]][::-1]
    return result


for i in task(path):
    print(i, end='')
