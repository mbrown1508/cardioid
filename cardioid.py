import pygame
import math


WIDTH, HEIGHT = 800, 800
X_OFFSET, Y_OFFSET = WIDTH / 2, HEIGHT / 2

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cardioid")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)


def circle(pos, radius, color=WHITE):
    pygame.draw.circle(win, color, (int(pos[0]+X_OFFSET), int(pos[1]+Y_OFFSET)), int(radius), 1)


def line(pos1, pos2, color=WHITE):
    pygame.draw.line(win, color, (int(pos1[0]+X_OFFSET), int(pos1[1]+Y_OFFSET)), (int(pos2[0]+X_OFFSET), int(pos2[1]+Y_OFFSET)), 1)


total = 200
step = math.pi * 2 / total
factor = 1
offset = ()
r = WIDTH / 2.2


def get_vector(index):
    angle = (index * step) % total

    x = r * math.cos(angle)
    y = r * math.sin(angle)

    return x, y


run = True
clock = pygame.time.Clock()
while run:
    dt = clock.tick(60)
    factor += 0.01

    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        elif event.type == pygame.QUIT:
            run = False

    for i in range(total):
        a = i
        b = i * factor

        a_pos = get_vector(a)
        b_pos = get_vector(b)

        line(a_pos, b_pos)

    circle([0, 0], r)

    pygame.display.update()

pygame.quit()
