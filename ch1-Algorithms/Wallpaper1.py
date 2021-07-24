import pygame
from random import randint

corna = int(input("corna"))
cornb = int(input("cornb"))
side = int(input("side"))

pygame.init()


width = 400
height = 400
pygame.display.set_caption("Wallpaper 1")
screen = pygame.display.set_mode((width, height))

square = pygame.Surface((1, 1))


for i in range(0, 400):
    for j in range(0, 400):
        x = corna + i * side / 100
        y = cornb + j * side / 100
        c = int(x * x + y * y)
        loc = pygame.Rect((j+1), (i+1), 1, 1)

        if c % 3 == 0:
            square.fill((0, 0, 255))
        elif c % 3 == 1:
            square.fill((255, 0, 0))
        else:
            square.fill((255, 255, 0))
        screen.blit(square, loc)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False