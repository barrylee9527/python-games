from 飞机大战.plane_sprites import *


class PlaneGame(object):
    def __init__(self):
        # 游戏的初始化
        print("游戏场景初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)  # 初始化屏幕大小
        self.clock = pygame.time.Clock()  # 游戏时钟帧数检测
        self.__create__sprites()  # 创建精灵组
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)  # 设置时间间隔来出现敌机,毫秒为单位
        pygame.time.set_timer(HERO_FRIE_EVENT, 200)  # 设置发射子弹的时间间隔

    def __create__sprites(self):
        # 创建游戏精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄的精灵和精灵组
        self.hero = Hero()  # 定义英雄属性
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("开始游戏")
        while True:
            self.clock.tick(TIME_SEC)
            self.__event_hander()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_hander(self):
        # 时间监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FRIE_EVENT:
                self.hero.fire()
        key_pressed = pygame.key.get_pressed()  # 捕获键盘按键事件
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_DOWN]:
            self.hero.speed = 3
        elif key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_UP]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 碰撞检测
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 敌机撞毁英雄
        enemys = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemys) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        # 更新精灵和精灵组的位置
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        print('游戏结束')
        exit(0)


# 游戏运行
if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
