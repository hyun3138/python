import pygame
import random
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("QUIZ")

background = pygame.image.load("C:\\Users\\lee\\OneDrive\\바탕 화면\\pythonworkspace\\pygame_basic\\paper.png")


chacter = pygame.image.load("C:\\Users\\lee\\OneDrive\\바탕 화면\\pythonworkspace\\pygame_basic\\dog.png")
chacter_size = chacter.get_rect().size
chacter_width = chacter_size[0]
chacter_height = chacter_size[1]
chacter_x_pos = (screen_width / 2) - (chacter_width / 2)
chacter_y_pos = screen_height - chacter_height

to_x = 0
chacter_speed = 0.6

enemy = pygame.image.load("C:\\Users\\lee\\OneDrive\\바탕 화면\\pythonworkspace\\pygame_basic\\ddong.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= chacter_speed
            elif event.key == pygame.K_RIGHT:
                to_x += chacter_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    chacter_x_pos += to_x * dt

    if chacter_x_pos < 0:
        chacter_x_pos = 0
    elif chacter_x_pos > screen_width - chacter_width:
        chacter_x_pos = screen_width - chacter_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    chacter_rect = chacter.get_rect()
    chacter_rect.left = chacter_x_pos
    chacter_rect.top = chacter_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if chacter_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
    
    screen.blit(background, (0, 0))
    screen.blit(chacter, (chacter_x_pos, chacter_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()

pygame.quit()