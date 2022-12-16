from typing import Any


class Team:
    def __init__(self, team: str, oponents: list[str], results_good: list[int], results_bad: list[int], order: list[int]):
        if not (len(oponents) == len(results_good) == len(results_bad) == len(order)):
            raise ValueError(f'diferent amount of oponents and games in team {team}')
        self.team: str = team
        self.games: dict[str, dict[str, Any]] = {
            o: {
                'goals': g,
                'falls': f,
                'result': 'win' if g > f else 'lose' if g < f else 'draw'
            }
            for o, g, f in zip(oponents, results_good, results_bad)
        }
        self.games_order: dict[int, str] = {
            g: o for g, o in zip(order, oponents)
        }
        self.goals_total: int = sum(results_good)
        self.falls_total: int = sum(results_bad)
        self.wins_total: int = sum([1 if g > f else 0 for g, f in zip(results_good, results_bad)])
        self.loses_total: int = sum([1 if g < f else 0 for g, f in zip(results_good, results_bad)])
        self.drawes_total: int = sum([1 if g == f else 0 for g, f in zip(results_good, results_bad)])
        self.points: int = self.wins_total * 3 + self.drawes_total

    def __str__(self):
        res = f'{self.team}'
        res += f'\nГолы - {self.goals_total}\nПропущено - {self.falls_total}'
        # for o, r in self.games.items():
        #     res += f'\n - {o} ( {r[0]} : {r[1]} )'

        return res

    def _deb(self) -> str:
        return f'{self.team=}\n{self.goals_total=}\n{self.falls_total=}\n{self.wins_total=}\n\
    {self.loses_total=}\n{self.drawes_total=}\n{self.points=}\n{self.games=}'


def setup_group(group: list[list[str | int]], order: list[list[int]]) -> list[Team]:
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

        teams.append(Team(team, ops, resg, resb, order[index]))

    return teams


def setup_groups():
    groupA = [['Нидерланды', '', 2, 1, 2], ['Сенегал', 0, '', 2, 3], ['Эквадор', 1, 1, '', 2], ['Катар', 0, 1, 0, '']]
    groupB = [['Англия', '', 0, 6, 3], ['США', 0, '', 1, 1], ['Иран', 2, 0, '', 2], ['Уэльс', 0, 1, 0, '']]
    groupC = [['Аргентина', '', 2, 2, 1], ['Польша', 0, '', 0, 2], ['Мексика', 0, 0, '', 2], ['Саудовская Аравия', 2, 0, 1, '']]
    groupD = [['Франция', '', 4, 0, 2], ['Австрия', 1, '', 1, 1], ['Тунис', 1, 0, '', 0], ['Дания', 1, 0, 0, '']]
    groupE = [['Япония', '', 2, 2, 0], ['Испания', 1, '', 1, 7], ['Германия', 1, 1, '', 4], ['Коста-Рика', 1, 0, 2, '']]
    groupF = [['Марокко', '', 0, 2, 2], ['Хорватия', 0, '', 0, 4], ['Бельгия', 0, 0, '', 1], ['Канада', 1, 1, 0, '']]
    groupG = [['Бразилия', '', 1, 0, 2], ['Швейцария', 0, '', 1, 3], ['Камерун', 1, 0, '', 3], ['Сербия', 0, 2, 3, '']]
    groupH = [['Португалия', '', 1, 2, 3], ['Южная Корея', 2, '', 0, 2], ['Уругвай', 0, 0, '', 2], ['Гана', 2, 3, 0, '']]

    gs: dict[str, list[Team]] = {
        'Группа A': setup_group(groupA, [[1, 2, 3], [1, 3, 2], [2, 3, 1], [3, 2, 1]]),
        'Группа B': setup_group(groupB, [[2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2]]),
        'Группа C': setup_group(groupC, [[3, 2, 1], [3, 1, 2], [2, 1, 3], [1, 2, 3]]),
        'Группа D': setup_group(groupD, [[1, 3, 2], [1, 2, 3], [3, 2, 1], [2, 3, 1]]),
        'Группа E': setup_group(groupE, [[3, 1, 2], [3, 2, 1], [1, 2, 3], [2, 1, 3]]),
        'Группа F': setup_group(groupF, [[1, 2, 3], [1, 3, 2], [2, 3, 1], [3, 2, 1]]),
        'Группа G': setup_group(groupG, [[2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2]]),
        'Группа H': setup_group(groupH, [[3, 2, 1], [3, 1, 2], [2, 1, 3], [1, 2, 3]])
    }

    return gs
