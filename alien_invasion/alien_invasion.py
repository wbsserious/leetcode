import sys
import pygame
from random import randint
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Aline
from game_stats import GameStates
from button import Button
from scoreboard import Scoreboard


class ALinenInvasion:
    # "管理游戏资源和行为的类"
    def __init__(self) -> None:
        pygame.init()
        self.settings=Settings()
    # 初始化背景设置
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        # self.background_image=pygame.image.load("images/yuanshen2.jpg")
        # self.background_image = pygame.transform.scale(self.background_image, (900, 600))
        # self.screen.blit(self.background_image, (0, 0))
    # 调用该函数创造显示窗口
        pygame.display.set_caption("题海大冒险")#窗口名字
        # 设置背景颜色
        # self.bg_color=(230,230,230)
        self.ship=Ship(self)
        # 存储子弹编组
        self.bullets=pygame.sprite.Group()
        self.aliens= pygame.sprite.Group()
        # 记录游戏统计信息
        self.stats=GameStates(self)
        # 创建记分牌
        self.sb=Scoreboard(self)
        # 创造敌人
        self._creat_feet()
        # 按钮出现
        self.play_button =Button(self,"Play")
    def _creat_feet(self):
        # 创建外星人群
        randint_number=randint(20,50)
        # 随机数量的外星人
        for i in range(randint_number):
            self._creat_alien()
            # 在这里可以选着敌人的类型
    def _creat_alien(self):
        # 创造一个外星人
        alien=Aline(self)
        alien.x=randint(0,1280)
        alien.y=randint(-500,50)
        alien.rect.x=alien.x
        alien.rect.y=alien.y
        self.aliens.add(alien)
    
    def _check_bullet_alien_collisions(self):
        # 判断是否消灭
        collisions=pygame.sprite.groupcollide(\
        self.bullets,self.aliens,True,True)
        if collisions:
            self.settings.increase_bullet()
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points*len(aliens)
            self.sb.prep_score()
        if not self.aliens:
            # 清空后生成新的外星人
            self.bullets.empty()
            self._creat_feet()
            self.settings.increase_speed()

            # 等级变化
            self.stats.level +=1
            self.sb.prep_level()
    
    def _check_aliens_bottom(self):
        # 判断敌人是否已经落地
        screen_rect= self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=screen_rect.bottom:

                self._shep_hit()
                break


    def _fire_bullet(self,event):
        # 生成子弹,判断方向并记录
        if len(self.bullets)<self.settings.bullets_allowed:
            
            new_bullet=Bullet(self)
            if event.key==pygame.K_UP:
                new_bullet.direction_up=True
            if event.key==pygame.K_DOWN:
                new_bullet.direction_down=True
            if event.key==pygame.K_LEFT:
                new_bullet.direction_left=True
                new_bullet.Bullet_LR()
            if event.key==pygame.K_RIGHT:
                new_bullet.direction_right=True
                new_bullet.Bullet_LR()
            self.bullets.add(new_bullet)    

    def _update_bullets(self):
        # 更新子弹状态
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0 or bullet.rect.top>=self.settings.screen_height\
                or bullet.rect.x> self.settings.screen_width\
                    or bullet.rect.right<0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()


    def _check_keydown_events(self,event):
        if event.key==pygame.K_d:
            # 向右移动飞船
            # self.ship.rect.x+=1
            self.ship.moving_right=True
        elif event.key==pygame.K_a:
            # 向左移动飞船
            # self.ship.rect.x+=1
            self.ship.moving_left=True
        elif event.key==pygame.K_w:
            # 向上移动飞船
            # self.ship.rect.x+=1
            self.ship.moving_up=True
        elif event.key==pygame.K_s:
            # 向上移动飞船
            # self.ship.rect.x+=1
            self.ship.moving_down=True
        elif event.key==pygame.K_l:
            sys.exit()
        elif event.key==pygame.K_UP or event.key==pygame.K_DOWN or \
            event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
            
            self._fire_bullet(event)

        
    def _check_keyup_events(self,event):
        # 松开按键
        if event.key==pygame.K_d:
            self.ship.moving_right=False
        if event.key==pygame.K_a:
            self.ship.moving_left=False
        if event.key==pygame.K_w:
            self.ship.moving_up=False
        if event.key==pygame.K_s:
            self.ship.moving_down=False

    def _check_play_button(self,mouse_pos):
        # 在单机 paly 按钮时开始新游戏
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:
            
            self.settings.initialize_dynamic_settings()#重置游戏基础设置
            self.stats.reset_stats()#重置血条
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # 清空敌人和子弹。
            self.aliens.empty()
            self.bullets.empty()

            # 创建新敌人
            self._creat_feet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

    def _check_events(self):
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
               
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:

                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _update_screen(self):
            # 每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)   
            # self.screen.blit(self.background_image, (0, 0))###可以讲指定图片作为背景
            self.ship.blitme()   #绘制飞船
            for bullet in self.bullets.sprites():#绘制子弹
                bullet.draw_bullet()   
            self.aliens.draw(self.screen)#绘制敌人
            # 显示得分
            self.sb.show_score()

            if not self.stats.game_active:
                self.play_button.draw_button()
            # 让最近的绘制的屏幕可见
            pygame.display.flip()
    def _shep_hit(self):
        # 碰撞发生时
        # 飞船数量减少
        if self.stats.ships_left>0:#判断还有没有生命值
            self.stats.ships_left -=1
            self.sb.prep_ships()
            # 清空子弹和敌人
            self.aliens.empty()#清空敌人
            self.bullets.empty()
            # 创建新的敌人，飞船复位
            self._creat_feet()
            self.ship.center_ship()

            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active=False
            pygame.mouse.set_visible(True)



    def _update_aliens(self):
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._shep_hit()
        self._check_aliens_bottom()

    def run_game(self):
        # 开始游戏的循环
        while True:
            # 监视键盘和鼠标事件
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()
            # 运用一个函数将功能独立出去
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                # self.bullets.update()
                # for bullet in self.bullets.copy():
                #     if bullet.rect.bottom<=0:
                #         self.bullets.remove(bullet)
                # print(len(self.bullets))
                # # 每次循环时都重绘屏幕
                # self.screen.fill(self.settings.bg_color)   
                # self.ship.blitme()     
                # # 让最近的绘制的屏幕可见
                # pygame.display.flip()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
if __name__=="__main__":
    # 创建游戏实力并运行游戏。
    ai=ALinenInvasion()
    ai.run_game()