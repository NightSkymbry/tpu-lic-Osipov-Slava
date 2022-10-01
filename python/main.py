import os

import multyply_table, from10convert, to10convert, Home_work_1, morze_rus
import xcar.main as xcar

while True:
    match int(input(
        'Выберите программу\n'
        '----------------------\n'
        '1 - Первое домашнее задание\n'
        '2 - Перевод числа из n<=10 системы счисления в десятичную\n'
        '3 - Перевод числа из десятичной системы счисления в n\n'
        '4 - Таблица умножения для n степени счисления\n'
        '5 - xcar\n'
        '6 - Кодирование русской строки в морзе\n'
        '-> '
        )):
        case 1:
            os.system('cls')
            Home_work_1.run()
        case 2:
            os.system('cls')
            to10convert.run()
        case 3:
            os.system('cls')
            from10convert.run()
        case 4:
            os.system('cls')
            multyply_table.run()
        case 5:
            os.system('cls')
            xcar.run()
        case 6:
            os.system('cls')
            morze_rus.run()
        case _:
            print('Ты дурак\n\n\n\n')
