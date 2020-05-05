# Реализовать итерируемую версию zip - izip чтоб он работал как itertools.izip.


def izip(object1, object2):
    it1 = [str(elem) for elem in object1]
    it2 = [str(elem) for elem in object2]

    '''if len(it1) > len(it2) or len(it1) < len(it2):
        it1 = it1[0:len(it2)]
        it2 = it2[0:len(it1)]'''  # для уравнивания длины списков

    for i in range(len(it1) - 1):
        for j in range(len(it2) - 1):
            try:
                pair = f'{it1[i]}{it2[j]}'
                print(pair)
                i += 1
                j += 1
            except IndexError:
                quit()


print(izip('ABCDEFGHIJKLM', 'abcdefghij'))
# Я не понимаю, как работает izip, потому что у меня он не импортируется. Примеры из интернета тоже странные.
# Ещё возникает вопрос о двойном итерировании с помощью 'for i ...: for j ... :' -
# как в таком случае сохранять пару один раз?
