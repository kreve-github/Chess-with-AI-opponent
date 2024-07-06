import pygame
import os

imgs = {
    "WHITE": {
        "Rook": pygame.image.load(os.path.join("Assets", 'W_Rook.png')),
        "Knight": pygame.image.load(os.path.join("Assets", 'W_Knight.png')),
        "Bishop": pygame.image.load(os.path.join("Assets", 'W_Bishop.png')),
        "Queen": pygame.image.load(os.path.join("Assets", 'W_Queen.png')),
        "King": pygame.image.load(os.path.join("Assets", 'W_King.png')),
        "Pawn": pygame.image.load(os.path.join("Assets", 'W_Pawn.png')),
    },
    "BLACK": {
        "Rook": pygame.image.load(os.path.join("Assets", 'B_Rook.png')),
        "Knight": pygame.image.load(os.path.join("Assets", 'B_Knight.png')),
        "Bishop": pygame.image.load(os.path.join("Assets", 'B_Bishop.png')),
        "Queen": pygame.image.load(os.path.join("Assets", 'B_Queen.png')),
        "King": pygame.image.load(os.path.join("Assets", 'B_King.png')),
        "Pawn": pygame.image.load(os.path.join("Assets", 'B_Pawn.png')),
    }
}

class Piece:
    def __init__(self, color, type, row, file) -> None:
        self.color = color
        self.type = type
        self.img = imgs[color][type]
        self.square = [file, row]

    def __str__(self) -> str:
        return self.type

    def move(self, where):
        self.square = where

