from PIL import Image
from random import randint
from dataclasses import dataclass
import os
from moviepy.editor import ImageClip, concatenate_videoclips


@dataclass
class const:
    img_size: tuple[int] = (1000, 1000)
    ball_size: tuple[int] = (150, 150)
    bg_color: tuple[str] = ('#f3c7ba')
    frames: int = 200
    folder: str = './1'
    video_name: str = './1.mp4'


class Ball:
    def __init__(self, posx: int, posy: int) -> None:
        self.img = Image.open('./balln.png')
        self.posx, self.posy = posx, posy

        self.posx_r = self.posx + const.ball_size[0]

        self.posy_r = self.posy + const.ball_size[1]

        self.velx = randint(-250, 250)/50
        self.vely = randint(-250, 250)/50

    def get_pos(self) -> tuple[int]:
        return int(self.posx), int(self.posy)


    def run(self) -> None:
        self.add('x', self.velx)
        if self.posx_r >= const.img_size[0]:
            self.velx = -self.velx
            self.add('x', const.img_size[0] - self.posx_r)
        elif self.posx <= 0:
            self.velx = -self.velx
            self.add('x', 0 - self.posx)

        self.add('y', self.vely)
        if self.posy_r >= const.img_size[1]:
            self.vely = -self.vely
            self.add('y', const.img_size[1] - self.posy_r)
        elif self.posy <= 0:
            self.vely = -self.vely
            self.add('y', 0 - self.posy)

    def add(self, axis, vel) -> None:
        if axis == 'x':
            self.posx += vel
            self.posx_r += vel
        elif axis == 'y':
            self.posy += vel
            self.posy_r += vel


def create_photoes() -> None:
    im = Image.new('RGB', const.img_size, color=const.bg_color)
    ball = Ball(500, 500)
    if const.folder[2:].split('/')[-1] not in os.listdir(path=f"./{'/'.join(const.folder[2:].split('/')[:-1])}"):
        os.mkdir(f'./{const.folder}')
    for i in range(const.frames):
        back = im.copy()
        back.paste(ball.img, ball.get_pos())
        back.save(f'./{const.folder}/{i}.png')
        ball.run()
        if i % 100 == 0:
            print(f'frame - {i}')


def make_video():
    phts = [ImageClip(f'./{const.folder}/{m}.png') for m in range(const.frames)]
    clip = concatenate_videoclips(phts, method='compose')
    clip.write_videofile(const.video_name, fps=60)


def main() -> None:
    create_photoes()
    make_video()


if __name__ == '__main__':
    main()