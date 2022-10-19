from fractions import Fraction
from numbers import Complex


def enterNum(place):
    num = list(map(int, input(f'Введите {place} дробь:').split('/')))
    if len(num) != 2:
        print('Неверно введена дробь, попробуйте еще раз!')
        a = enterNum(place)
        return a
    else:
        a = Fraction(num[0], num[1])
        return a


def enterAction():
    action = input('Введите действие (+,-,*,/,**):')
    if action == '+' or action == '-' or action == '*' or action == '/' or action == '**':
        return action
    else:
        print('Неверно указано действие, попробуйте еще раз!')
        action = enterAction()
        return action


def enterComplexNum(place):
    num = list(map(int, input(
        f'Введите коофициенты {place} комплексного числа через пробел:').split(' ')))
    if len(num) != 2:
        print('Неверно введено комплексное число попробуйте еще раз!')
        a = enterNum(place)
        return a
    else:
        a = complex(num[0], num[1])
        return a
