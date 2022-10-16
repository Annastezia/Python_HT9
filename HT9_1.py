#1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

import pygame
import sys

def win(places, sign):
    empty = 0
    for row in places:
        empty += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if places[0][col] == sign and places[1][col] == sign and places[2][col] == sign:
            return sign
    if places[0][0] == sign and places[1][1] == sign and places[2][2] == sign:
        return sign
    if places[0][2] == sign and places[1][1] == sign and places[2][0] == sign:
        return sign
    if empty == 0:
        return 'None'
    return False

pygame.init()
pygame.mixer.init()

FPS = 25
size_block = 100
margin = 10
width = height = size_block * 3 + margin * 4

size = (width, height)
screen = pygame.display.set_mode((size))
pygame.display.set_caption('Tic-tac-toe')
clock = pygame.time.Clock()

black = (0, 0, 0)
light_yellow = (255, 255, 224)
dark_violet = (148, 0, 211)
dark_green = (10, 153, 0)
medium_blue = (0, 0, 205)

places = [[0]*3 for i in range(3)]
change = 0
game_over = False

going = True
while going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if places[row][col] == 0:
                if change % 2 == 0:
                    places[row][col] = 'X'
                else:
                    places[row][col] = 'O'
                change += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            places = [[0] * 3 for i in range(3)]
            change = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if places[row][col] == 'X':
                    color = dark_violet
                elif places[row][col] == 'O':
                    color = dark_green
                else:
                    color = light_yellow
                x = col * size_block + (col + 1)*margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == dark_violet:
                    pygame.draw.line(screen, black, (x + 8, y + 8), (x + size_block - 8, y + size_block - 8), 7)
                    pygame.draw.line(screen, black, (x + size_block - 8, y + 8), (x + 8, y + size_block - 8), 7)
                elif color == dark_green:
                    pygame.draw.circle(screen, black, (x + size_block // 2, y + size_block // 2,), size_block // 2 - 8, 6)
    if (change - 1) % 2 == 0:
        game_over = win(places, 'X')
    else:
        game_over = win(places, 'O')

    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('Шрифт', 80)
        text1 = font.render(game_over, True, light_yellow)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, (text_x, text_y))
    pygame.display.update()