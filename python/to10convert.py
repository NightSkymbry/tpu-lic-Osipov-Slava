def run():
    system = int(input('Основание системы: '))
    NumStart = input(f'Число {system} системы: ')
    if not all([int(i) < system for i in NumStart]):
        raise ValueError(f'You typed the number ({NumStart}) and it is above {system}-th graduate')
    NumEnd = 0
    k = 0
    for i in ''.join(reversed(NumStart)):
        NumEnd += int(i)*system**k
        k += 1
    print(NumEnd)
