from typing import Iterable


vowels = 'аеёиоуыэюя'
double_vowels = 'еёяюи'
consonat = 'бвгджзйклмнпрстфхцчшщъь'


def test_for(subject: any,  filter_: Iterable, ttype: int) -> bool:
    """subject - Строка для проверки;
    filter_ - Фильтр по которому будет происходить проверка;
    ttype - Может принимать некоторые значения, соответствующие типу проверки
    1 - Если хоть 1 из subject содержится в filter_"""
    for i in filter_:
        match ttype:
            case 1:
                if i in subject:
                    return True
    return False


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
                if test_for(ans[-1], vowels, 1) and i+1 < len(string) and test_for(string[i+1:], vowels, 1) and string[i+1] not in 'ьъ' and i+2 < len(string) and string[i+2] in vowels:
                    add = True
        else:
            ans.append(v)
            if test_for(ans[-1], vowels, 1) and i+1 < len(string) and test_for(string[i+1:], vowels, 1) and string[i+1] not in 'ьъ' and i+2 < len(string) and string[i+2] in vowels:
                add = True
            else:
                add = False
    return ans


def main():
    name = input('Введите ваше полное имя\n-> ')
    Name = split_by_syllable(name)
    print(Name)


if __name__ == "__main__":
    main()