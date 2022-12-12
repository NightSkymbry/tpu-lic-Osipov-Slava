groupA = [['Нидерланды', '', 2, 1, 2], ['Сенегал', 0, '', 2, 3], ['Эквадор', 1, 1, '', 2], ['Катар', 0, 1, 0, '']]
groupB = [['Англия', '', 0, 6, 3], ['США', 0, '', 1, 1], ['Иран', 2, 0, '', 2], ['Уэльс', 0, 1, 0, '']]
groupC = [['Аргентина', '', 2, 2, 1], ['Польша', 0, '', 0, 2], ['Мексика', 0, 0, '', 2], ['Саудовская Аравия', 2, 0, 1, '']]
groupD = [['Франция', '', 4, 0, 2], ['Австрия', 1, '', 1, 1], ['Тунис', 1, 0, '', 0], ['Дания', 1, 0, 0, '']]
groupE = [['Япония', '', 2, 2, 0], ['Испания', 1, '', 1, 7], ['Германия', 1, 1, '', 4], ['Коста-Рика', 1, 0, 2, '']]
groupF = [['Марокко', '', 0, 2, 2], ['Хорватия', 0, '', 0, 4], ['Бельгия', 0, 0, '', 1], ['Канада', 1, 1, 0, '']]
groupG = [['Бразилия', '', 1, 0, 2], ['Швейцария', 0, '', 1, 3], ['Камерун', 1, 0, '', 3], ['Сербия', 0, 2, 3, '']]
groupH = [['Португалия', '', 1, 2, 3], ['Южная Корея', 2, '', 0, 2], ['Уругвай', 0, 0, '', 2], ['Гана', 2, 3, 0, '']]


class Team:
    def __init__(self, team: str, oponents: list[str], results_good: list[int], results_bad: list[int]) -> None:
        if not (len(oponents) == len(results_good) == len(results_bad)):
            raise ValueError(f'diferent amount of oponents and games in team {team}')
        self.team = team
        self.games = {oponents[i]: [results_good[i], results_bad[i]] for i in range(len(oponents))} # {oponent: [goals, falls]}
        self.all_goals = sum(results_good)
        self.all_falls = sum(results_bad)

    def __str__(self):
        res = f'{self.team}'
        res += f'\nГолы - {self.all_goals}\nПропущено - {self.all_falls}'
        # for o, r in self.games.items():
        #     res += f'\n - {o} ( {r[0]} : {r[1]} )'

        return res


def setup_group(group: list[list[str | int]]) -> list[Team]:

    teams: list[Team] = list()

    for index, results in enumerate(group):
        ops: list[str] = []
        resg: list[int] = []
        resb: list[int] = []
        team = results[0]
        results = results[1:]
        for opponent, play in enumerate(results):
            if type(play) is int:
                ops.append(group[opponent][0])
                resg.append(play)
                resb.append(group[opponent][1 + index])

        teams.append(Team(team, ops, resg, resb))

    return teams


def main():
    teams = setup_group(groupA) + setup_group(groupB) + setup_group(groupC) + setup_group(groupD) + setup_group(groupE) + setup_group(groupF) + setup_group(groupG) + setup_group(groupH)

    for i in teams:
        print(i)


if __name__ == '__main__':
    main()
