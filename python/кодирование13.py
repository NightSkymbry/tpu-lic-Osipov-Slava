from math import log2, ceil
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style


def convert(val: str | int | float, system: str, from_: str, to: str | None = None) -> float | int:
        try:
            if to is None:
                return eval(str(val)) * systems[system][from_]
            else:
                return eval(str(val)) * systems[system][from_] / systems[system][to]
        except IndexError as e:
            raise
        except ValueError as e:
            raise


def scan_given(g: str, u: dict[str, dict[str, str]]) -> list[str, int] | str:
    given = {}
    g = g.strip()
    if g == '':
        return 'Не дано ничего.'
    
    g = g.split(';')
    for i in g:
        i = i.strip()
        if i == '': continue
        
        if i.find('=') == -1:
            return f'В подстроке "{i}" отсутствует знак ='
        
        i = list(map(lambda x: x.strip(), i.split('=')[:2]))
        if i[0] in u.keys():
            if u[i[0]] is None:
                given[i[0]] = i[1]
            else:
                a = i[1].split()
                if len(a) > 1:
                    if a[1] in systems[u[i[0]]['system']].keys():
                        given[i[0]] = convert(a[0], u[i[0]]['system'], a[1])
                    else:
                        return f'Для перемнной "{i[0]}" указана недопустимая единица измерения - "{a[1]}"'
                else:
                    given[i[0]] = convert(a[0], u[i[0]]['system'], u[i[0]]['base'])
        else:
            given[i[0]] = i[1].split()[0]
    
    return given


def scan_to_find(tf: str, u: dict[str, dict[str, str]]) -> list[str, int] | str:
    to_find = {}
    tf = tf.strip()
    if tf == '':
        return 'Маловато запрошено.'
    
    tf = tf.split(';')
    for i in tf:
        i = i.strip()
        if i == '': continue
        
        if i.find(' ') == -1:
            if i not in u.keys():
                to_find[i] = None
            elif u[i] is None:
                return f'Переменная "{i}" может быть указана исключительно в Дано'
            else:
                to_find[i] = list(systems[u[i]['system']].keys())
        else:
            i = list(map(lambda x: x.strip(), [i.split(' ')[0], ' '.join(i.split(' ')[1:])]))
            if i[0] not in u.keys():
                to_find[i[0]] = None
            elif u[i[0]] is None:
                return f'Переменная "{i[0]}" может быть указана исключительно в Дано'
            else:
                pos_u = list(systems[u[i[0]]['system']].keys())
                units = []
                for l in i[1].split(','):
                    l = l.strip()
                    if l == '': continue
                    
                    if l in pos_u:
                        units.append(l)
                    else:
                        # print(tf, i, l)
                        return f'Я надеюсь, что в следующей попытке вы получше объясните значение еденицы измерения "{l}" для переменной "{i[0]}"'
                to_find[i[0]] = units
            
    
    return to_find


systems = {
    'b-TB': {'b': 1, 'B': 8, 'KB': 8*1024, 'MB': 8*(1024**2), 'GB': 8*(1024**3), 'TB': 8*(1024**4)},
    's-d': {'s': 1, 'm': 60, 'h': 60*60, 'd': 60*60*24},
    'Hz-MHz': {'Hz': 1, 'KHz': 1000, 'MHz': 1000**2}
}


