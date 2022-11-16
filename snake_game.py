import pygame
pygame.init()


dis=pygame.display.set_mode((500,500))
pygame.display.update()
pygame.display.set_caption("Eugene's Snake Game")

# Set Colors
blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)

# Snake starting point
x1 = 250
y1 = 250

x1_change=0
y1_change=0

clock = pygame.time.Clock()

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
  
    x1 += x1_change
    y1 += y1_change
    dis.fill(black)

    pygame.draw.rect(dis,white,[x1,y1,10,10])
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()