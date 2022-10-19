def comp():
    import actions as a
    import input_data as i
    import logging as l

    firstNum = i.enterComplexNum('первого')
    print(firstNum)
    action = i.enterAction()
    secondNum = i.enterComplexNum('второго')
    print(secondNum)

    res = 0
    match action:
        case '+': res = a.add(firstNum, secondNum)
        case '-': res = a.sub(firstNum, secondNum)
        case '*': res = a.mult(firstNum, secondNum)
        case '/': res = a.div(firstNum, secondNum)
        case '**': res = a.factor(firstNum, secondNum)
    print(f'Ответ:{res}')

    l.compLogger(firstNum, secondNum, action, res)
