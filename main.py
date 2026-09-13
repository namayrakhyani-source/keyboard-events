import pygame

pygame.init()

WIDTH = 650
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Keyboard Events')

#loading rocket image
rocket_img = pygame.image.load('assets/rocket.jpg')

while True:
    screen.fill((180,200,65))

    #displaying rocket image
    screen.blit(rocket_img, (325, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    pygame.display.update()

pygame.quit()