import pygame
import os

from classes import *
from game import *

window = pygame.display.set_mode((800,600))

def draw_screen() -> None:
    img = pygame.image.load(os.path.join("Assets", 'chessboard.png')).convert()
    window.blit(img, (100, 0))
    for piece in board:
        if piece:
            window.blit(piece.img.convert_alpha(), (piece.square[0]*75+100, piece.square[1]*75))
    pygame.display.update()


run = True
starting_board = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
board = genBoardFromFEN(starting_board)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw_screen()
