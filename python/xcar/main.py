import json
import time
from random import randint as rand


track_lenght = 100


class xcar:
    def __init__(self, prop_file_path: str):
        with open(prop_file_path, encoding='utf-8') as f:
            prop = json.loads(f.read())
            print(prop)
        self.speed_min, self.speed_max = map(float, prop['speed_range'].split())
        self.model = prop['simbol']
        self.pos = 0
    
    def run(self):
        self.pos += rand(int(self.speed_min*100), int(self.speed_max*100))/100


def run():
    game = True
    cars = [
        xcar('./xcar/first.json'),
        xcar('./xcar/second.json'),
        xcar('./xcar/third.json'),
        xcar('./xcar/fourth.json')
    ]
    while game:
        time.sleep(0.3)
        print('\n'*37)
        for car in cars:
            car.run()
            print(' ' * int(car.pos), car.model, ' ' * int(track_lenght-car.pos), '|' if car.pos < track_lenght else '', sep = '')

        if any([True if car.pos >= track_lenght else False for car in cars]):
            game = False

    winner = cars[0]
    for car in cars:
        if car.pos > winner.pos: winner = car

    print('Winner is', winner.model, '!')
    


if __name__ == '__main__':
    run()
