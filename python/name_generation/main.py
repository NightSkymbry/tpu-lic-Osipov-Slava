from typing import Iterable, Any
import random
import time

vowels = 'аеёиоуыэюя'
double_vowels = 'еёяюи'
consonat = 'бвгджзйклмнпрстфхцчшщ'
pristavki = list(map(lambda x: x.capitalize(), 'гипо ано супер сверх купер убер квадра кристи квекто хладо кветта ронта хант соло зе алла пуга хазо зик кринже ке еже хроно ра ве за ли жи пе авто мудро дубо славо клее христо мусли кресто ари храмо дур яд яз астро паро водо огне эхо дву ед три шумо рас дис ир до ил ан книго солнце яро ветро аллахо'.split()))
otstavki = '_2007 _2006 _228 _229 _222 _2004 _X22X_ _2002 _224_ XXX _4444 _2222 _2929 _1000-7 _993 _DOTA2_ _МаМаЛавер_ _ПаПаЛавер_228 _Шлёпстер_ _DikiyTazik_ _ДизельныйМотор228 _Дизельный _Фруктовый _Вишнёвый _Сальный _Солевой _КрингеБунт_ _Заводной _ _Petr_IX _KiloEd _)I(upoed _KIlogramSoSiSok_ +Kipudon _5488_ _SuPeRlOx_ _аКаК_ _аКаК_КаКаТь _фрес_ _Х0Л0Д0К-2_ _СмЕрТнЫйЧеЛ_ _6ПчеловоД9 _Худ56 _Чел _Трамп _Морской _моНархисТ _легоКуБ _некСуС _кИсЕлЬ_ _м0т0р0лла38 _Gеп0рд45 _шшершшенЬ_ _ГеРаКаКаЛ_ _Диага-Нал_ _КринжМарин_ _02921 _1343 _1984 _637457 _5465 _1000-77  _1985 _1986 _547 _8354 _20785 _354 _1956 _1988 _1919 _6969 _667 _666 _321 _2345 _54637 _6473823 _2037 _2003 _2009 _2000 _2к91 _2081 _2099 _кий _кий _кий _кий _кий _кий _кий _кий _2080 _2026 _2029 _2054 _2012 _2020 _2054 _2077'.split()


def test_for(subject: any,  filter_: Iterable, ttype: int) -> tuple[bool, list[Any]]:
    """subject - Строка для проверки;
    filter_ - Фильтр по которому будет происходить проверка;
    ttype - Может принимать некоторые значения, соответствующие типу проверки
    1 - Если хоть 1 из subject содержится в filter_"""
    x = False
    r = []
    for i in filter_:
        match ttype:
            case 1:
                if i in subject:
                    x = True
                    r.append(i)
    return x, r


def split_by_syllable(string: str) -> list[str]:
    ans = []
    add = True
    for i, v in enumerate(string):
        v = v.lower()
        if not add:
            if v in double_vowels and string[i-1] in 'ьъй':
                ans.append(v)
            else:
                ans[-1] += v
                if test_for(ans[-1], vowels, 1)[0] and i+1 < len(string) and test_for(string[i+1:], vowels, 1)[0] and string[i+1] not in 'ьъ' and i+2 < len(string) and string[i+2] in vowels:
                    add = True
        else:
            ans.append(v)
            if test_for(ans[-1], vowels, 1)[0] and i+1 < len(string) and test_for(string[i+1:], vowels, 1)[0] and string[i+1] not in 'ьъ' and i+2 < len(string) and string[i+2] in vowels:
                add = True
            else:
                add = False
    return ans


def main():
    name = input('\n\nВведите ваше имя\n-> ')
    Name = split_by_syllable(name)
    for index, i in enumerate(Name):
        if test_for(i, consonat, 1)[0]:
            Name[index] = change_consonate(i)
    return ''.join(Name)


def change_consonate(slog: str):
    res = test_for(slog, consonat, 1)
    # print(res[1])
    for i in res[1]:
        if random.randint(0, 1):
            slog = slog.replace(i, random.choice(consonat))
    return slog


def ending(Names):
    shiiish = random.randint(0, 2)
    match shiiish:
        case 0:
            endingusus = str(random.randint(99, 999))
            Namesplus = Names + "_" + endingusus
        case 1:
            endingusus = str(random.randint(1, 9))
            Namesplus = Names + "_" + "200" + endingusus
        case 2:
            Namesplus = Names + random.choice(otstavki)
    return Namesplus


def oppening(Namesplus):

    Namespluss = random.choice(pristavki) + "_" + Namesplus
    return Namespluss


if __name__ == "__main__":
    if input('''Хотите узнать, кто работал над данной программой?
1 ---- Да
не 1 - Нет
-> ''').strip() == '1':
        input('''
Тимлид - Осипов Вячеслав
Программисты - Кукина Анна, Егоров Юрий
Особые благодарности - Иванов Николай, Балаганский Дмитрий, Козлова Карина

Далее ->>''')

    while True:
        Names = main()

        print(f'''
Итоговый никнэйм - "{oppening(ending(Names))}"
        ''')
        time.sleep(0.2)
        if input('''Хотите попробовать ещё?
1 ---- Нет
не 1 - Да
-> ''').strip() == '1':
            break
