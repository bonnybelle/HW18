# Реализовать итерируемую версию zip - izip чтоб он работал как itertools.izip.


def izip(*args):
    it1 = [str(elem) for elem in args[0][0]]
    it2 = [str(elem) for elem in args[0][1]]
    result = []
    for i in range(len(it1)) and range(len(it2)):
        pair = f'{it1[i]}{it2[i]}'
        i += 1
        result.append(pair)
    return result


request = ('ABCDEFGHIJKLM', 'abcdefghij')
for i in izip(request):
    print(i)
