import pygame

pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint!")

def draw_menu():
    pygame.draw.rect(screen, (10,120,150), [0,0,WIDTH,70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    xl_brush = pygame.draw.circle(surface=screen, color='black', center=[100,35], radius=25.6, width=4)





run = True
while run:
    timer.tick(fps)
    screen.fill('white')

    draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()