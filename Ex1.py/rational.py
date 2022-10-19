def rat():
    from fractions import Fraction
    import actions as a
    import input_data as i
    import logging as l

    firstNum = i.enterNum('первую')
    action = i.enterAction()
    secondNum = i.enterNum('вторую')

    res = 0
    match action:
        case '+': res = a.add(firstNum, secondNum)
        case '-': res = a.sub(firstNum, secondNum)
        case '*': res = a.mult(firstNum, secondNum)
        case '/': res = a.div(firstNum, secondNum)
        case '**': res = a.factor(firstNum, secondNum)
    print(f'Ответ:{res} или {float(res)}')

    l.ratLogger(firstNum, secondNum, action, res)
