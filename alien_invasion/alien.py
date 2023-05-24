import pygame
from pygame.sprite import Sprite
import random
class Aline(Sprite):
    # 敌人类型
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen= ai_game.screen
        # 引入敌人
        self.NumberRandom= random.randint(1,3)
        if self.NumberRandom==1:
            self.image = pygame.image.load("images/对外汉语.bmp")
        if self.NumberRandom==2:
            self.image = pygame.image.load("images/汉语国际教育.bmp")
        if self.NumberRandom==3:
            self.image = pygame.image.load("images/现代汉语.bmp")
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.setting=ai_game.settings
        self.screen_rect=self.screen.get_rect()
        self.TimeDrop=0

    def check_edges(self):
        #判断是否碰到了边缘

        if self.rect.right>=self.screen_rect.right or self.rect.left<=0: 
            return True
        
    def update_lr(self):
        #水平方向如何移动
        if self.NumberRandom==1:
            DistanceMove=random.uniform(-2,4)
        elif self.NumberRandom==2:
            DistanceMove=random.uniform(-4,2)
        elif self.NumberRandom==3:
            DistanceMove=random.uniform(-10,10)
        self.x+= self.setting.alien_speed*DistanceMove
        if self.rect.left<self.screen_rect.left:
            self.rect.right=self.screen_rect.right
            self.x=float(self.rect.x)
        elif self.rect.right>self.screen_rect.right:
            self.rect.left=self.screen_rect.left
            self.x=float(self.rect.x)
        self.rect.x=self.x
    def update_ud(self):
        # 上下移动
        if self.TimeDrop>=self.setting.fleet_drop_time:
            self.y+=self.setting.fleet_drop_speed
            self.rect.y=self.y
            self.TimeDrop=0
        else:
            self.TimeDrop+=random.randint(20,100)
    def update(self):
        # 敌人的移动
        self.update_lr()
        self.update_ud()

