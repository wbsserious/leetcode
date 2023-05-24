import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # 管理子弹
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen= ai_game.screen
        self.settings= ai_game.settings
        self.color= ai_game.settings.bullet_color
        self.direction_up=False
        self.direction_down=False
        self.direction_left=False
        self.direction_right=False
        self.PlayerRect=ai_game.ship.rect

        # 在（0，0）处创建一个表示子弹的矩阵，再设置正确的位置
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.center=ai_game.ship.rect.center
        # 用小数表示子弹位置
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)
    def Bullet_LR(self):
        # 修改子弹方向
        self.rect=pygame.Rect(0,0,self.settings.bullet_height,self.settings.bullet_width)
        self.rect.center=self.PlayerRect.center
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)
    def update(self):
        # 子弹的移动方式
        if self.direction_up:
            self.y -=self.settings.bullet_speed
        if self.direction_down:
            self.y +=self.settings.bullet_speed
        if self.direction_left:
            self.x -=self.settings.bullet_speed
        if self.direction_right:
            self.x +=self.settings.bullet_speed

        self.rect.y=self.y
        self.rect.x=self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        