def information():

    basic_units = {
        'I': {'system': 'b-TB', 'base': 'B', 'base_': 'b'},
        'i': {'system': 'b-TB', 'base': 'b'},
        'kt': None
    }
    
    
    g = input('''\n\n\nМожно использовать:
N  (Мощность алфавита)
I  (Инф. объём текста) [ b, <B>, KB, MB, GB, TB ]
i  (Инф. объём символа) [ <b>, B, KB, MB, GB, TB ]
k  (Количество символов в тексте)
kt (Текст) (Только для дано)
--------------------------
Дано -> ''').replace(',', '.')
    given = scan_given(g, basic_units)
    
    if type(given) is str:
        print(f'{Fore.RED}\nЧувак, ты как то не так ввёл данные, а конкретнее:\n{Style.BRIGHT}{given}\n\n{Fore.WHITE}{Style.NORMAL}Попробуй ка уточнить данные.\n\n')
        return
    
    t_f = input('Найти -> ')
    to_find = scan_to_find(t_f, basic_units)
    
    if type(to_find) is str:
        print(f'{Fore.RED}\nЧувак, ты как то не так ввёл данные, а конкретнее:\n{Style.BRIGHT}{to_find}\n\n{Fore.WHITE}{Style.NORMAL}Попробуй ка уточнить данные.\n\n')
        return
    
    # print(given, to_find)
    
    if 'kt' in given.keys():
        given['k'] = len(given['kt'])
    if 'k' in given.keys():
        given['k'] = int(given['k'])
    if 'N' in given.keys():
        given['N'] = int(given['N'])
    
    # print(given, to_find)
    result = {}
    
    for var, units in to_find.items():
        match var:
            case 'I':
                if 'k' in given.keys() and 'i' in given.keys():
                    result['I'] = [str(convert(given['k'] * given['i'], basic_units['I']['system'], basic_units['I']['base_'], to=u)) + f' {u}' for u in units]
                elif 'k' in given.keys() and 'N' in given.keys():
                    if given['N'] > 0:
                        result['I'] = [str(convert(given['k'] * (ceil(log2(given['N'])) if N != 1 else 1), basic_units['I']['system'], basic_units['I']['base_'], to=u)) + f' {u}' for u in units]
                    else:
                        print(Fore.YELLOW + f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", почему то в алфавите нет букв ¯\(°_o)/¯')
                elif 'I' in given.keys():
                    result['I'] = [str(convert(given['I'], basic_units['I']['system'], basic_units['I']['base_'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case 'k':
                if 'I' in given.keys() and 'i' in given.keys():
                    if given['i'] != 0:
                        result['k'] = [given['I'] / given['i']]
                    else:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (i) я не проходил ƪ(˘⌣˘)ʃ')
                elif 'I' in given.keys() and 'N' in given.keys():
                    if given['N'] > 0:
                        result['k'] = [given['I'] / (ceil(log2(given['N'])) if N != 1 else 1)]
                    else:
                        print(Fore.YELLOW + f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", почему то в алфавите нет букв ¯\(°_o)/¯')
                elif 'k' in given.keys():
                    result['k'] = [given['k']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case 'i':
                if 'I' in given.keys() and 'k' in given.keys():
                    if given['k'] != 0:
                        result['i'] = [str(convert(given['I'] / given['k'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                    else: 
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (k) я не проходил ƪ(˘⌣˘)ʃ')
                elif 'N' in given.keys():
                    if given['N'] > 0:
                        result['i'] = [str(convert((ceil(log2(given['N'])) if N != 1 else 1), basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                    else:
                        print(Fore.YELLOW + f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", почему то в алфавите нет букв ¯\(°_o)/¯')
                elif 'i' in given.keys():
                    result['i'] = [str(convert(given['i'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case 'N':
                if 'i' in given.keys():
                    result['N'] = [2**given['i']]
                elif 'I' in given.keys() and 'k' in given.keys():
                    if given['k'] != 0:
                        result['N'] = [2**(given['I'] / given['k'])]
                    else:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (k) я не проходил ƪ(˘⌣˘)ʃ')
                elif 'k' in given.keys():
                    result['N'] = [given['N']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case _:
                print(Fore.YELLOW + f'WARN! Unknown variable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}.\nIf you meant something else, please restsrt the programm.')
    
    # print(result)
    for var, res in result.items():
        print(f'{var} = {"; ".join(map(str, res))}')


def sound():

    basic_units = {
        'I': {'system': 'b-TB', 'base': 'MB', 'base_': 'b'},
        'i': {'system': 'b-TB', 'base': 'b'},
        't': {'system': 's-d', 'base': 's'},
        'D': {'system': 'Hz-MHz', 'base': 'KHz', 'base_': 'Hz'}
    }


    g = input('''\n\n\nМожно использовать:
I (Инф. объём Файла) [ b, B, KB, <MB>, GB, TB ]
D (Частота дискретизации) [ Hz, <KHz>, MHz ]
t (Время звучания) [ <s>, m, h, d ]
i (Глубина кодирования) [ <b>, B, KB, MB, GB, TB ]
k (Количество каналов) = 1
--------------------------
Дано -> ''').replace(',', '.')
    given = scan_given(g, basic_units)
    
    if type(given) is str:
        print(f'{Fore.RED}\nЧувак, ты как то не так ввёл данные, а конкретнее:\n{Style.BRIGHT}{given}\n\n{Fore.WHITE}{Style.NORMAL}Попробуй ка уточнить данные.\n\n')
        return
    
    t_f = input('Найти -> ')
    to_find = scan_to_find(t_f, basic_units)
    
    if type(to_find) is str:
        print(f'{Fore.RED}\nЧувак, ты как то не так ввёл данные, а конкретнее:\n{Style.BRIGHT}{to_find}\n\n{Fore.WHITE}{Style.NORMAL}Попробуй ка уточнить данные.\n\n')
        return
    
    if 'k' in given.keys():
        given['k'] = int(given['k'])
    if 'k' not in given.keys() and 'k' not in to_find.keys():
        given['k'] = 1
    
    result = {}
    
    for var, units in to_find.items():
        match var:
            case 'I':
                if 'I' in given.keys():
                    result['I'] = [str(convert(given['I'], basic_units['I']['system'], basic_units['I']['base_'], to=u)) + f' {u}' for u in units]
                elif 'k' in given.keys() and 'D' in given.keys() and 't' in given.keys() and 'i' in given.keys():
                    result['I'] = [str(convert(given['k'] * given['D'] * given['t'] * given['i'], basic_units['I']['system'], basic_units['I']['base_'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            case 'k':
                if 'k' in given.keys():
                    result['k'] = [given['k']]
                elif 'I' in given.keys() and 'D' in given.keys() and 't' in given.keys() and 'i' in given.keys():
                    if given['D'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (D) я не проходил ƪ(˘⌣˘)ʃ')
                    elif given['t'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (t) я не проходил ƪ(˘⌣˘)ʃ')
                    elif given['i'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (i) я не проходил ƪ(˘⌣˘)ʃ')
                    else:
                        result['k'] = [given['I'] / (given['D'] * given['t'] * given['i'])]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            case 'D':
                if 'D' in given.keys():
                    result['D'] = [str(convert(given['D'], basic_units['D']['system'], basic_units['D']['base_'], to=u)) + f' {u}' for u in units]
                elif 'k' in given.keys() and 'I' in given.keys() and 't' in given.keys() and 'i' in given.keys():
                    if given['k'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (k) я не проходил ƪ(˘⌣˘)ʃ')
                    elif given['t'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (t) я не проходил ƪ(˘⌣˘)ʃ')
                    elif given['i'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (i) я не проходил ƪ(˘⌣˘)ʃ')
                    else:
                        result['D'] = [str(convert(given['I'] / (given['k'] * given['t'] * given['i']), basic_units['D']['system'], basic_units['D']['base_'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            case 't':
                if 't' in given.keys():
                    result['t'] = [str(convert(given['t'], basic_units['t']['system'], basic_units['t']['base'], to=u)) + f' {u}' for u in units]
                elif 'k' in given.keys() and 'I' in given.keys() and 'D' in given.keys() and 'i' in given.keys():
                    if given['D'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (D) я не проходил ƪ(˘⌣˘)ʃ')
                    elif given['k'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (k) я не проходил ƪ(˘⌣˘)ʃ')
                    elif given['i'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (i) я не проходил ƪ(˘⌣˘)ʃ')
                    else:
                        result['t'] = [str(convert(given['I'] / (given['k'] * given['D'] * given['i']), basic_units['t']['system'], basic_units['t']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            case 'i':
                if 'i' in given.keys():
                    result['i'] = [str(convert(given['i'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                elif 'k' in given.keys() and 'I' in given.keys() and 'D' in given.keys() and 't' in given.keys():
                    if given['D'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (D) я не проходил ƪ(˘⌣˘)ʃ')
                    elif given['t'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (t) я не проходил ƪ(˘⌣˘)ʃ')
                    elif given['k'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (k) я не проходил ƪ(˘⌣˘)ʃ')
                    else:
                        result['i'] = [str(convert(given['I'] / (given['k'] * given['D'] * given['t']), basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case _:
                print(Fore.YELLOW + f'WARN! Unknown variable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}.\nIf you meant something else, please restsrt the programm.')
    
    # print(result)
    for var, res in result.items():
        print(f'{var} = {"; ".join(map(str, res))}')


def picture():

    basic_units = {
        'V': {'system': 'b-TB', 'base': 'MB', 'base_': 'b'},
        'i': {'system': 'b-TB', 'base': 'b'},
    }


    def convert(val: str | int | float, system: str, from_: str, to: str | None = None) -> float | int:
        try:
            if to is None:
                return eval(str(val)) * systems[system][from_]
            else:
                return eval(str(val)) * systems[system][from_] / systems[system][to]
        except IndexError as e:
            raise
        except ValueError as e:
            raise
    
    
    
    g = input('''\n\n\nМожно использовать:
V (Объём видеопамяти) [ b, B, KB, <MB>, GB, TB ]
N (Количество цветов)
r (Количество пикселей)
i (Глубина цвета) [ <b>, B, KB, MB, GB, TB ]
x (Количество пикселей по горизонтали)
y (Количество пикселей по вертикали)
--------------------------
Дано -> ''').replace(',', '.')
    given = scan_given(g, basic_units)
    
    if type(given) is str:
        print(f'{Fore.RED}\nЧувак, ты как то не так ввёл данные, а конкретнее:\n{Style.BRIGHT}{given}\n\n{Fore.WHITE}{Style.NORMAL}Попробуй ка уточнить данные.\n\n')
        return
    
    t_f = input('Найти -> ')
    to_find = scan_to_find(t_f, basic_units)
    
    if type(to_find) is str:
        print(f'{Fore.RED}\nЧувак, ты как то не так ввёл данные, а конкретнее:\n{Style.BRIGHT}{to_find}\n\n{Fore.WHITE}{Style.NORMAL}Попробуй ка уточнить данные.\n\n')
        return
    
    if 'N' in given.keys() and int(given['N']) > 0:
        given['N'] =  int(given['N'])
        given['i'] = (ceil(log2(given['N'])) if given['N'] != 1 else 1)
    elif 'i' in given.keys():
        given['N'] = 2**given['i']
    elif 'V' in given.keys() and 'r' in given.keys() and given['r'] != 0:
        given['N'] = 2**(given['V'] / given['r'])
    elif 'V' in given.keys() and 'x' in given.keys() and 'y' in given.keys() and given['y'] != 0 and given['x'] != 0:
        given['N'] = 2**(given['V'] / (given['x'] * given['y']))
        
    if 'x' in given.keys():
        given['x'] = int(given['x'])
    if 'y' in given.keys():
        given['y'] = int(given['y'])
    if 'r' in given.keys():
        given['r'] = int(given['r'])
    
    if 'V' in given.keys() and 'i' in given.keys() and given['i'] != 0:
        given['r'] = [given['V'] / given['i']]
    
    if 'x' in given.keys() and 'y' in given.keys():
        given['r'] = given['x'] * given['y']
    elif 'r' in given.keys() and 'y' in given.keys() and given['y'] != 0:
        given['x'] = given['r'] / given['y']
    elif 'r' in given.keys() and 'x' in given.keys() and given['x'] != 0:
        given['y'] = given['r'] / given['x']
    
    result = {}

    for var, units in to_find.items():
        match var:
            case 'V':
                if 'V' in given.keys():
                    result['V'] = [str(convert(given['V'], basic_units['V']['system'], basic_units['V']['base_'], to=u)) + f' {u}' for u in units]
                elif 'i' in given.keys() and 'r' in given.keys():
                    result['V'] = [str(convert(given['i'] * given['r'], basic_units['V']['system'], basic_units['V']['base_'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
                
            case 'i':
                if 'i' in given.keys():
                    result['i'] = [str(convert(given['i'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                elif 'V' in given.keys() and 'r' in given.keys():
                    if given['r'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (r = x*y) я не проходил ƪ(˘⌣˘)ʃ')
                    else:
                        result['i'] = [str(convert(given['V'] / given['r'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
                
            case 'r':
                if 'r' in given.keys():
                    result['r'] = [given['r']]
                elif 'V' in given.keys() and 'i' in given.keys():
                    if given['i'] == 0:
                        print(f'Я затрудняюсь с нахождением "{Style.BRIGHT}{var}{Style.NORMAL}", деление на ноль (i) я не проходил ƪ(˘⌣˘)ʃ')
                    else:
                        result['r'] = [given['V'] / given['i']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
                
            case 'x':
                if 'x' in given.keys():
                    result['x'] = [given['x']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data или деление на ноль')
            
            case 'y':
                if 'y' in given.keys():
                    result['y'] = [given['y']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data или деление на ноль')
            
            case 'N':
                if 'N' in given.keys():
                    result['N'] = [given['N']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data или деление на ноль или нет цветов')
            
            case _:
                print(Fore.YELLOW + f'WARN! Unknown variable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}.\nIf you meant something else, please restsrt the programm.')
                    
    # print(result)
    for var, res in result.items():
        print(f'{var} = {"; ".join(map(str, res))}')
    
    
def f13():
    if input('''Перед использованием советую прочитать инструкцию
0. -- Инструкция
не 0. Далее
--------------------------
Писать сюда -> ''') == '0':
        input('''\n\n\nПосле выбора типа задачи вам будет предложен список возможных значений.
Пример строчки такого списка: "i (Глубина кодирования) (только для дано) [ <b>, B, KB, MB, GB, TB ] = 1"

Первым идёт Обозначение перемнной, потом в скобках указано её название на человеческом языке.
Затем в ещё одних скобках может быть указано, что данную переменную можно использовать только в дано.

Потом у переменных, которые могут иметь различные еденицы измерения, перечислены эти самые единицы измерения,
и в <> находится то значение, которое будет использовано по умалчанию, если не указать иного.

Ну и у некоторых переменных, которые частенико не указывают в дано, потому что подразумевают некоторое базовое значение,
может быть указано значение, которое будет дано данной перемнной, если её не указать ни в Дано, ни в Найти

При вводе "Дано" надо учитывать 4 правила:
    1.  Данные значения перечисляются через ;
    2.  Каждое значение должно быть записано как Обозначение перемнной и её значение разделённые знаком =
    3.  К значению переменной можно дописать единицу измерения в которой она дана, записав через пробел.
    4.  Учитывайте регистр Обозначений перемнных

Пример строчки из дано (из решения задачи кодирования информации): "Дано -> I=6 B;K=3"

При вводе "Найти" надо учитывать 3 правила:
    1.  Переменные для нахождения перечисляются через пробел
    2.0 При желании можно указать конкретные единицы измерения для вывода
    2.1 Эти еденицы приписываются к Обозначению переменной через пробел и перечисляются через ,
    2.2 По умолчанию вывод будет во всех доступных единицах измерения.
    3.  Учитывайте регистр Обозначений перемнных

Email для связи - night_skumbry@outlook.com

Данная инстукция переделается в ближайшее дни, но по функционалу она актуальна
\n>>>''')

    match input('''\n\n\nВыберите тип задачи
--------------------------
1. Кодирование информации
2. Кодирование звука
3. Кодирование изображений
--------------------------
Писать сюда -> ''')[0]:
        case '1':
            information()
        case '2':
            sound()
        case '3':
            picture()
        case 'счастье':
            print('I can\'t help you, but you still can read the instruction. ☻')
        case _:
            print('You must stry again.')

if __name__ == '__main__':
    while True:
        f13()
        input('Нажмите Enter ')

