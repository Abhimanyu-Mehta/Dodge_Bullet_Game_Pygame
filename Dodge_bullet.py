import pygame
import math
from pygame import mixer

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Dodge Bullet")

icon = pygame.image.load('guns_icon.png')
pygame.display.set_icon(icon)

background_load = pygame.image.load('fight_background.png')
background = pygame.transform.scale(background_load, (800, 600))

mixer.music.load('background.wav')
mixer.music.play(-1)

player1_gun_load = pygame.image.load('player1_rifle.png')
player1_gun = pygame.transform.rotate(player1_gun_load, 45)
player1_gunX = 336
player1_gunY = 480
player1_gunX_change = 0
player1_gunY_change = 0

player2_gun_load = pygame.image.load('player2_rifle.png')
player2_gun = pygame.transform.rotate(player2_gun_load, 225)
player2_gunX = 336
player2_gunY = 70
player2_gunX_change = 0
player2_gunY_change = 0


def print_player1_gun():
    screen.blit(player1_gun, (player1_gunX, player1_gunY))


def print_player2_gun():
    screen.blit(player2_gun, (player2_gunX, player2_gunY))


player1_bullet = pygame.image.load('bullet.png')
player1_bulletX = 0
player1_bulletY = 480
player1_bulletX_change = 0
player1_bulletY_change = -6
player1_bullet_state = "ready"

player2_bullet_load = pygame.image.load('bullet.png')
player2_bullet = pygame.transform.rotate(player2_bullet_load, 180)
player2_bulletX = 0
player2_bulletY = 70
player2_bulletX_change = 0
player2_bulletY_change = 6
player2_bullet_state = "ready"


def print_player1_bullet(x, y):
    global player1_bullet_state
    player1_bullet_state = "fire"
    screen.blit(player1_bullet, (x + 25, y + 10))


def print_player2_bullet(x, y):
    global player2_bullet_state
    player2_bullet_state = "fire"
    screen.blit(player2_bullet, (x + 25, y + 10))


def player2_cheak_collision(player2_gunX, player2_gunY, player1_bulletX, player1_bulletY):
    distance = math.sqrt((math.pow(player2_gunX - player1_bulletX, 2) + (math.pow(player2_gunY - player1_bulletY, 2))))
    if distance <= 27:
        return True
    else:
        return False


def player1_cheak_collision(player1_gunX, player1_gunY, player2_bulletX, player2_bulletY):
    distance = math.sqrt((math.pow(player1_gunX - player2_bulletX, 2) + (math.pow(player1_gunY - player2_bulletY, 2))))
    if distance <= 27:
        return True
    else:
        return False


you_won = pygame.font.Font('freesansbold.ttf', 64)
you_won_fontX = 190
you_won_fontY = 270
text = ""


def print_you_won():
    you_won_ = you_won.render(text, True, (0, 0, 0))
    screen.blit(you_won_, (you_won_fontX, you_won_fontY))


running = True

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player1_gunX_change = 3
            elif event.key == pygame.K_LEFT:
                player1_gunX_change = -3
            elif event.key == pygame.K_d:
                player2_gunX_change = 3
            elif event.key == pygame.K_a:
                player2_gunX_change = -3
            elif event.key == pygame.K_SPACE:
                if player1_bullet_state == "ready":
                    bullet_sound = mixer.Sound('shooting_sound.wav')
                    bullet_sound.play()
                    player1_bulletX = player1_gunX
                    print_player1_bullet(player1_bulletX, player1_bulletY)
            elif event.key == pygame.K_x:
                if player2_bullet_state == "ready":
                    bullet_sound = mixer.Sound('shooting_sound.wav')
                    bullet_sound.play()
                    player2_bulletX = player2_gunX
                    print_player2_bullet(player2_bulletX, player2_bulletY)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player1_gunX_change = 0
            elif event.key == pygame.K_LEFT:
                player1_gunX_change = 0
            elif event.key == pygame.K_d:
                player2_gunX_change = 0
            elif event.key == pygame.K_a:
                player2_gunX_change = 0

    if player1_bulletY <= 0:
        player1_bulletY = 490
        player1_bullet_state = "ready"

    elif player1_bullet_state is "fire":
        print_player1_bullet(player1_bulletX, player1_bulletY)
        player1_bulletY += player1_bulletY_change

    elif player2_bulletY >= 536:
        player2_bulletY = 70
        player2_bullet_state = "ready"

    elif player2_bullet_state is "fire":
        print_player2_bullet(player2_bulletX, player2_bulletY)
        player2_bulletY += player2_bulletY_change

    player2_collision = player2_cheak_collision(player2_gunX, player2_gunY, player1_bulletX, player1_bulletY)
    if player2_collision:
        text = "  wins"
        player2_bulletX = 1000
        player1_bulletX = 1000
        player1_bulletY = 1000
        player2_gunX = 1000
        player1_gunX = 150
        player1_gunY = 268

    player1_collision = player1_cheak_collision(player1_gunX, player1_gunY, player2_bulletX, player2_bulletY)
    if player1_collision:
        text = "  wins"
        player1_bulletX = 1000
        player2_bulletX = 1000
        player2_bulletY = 1000
        player1_gunX = 1000
        player2_gunX = 150
        player2_gunY = 268
        player2_gun = pygame.transform.rotate(player2_gun_load, 45)

    print_you_won()
    player1_gunX += player1_gunX_change
    player2_gunX += player2_gunX_change
    print_player1_gun()
    print_player2_gun()
    pygame.display.update()
