import pygame


pygame.init()
win = pygame.display.set_mode((800, 600)) # Задаём размеры окну нашей игры"
pygame.display.set_caption("Лабиринт") # Даём назнавие нашему окну"
player_stand = pygame.image.load('playe.png')
bg = pygame.image.load('bg2.png')


clock = pygame.time.Clock()

BLACK = (1, 1, 1)

speed = 1  # Скорость перемещения персонажа

a = 550
b = 450
d = []
c = []
for i in range(50):
    c.append(a)
    a += 1
    d.append(b)
    b += 1

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img='playe.png'):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = 0

        self.walls = None
        alive = True

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if pygame.sprite.spritecollide(self, self.walls, False):
            self.alive = False
        alive = True
        self.change_x = 0
        self.change_y = 0


class wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.x = y

def game_main():
    igra = True
    button_pressed = False
    game = True
    all_sprite_list = pygame.sprite.Group()
    wall_list = pygame.sprite.Group()
    wall_coords = [
        [0, 0, 10, 600],
        [790, 0, 10, 600],
        [790, 0, 800, 10],
    ]
    for i in wall_coords:
        Wall = wall(i[0], i[1], i[2], i[3])
        wall_list.add(Wall)
        all_sprite_list.add(Wall)

    player = Player(20, 20)
    player.walls = wall_list
    all_sprite_list.add(player)

    def draw_window():
        win.blit(bg, (0, 0))
        win.blit(player_stand, (player))  # Всегда отрисовываем персонажа, когда он перемещается

        pygame.display.update()

    while game:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   # 1 - означает левую кнопку мыши
                    x_new, y_new = event.pos    # Координаты точки, где находиться курсор
                    button_pressed = True   # Левая кнопка мыши нажата
                def cha(player):
                    if player.rect.x != x_new or player.rect.y != y_new:
                        '''Условие, если координата x игрока не равна координате x курсора 
                        или координата y игрока не равна координате y курсора'''
                        if player.rect.x != x_new and player.rect.y != y_new:
                            if player.rect.x > x_new and player.rect.y > y_new:
                                player.rect.x -= speed  # Перемещаем персонажа влево
                                player.rect.y -= speed  # И одновременно перемещаем его вверх
                            elif player.rect.x < x_new and player.rect.y < y_new:
                                player.rect.x += speed  # Перемещаем персонажа вправо
                                player.rect.y += speed  # И одновременно перемещаем его вниз
                            elif player.rect.x < x_new and player.rect.y > y_new:
                                player.rect.x += speed  # Перемещаем персонажа вправо
                                player.rect.y -= speed  # И одновременно перемещаем его вверх
                            elif player.rect.x > x_new and player.rect.y < y_new:
                                player.rect.x -= speed  # Перемещаем персонажа влево
                                player.rect.y += speed  # И одновременно перемещаем его вниз
                        elif player.rect.y != y_new:
                            if player.rect.y < y_new:
                                player.rect.y += speed  # Перемещаем персонажа вниз
                            elif player.rect.y > y_new:
                                player.rect.y -= speed  # Перемещаем персонажа вверх
                        elif player.rect.x != x_new:
                            if player.rect.x < x_new:
                                player.rect.x += speed  # Перемещаем персонажа вправо
                            elif player.rect.x > x_new:
                                player.rect.x -= speed  # Перемещаем персонажа влево

        if button_pressed:
            '''Если левая кнопка мыши нажата, то вызываем функцию и персонаж начинает перемещаться в точку,
            где находился курсор при нажатии'''
            cha(player)# Вызываем функциию игрока
            player.update()
            if not player.alive:
                player.rect.x = 20
                player.rect.y = 20
                player.alive = True
                x_new = 20
                y_new = 20
            if player.rect.y in c and player.rect.x in d:
                return False
        draw_window()   # Отрисовываем все наше окно игры

        all_sprite_list.draw(win)
        pygame.display.flip()
    return True


if __name__ == '__main__':
    game_main()
    pygame.quit()
