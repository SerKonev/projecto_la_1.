import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Начало")

clock = pygame.time.Clock()


def runin():
    a = 'blob1'
    im_1 = pygame.image.load('1 кадр.png')
    ru = True
    buton_pressed = False

    def draw_windo():
        win.blit(im_1, (0, 0))
        pygame.display.update()

    while ru:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    buton_pressed = True

        if buton_pressed:
            if a == 'blob1':
                im_1 = pygame.image.load('1.5 кадр.png')
                a = 'blob2'
                buton_pressed = False
            elif a == 'blob2':
                im_1 = pygame.image.load('2 кадр.png')
                a = 'blob3'
                buton_pressed = False
            else:
                return False

        draw_windo()
        pygame.display.flip()
    return True


if __name__ == '__main__':
    runin()
    pygame.quit()
