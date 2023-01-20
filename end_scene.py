import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Три шага к счастью")

clock = pygame.time.Clock()


def runi():
    a = 'blob1'
    im_1 = pygame.image.load('1конецсцена.png.')
    ru = True
    buton_pressed = False

    def draw_window():
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
                im_1 = pygame.image.load('2конецсцена.png')
                a = 'blob2'
                buton_pressed = False
            elif a == 'blob2':
                im_1 = pygame.image.load('3конецсцена.png.')
                a = 'blob3'
                buton_pressed = False
            elif a == 'blob3':
                im_1 = pygame.image.load('4конецсцена.png.')
                a = 'blob4'
                buton_pressed = False
            elif a == 'blob4':
                im_1 = pygame.image.load('5конецсцена.png.')
                a = 'blob5'
                buton_pressed = False
            elif a == 'blob5':
                im_1 = pygame.image.load('6конецсцена.png.')
                a = 'blob6'
                buton_pressed = False
            elif a == 'blob6':
                im_1 = pygame.image.load('7конецсцена.png.')
                a = 'blob7'
                buton_pressed = False
            elif a == 'blob7':
                im_1 = pygame.image.load('8конецсцена.png.')
                a = 'blob8'
                buton_pressed = False
            elif a == 'blob8':
                return False

        draw_window()
        pygame.display.flip()
    return True


if __name__ == '__main__':
    runi()
    pygame.quit()
