from pandas import DataFrame as df


def run():
    system = int(input('Система счисления: '))

    multys = list(range(1, system))

    data = []
    for a in multys:
        data.append([((a*b)//system)*10+((a*b)%system) for b in multys])

    input(df(data, columns = multys, index = multys))
        
    


if __name__ == '__main__':
    run()