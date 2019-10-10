import random
import pygame
SCREEN_RECT = pygame.Rect(0, 0, 400, 700)
TIME_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 发射子弹事件
HERO_FRIE_EVENT = pygame.USEREVENT + 1


# 定义精灵类
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super(GameSprite, self).__init__()  # 初始化父类方法
        self.image = pygame.image.load(image_name)  # 载入图片
        self.rect = self.image.get_rect()  # 获取图片的属性
        self.speed = speed

    def update(self):
        self.rect.y += self.speed  # 更新在垂直方向的位置


class Background(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:  # 判断是否移出屏幕
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    def __init__(self):
        super().__init__('./images/enemy1.png')
        # 敌机的初始速度
        self.speed = random.randint(1, 5)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类方法，保持垂直方向的飞行
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # print('飞出屏幕，需要从精灵组中删除')
            # kill方法可以将精灵从所有精灵组中删除
            self.kill()

    def __del__(self):
        # print('敌机飞出屏幕')
        pass


class Hero(GameSprite):
    def __init__(self):
        super().__init__('./images/me1.png', 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄在水平方向移动
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_LEFT]:
            self.rect.x += self.speed
        elif key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_UP]:
            super().update()
        # 控制英雄不能移除屏幕
        # print(SCREEN_RECT.height)
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        print('发射子弹')
        # for i in (0, 1, 2):
        #     bullet = Bullet()
        #     bullet.rect.bottom = self.rect.y - 20 * i
        #     bullet.rect.centerx = self.rect.centerx
        #     self.bullets.add(bullet)
        bullet = Bullet()
        bullet.rect.bottom = self.rect.y - 20
        bullet.rect.centerx = self.rect.centerx
        self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__('./images/bullet1.png', -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print('子弹被销毁')
