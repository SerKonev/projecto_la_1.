import pygame
import pygame.freetype

def maini():
    pygame.init()
    out = ''
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.freetype.SysFont(None, 34)
    font.origin = True
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:   # 1 - означает левую кнопку мыши
                    print(out)
        screen.fill(pygame.Color('grey12'))
        ticks = pygame.time.get_ticks()
        millis = ticks % 1000
        seconds = int(ticks/1000 % 60)
        minutes = int(ticks/60000 % 24)
        out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        font.render_to(screen, (100, 100), out, pygame.Color('dodgerblue'))
        pygame.display.flip()
        clock.tick(60)



if __name__ == '__main__':
    maini()
