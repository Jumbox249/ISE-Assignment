import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Super Kart")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255))  # Blue background

    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 100))

    pygame.draw.circle(screen, (0, 255, 0), (400, 300), 50)

    pygame.display.flip()

pygame.quit()
