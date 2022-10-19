def ratLogger(fNum, sNum, action, res):
    f = open('text.txt', 'a')
    f.write(f'{fNum} {action} {sNum} = {res}({float(res)})\n')


def compLogger(fNum, sNum, action, res):
    f = open('text.txt', 'a')
    f.write(f'{fNum} {action} {sNum} = {res}\n')


def printLogs():
    f = open('text.txt', 'r')
    for line in f.readlines():
        print(line)
