import rational as r
import complex as c
import logging as l


def Mode():
    mode = (int(input('Для работы с комплексными числами введите 1\nДля работы с рациональными числами введите 2\nДля вызова истории запросов введите 3: ')))
    if mode < 1 or mode > 3:
        print('Проверьте правильность ввода!')
        mode = Mode()
        return mode
    else:
        return mode


mode = Mode()

match mode:
    case 1: c.comp()
    case 2: r.rat()
    case 3: l.printLogs()
