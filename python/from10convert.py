
def run():
    toSys = int(input('Основание системы: '))
    NumStart = int(input(f'Число 10 системы: '))
    NumEnd = []

    while NumStart != 0:
        NumEnd.append(str(NumStart%toSys))
        NumStart//=toSys
    input('Ответ: ' + ''.join(reversed(NumEnd)))


if __name__ == '__main__':
    run()