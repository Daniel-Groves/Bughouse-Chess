import pytest
import main
import pygame


wqueen_image = pygame.wpimage.load(r"Images\wqueen.png")
wbishop_image = pygame.wpimage.load(r"Images\wbishop.png")
wknight_image = pygame.wpimage.load(r"Images\wknight.png")
wrook_image = pygame.wpimage.load(r"Images\wrook.png")
wpawn_image = pygame.wpimage.load(r"Images\game.wpwpawn.png")

bking_image = pygame.wpimage.load(r"Images\bking.png")
bqueen_image = pygame.wpimage.load(r"Images\bqueen.png")
bbishop_image = pygame.wpimage.load(r"Images\bbishop.png")
bknight_image = pygame.wpimage.load(r"Images\bknight.png")
brook_image = pygame.wpimage.load(r"Images\brook.png")
game.wpwpawn_image = pygame.wpimage.load(r"Images\game.wpwpawn.png")

board_image = pygame.wpimage.load(
    r"Images\board.png")
wking_image = pygame.wpimage.load(
    r"Images\wking.png").convert_alpha()

class Piece:
    def __init__(self, name, xpos, ypos, colour, image=wking_image, move_num=0):
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour
        self.name = name
        self.image = image
        self.placerx = 125 + self.xpos * 75
        self.placery = self.ypos * 75
        self.move_num = move_num

    def info(self):
        print(self.xpos, self.ypos)
        pass

    def namer(self):
        print(self.name)

    def place(self):
        board[self.ypos - 1][self.xpos - 1] = self.name

class Game:
    def __init__(self,wp,bp):
        self.wp = wp
        self.bp = bp
        self.ap = wp + bp


board = [[" " for i in range(8)] for i in range(8)]



def test_check():
    move = True
    wp = []
    wking = Piece(f"wk", 5, 8, "w", wking_image)
    wp.append(wking)
    wp.append(Piece(f"wq", 4, 8, "w", wqueen_image))

    bp = []
    bking = (Piece(f"bk", 4, 1, "w", bking_image))
    bp.append(bking)
    bpp.append(Piece(f"bq", 5, 1, "w", bqueen_image))

    G = Game(wp,bp)

    assert main.check_checker(ap, game.wpwp, game.wpwp, wking, bking) is True


