import pygame
class Settings:
    # 《外星人大战》的设置
    def __init__(self) -> None:
        # 初始化游戏设置
        # 屏幕设置
        self.screen_width=900
        self.screen_height=600
        # 这两个值为不重要的设定值
        self.bg_color=(230,230,230)
        self.ship_limit=3
        self.ship_speed=1.5

        self.bullet_speed=5.0

        self.bullet_height=15
        self.bullet_color=(64,224,208)
        self.bullets_allowed=10
        self.bullet_update=2
        
        # self.alien_speed=1

        self.fleet_drop_time=10000
        self.fleet_direction=1

        #加快速度
        self.speedup_scale=1.1
        self.initialize_dynamic_settings()

        # 增加分值
        self.score_scale=1.5
    
    def initialize_dynamic_settings(self):
        # 使设置随游戏进行变化而变化
        self.bullet_width=2

        self.alien_speed=1.0
        # 计分
        self.alien_points = 50

        self.fleet_drop_speed=10
    def increase_speed(self):
        # 提高速度设置
        # self.ship_speed *=self.speedup_scale
        self.alien_speed *=self.speedup_scale
        self.fleet_drop_speed *=self.speedup_scale

        # 提升分值
        self.alien_points= int(self.alien_points * self.score_scale)
    def increase_bullet(self):
        if self.bullet_width<=300:
            self.bullet_width +=self.bullet_update
