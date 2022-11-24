import pytest
import main
import pygame


wqueen_image = pygame.image.load(r"Images\wqueen.png")
wbishop_image = pygame.image.load(r"Images\wbishop.png")
wknight_image = pygame.image.load(r"Images\wknight.png")
wrook_image = pygame.image.load(r"Images\wrook.png")
wpawn_image = pygame.image.load(r"Images\wpawn.png")

bking_image = pygame.image.load(r"Images\bking.png")
bqueen_image = pygame.image.load(r"Images\bqueen.png")
bbishop_image = pygame.image.load(r"Images\bbishop.png")
bknight_image = pygame.image.load(r"Images\bknight.png")
brook_image = pygame.image.load(r"Images\brook.png")
bpawn_image = pygame.image.load(r"Images\bpawn.png")

board_image = pygame.image.load(
    r"Images\board.png")
wking_image = pygame.image.load(
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
    def __init__(self,wp,bp, move):
        self.wp = wp
        self.bp = bp
        self.ap = wp + bp
        self.move = move


board = [[" " for i in range(8)] for i in range(8)]




def test_check():

    move = False
    wp = []

    wking = Piece(f"wk", 5, 8, "w", wking_image)
    wp.append(wking)
    wp.append(Piece(f"wq", 4, 8, "w", wqueen_image))
    wp.append(Piece(f"wb1", 3, 8, "w", wbishop_image))
    wp.append(Piece(f"wb2", 2, 4, "w", wbishop_image))
    wp.append(Piece(f"wn1", 2, 8, "w", wknight_image))
    wp.append(Piece(f"wn2", 6, 6, "w", wknight_image))
    wp.append(Piece(f"wr1", 1, 8, "w", wrook_image))
    wp.append(Piece(f"wr2", 8, 8, "w", wrook_image))

    bp = []

    bking = (Piece(f"bk", 5, 1, "w", bking_image))
    bp.append(bking)
    bp.append(Piece(f"bq", 4, 1, "w", bqueen_image))
    bp.append(Piece(f"bb1", 3, 1, "w", bbishop_image))
    bp.append(Piece(f"bb2", 6, 1, "w", bbishop_image))
    bp.append(Piece(f"bn1", 2, 1, "w", bknight_image))
    bp.append(Piece(f"bn2", 7, 1, "w", bknight_image))
    bp.append(Piece(f"br1", 1, 1, "w", brook_image))
    bp.append(Piece(f"br2", 8, 1, "w", brook_image))

    G = Game(wp,bp, move)


    for piece in G.ap:
        piece.place()
    print("".join([f"\n{i}" for i in board]))

    assert main.check_checker(G, G.wp, G.wp, wking, bking) is True

    print("here")
