import sys
import pygame
import numpy as np

background_color = (255, 255, 255)
color_line = (0, 0, 0)
(width, height) = (600, 600)


def outfit():
    icon = pygame.image.load("pics\\tic-tac-toe.png")
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tic Tac Toe')
    pygame.display.set_icon(icon)
    screen.fill(background_color)
    pygame.display.flip()
    return screen


def draw_board(screen):
    pygame.draw.line(screen, color_line, (200, 0), (200, 600), 10)
    pygame.draw.line(screen, color_line, (400, 0), (400, 600), 10)
    pygame.draw.line(screen, color_line, (0, 200), (600, 200), 10)
    pygame.draw.line(screen, color_line, (0, 400), (600, 400), 10)
    pygame.display.update()


def check_draw(screen, board, marker, x, y, npx, npy, turn):
    if turn == 0:
        board[npx][npy] = 1
    elif turn == 1:
        board[npx][npy] = -1
    checking(board)
    screen.blit(marker, (x, y))
    pygame.display.update()


def checking(board):
    np_list = [[0, 0], [0, 1], [0, 2],
               [1, 0], [1, 1], [1, 2],
               [2, 0], [2, 1], [2, 2]]

    x0y0 = board[np_list[0][0]][np_list[0][1]]
    x0y1 = board[np_list[1][0]][np_list[1][1]]
    x0y2 = board[np_list[2][0]][np_list[2][1]]
    x1y0 = board[np_list[3][0]][np_list[3][1]]
    x1y1 = board[np_list[4][0]][np_list[4][1]]
    x1y2 = board[np_list[5][0]][np_list[5][1]]
    x2y0 = board[np_list[6][0]][np_list[6][1]]
    x2y1 = board[np_list[7][0]][np_list[7][1]]
    x2y2 = board[np_list[8][0]][np_list[8][1]]

    if x0y0 == x0y1 == x0y2 == 1 or \
        x1y0 == x1y1 == x1y2 == 1 or \
        x2y0 == x2y1 == x2y2 == 1 or \
        x0y0 == x1y0 == x2y0 == 1 or \
        x0y1 == x1y1 == x2y1 == 1 or \
        x0y2 == x1y2 == x2y2 == 1 or \
        x0y0 == x1y1 == x2y2 == 1 or \
        x2y0 == x1y1 == x0y2 == 1:
            print("Crossing win")
            sys.exit()

    if x0y0 == x0y1 == x0y2 == -1 or \
        x1y0 == x1y1 == x1y2 == -1 or \
        x2y0 == x2y1 == x2y2 == -1 or \
        x0y0 == x1y0 == x2y0 == -1 or \
        x0y1 == x1y1 == x2y1 == -1 or \
        x0y2 == x1y2 == x2y2 == -1 or \
        x0y0 == x1y1 == x2y2 == -1 or \
        x2y0 == x1y1 == x0y2 == -1:
            print("Circling win")
            sys.exit()


def marking(screen, pos_x, pos_y, marker, board, turn):
    if pos_x <= 200:
        if pos_y <= 200:
            check_draw(screen, board, marker, 36, 36, 0, 0, turn)
        elif 200 < pos_y <= 400:
            check_draw(screen, board, marker, 36, 236, 1, 0, turn)
        elif 400 < pos_y <= 600:
            check_draw(screen, board, marker, 36, 436, 2, 0, turn)
    elif 200 < pos_x <= 400:
        if pos_y <= 200:
            check_draw(screen, board, marker, 236, 36, 0, 1, turn)
        elif 200 < pos_y <= 400:
            check_draw(screen, board, marker, 236, 236, 1, 1, turn)
        elif 400 < pos_y <= 600:
            check_draw(screen, board, marker, 236, 436, 2, 1, turn)
    elif 400 < pos_x <= 600:
        if pos_y <= 200:
            check_draw(screen, board, marker, 436, 36, 0, 2, turn)
        elif 200 < pos_y <= 400:
            check_draw(screen, board, marker, 436, 236, 1, 2, turn)
        elif 400 < pos_y <= 600:
            check_draw(screen, board, marker, 436, 436, 2, 2, turn)


def main():
    screen = outfit()
    clock = pygame.time.Clock()
    draw_board(screen)

    cross  = pygame.image.load('pics\close.png')
    circle = pygame.image.load('pics\circle.png')

    digital_board = np.zeros((3, 3))

    gaming = True
    num_of_player = 2
    player_turn_count = 0
    while gaming:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]
                current_player_turn = player_turn_count % num_of_player
                if current_player_turn == 0:
                    marking(screen, pos_x, pos_y, cross, digital_board, current_player_turn)
                if current_player_turn == 1:
                    marking(screen, pos_x, pos_y, circle, digital_board, current_player_turn)
                player_turn_count += 1

        clock.tick(60)


if __name__ == "__main__":
    main()
