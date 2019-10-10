from 飞机大战.plane_sprites import *

pygame.init()
screen = pygame.display.set_mode((480, 700),  0, 0)  # 初始化游戏显示窗口,
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))   # 将图像绘制到指定屏幕位置
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 300))
pygame.display.update()  # 刷新屏幕显示
hero_rect = pygame.Rect(200, 300, 120, 125)  # 专门绘制矩形区域(x,y,width,height)
print("%d %d" % (hero_rect.x, hero_rect.y))
clock = pygame.time.Clock()
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
enemy_Group = pygame.sprite.Group(enemy, enemy1)
i = 0
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出")
            pygame.quit()
            exit()
    hero_rect.y -= 1
    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    enemy_Group.update()
    enemy_Group.draw(screen)

    pygame.display.update()
    i += 1
    print(i)

