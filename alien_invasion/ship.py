import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    # 游戏形象的类
    def __init__(self,ai_game) -> None:
        # 初始化飞船的位置
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()
        # 加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/达达利亚.bmp')
        self.rect=self.image.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.center_ship()
        # self.rect.midbottom=self.screen_rect.midbottom
        # # ####前面是载入图片的位置，后方为需要对应的位置，可以直接输入数据
        # # self.rect.midbottom=(100,100)
        # self.x=float(self.rect.x)
        # self.y=float(self.rect.y)
        # 移动标志
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    def center_ship(self):
        # 初始化飞船位置
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
    def update(self):
        # 根据移动标志调整飞船位置
        if self.moving_right:
            # self.rect.x +=1
            self.x += self.settings.ship_speed
        if self.moving_left :
            # self.rect.x -=1
            self.x -= self.settings.ship_speed
        if self.moving_up:
            if self.rect.top>self.screen_rect.top:    
                self.y -= self.settings.ship_speed
            # self.y -= self.settings.ship_speed
        if self.moving_down:
            if self.rect.bottom<self.screen_rect.bottom:    
                self.y += self.settings.ship_speed
            # self.y += self.settings.ship_speed
        self.rect.x=self.x
        self.rect.y=self.y
        # 接下来是让角色可以不受限制的四面移动
        if self.rect.left<self.screen_rect.left:
            self.rect.right=self.screen_rect.right
            self.x=float(self.rect.x)
        elif self.rect.right>self.screen_rect.right:
            self.rect.left=self.screen_rect.left
            self.x=float(self.rect.x)
        # if self.rect.top<self.screen_rect.top:
        #     self.rect.bottom=self.screen_rect.bottom
        #     self.y=float(self.rect.y)
        # elif self.rect.bottom>self.screen_rect.bottom:
        #     self.rect.top=self.screen_rect.top
        #     self.y=float(self.rect.y)
    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)