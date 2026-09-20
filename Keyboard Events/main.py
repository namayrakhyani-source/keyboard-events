import pygame

pygame.init()

WIDTH = 650
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Keyboard Events')

#loading rocket image
rocket_img = pygame.image.load('assets/rocket.png')

rocket_x = 325
rocket_y = 250

while True:
    screen.fill((180,200,65))

    #displaying rocket image
    screen.blit(rocket_img, (rocket_x, rocket_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        #checking if a key is pressed
        if event.type == pygame.KEYDOWN:
            #checking if left arrow key is being pressed
            if event.key == pygame.K_LEFT:
                if rocket_x > 0:
                    rocket_x = rocket_x - 15
            #checking if right arrow key is being pressed
            if event.key == pygame.K_RIGHT:
                if rocket_x < 600:
                    rocket_x = rocket_x +15
            #checking if up arrow key is being pressed
            if event.key == pygame.K_UP:
                if rocket_y > 0:
                    rocket_y = rocket_y - 15
            #checking if down arrow key is being pressed
            if event.key == pygame.K_DOWN:
                if rocket_y < 425:
                    rocket_y = rocket_y + 15

    pygame.display.update()

pygame.quit()