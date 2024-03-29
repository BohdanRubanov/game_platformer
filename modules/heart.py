import pygame
import modules.settings as settings

pygame.init()

count_heart = 3
game_over = False

class Heart(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

heart = Heart(
    x= 0,
    y= 0,
    width=30,
    height=30,
    name_image= 'images/heart/1.png',
    color= (255,0,0)
)

def show_hearts(win):
    global game_over
    # global count_heart
    heart.X = 0
    for count in range(count_heart):
        heart.blit_sprite(win)
        heart.X += heart.WIDTH
    if count_heart <= 0:
        game_over = True
    