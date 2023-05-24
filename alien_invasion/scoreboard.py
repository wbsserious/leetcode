import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    def __init__(self,ai_game) -> None:

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect =self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分信息室使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        # 准备初始得分图像
        self.prep_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        rounded_score = round(self.stats.score,-1)
        score_str="{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str,True,self.text_color,self.settings.bg_color
        )

        # 划定得分矩形图案
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        # 将等级渲染出来
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str,True, self.text_color,self.settings.bg_color
        )

        # 确定位置

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom+10
    
    def prep_ships(self):
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x= 10 + ship_number * ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)
    
    def show_score(self):
        # 显示得分
        self.screen.blit( self.score_image,self.score_rect)
        self.screen.blit( self.level_image,self.level_rect)
        self.ships.draw(self.screen)


