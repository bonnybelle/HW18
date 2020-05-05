# Реализовать функцию которая рекурсивно обходит дерево указанной папки и генерирует пути ко всем файлам в дереве.
# Использовать генераторы.

import os


def path_generator(path):
    # print('current path: ' + path)
    for folder in os.listdir(path):
        abs_path = os.path.join(path, folder)
        print('generated path: ' + abs_path.replace('\\', '/'))
        if os.path.isdir(abs_path):
            path_generator(abs_path)
    return 'finished'


print(path_generator('C:/Users/bonny/PycharmProjects/FirstPrj/advanced/HW18/folder1'))
