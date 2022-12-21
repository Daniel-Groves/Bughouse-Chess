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

@pytest.mark.parametrize("wking,bking,wp, bp, expected_result, move", [
    (Piece(f"wk", 7, 8, "w", wking_image),
        Piece(f"bk", 7, 2, "w", bking_image),
        [Piece(f"wk", 7, 8, "w", wking_image),
         Piece(f"wb1", 3, 8, "w", wbishop_image),
         Piece(f"wn1", 2, 8, "w", wknight_image),
         Piece(f"wn2", 3, 1, "w", wknight_image),
         Piece(f"wr1", 1, 8, "w", wrook_image),
         Piece(f"wr2", 5, 8, "w", wrook_image),
         Piece(f"wp1", 1, 7, "w", wpawn_image),
         Piece(f"wp2", 2, 6, "w", wpawn_image),
         Piece(f"wp3", 3, 4, "w", wpawn_image),
         Piece(f"wp4", 4, 3, "w", wpawn_image),
         Piece(f"wp5", 6, 7, "w", wpawn_image),
         Piece(f"wp6", 7, 7, "w", wpawn_image),
         Piece(f"wp7", 8, 7, "w", wpawn_image)],
        [Piece(f"bk", 7, 2, "b", bking_image),
         Piece(f"bp1", 6, 2, "b", bpawn_image),
         Piece(f"bp2", 7, 3, "b", bpawn_image),
         Piece(f"bp3", 1, 3, "b", bpawn_image)],
        False,
        False),
    (Piece(f"wk", 8, 1, "w", wking_image), #TEST CASE 4
        Piece(f"bk", 6, 3, "b", bking_image),
        [Piece(f"wk", 8, 1, "w", wking_image),
         Piece(f"wp1", 8, 2, "w", wpawn_image),
        Piece(f"wp1", 7, 2, "w", wpawn_image)],
        [Piece(f"bk", 6, 3, "b", bking_image),
        Piece(f"bb1", 1, 8, "b", bbishop_image),
        Piece(f"bn1", 8, 3, "b", bknight_image)],
        False,
        True)

    ])


def test_check(wking,bking,wp,bp,expected_result,move):


    G = Game(wp, bp, move)


    for piece in G.ap:
        piece.place()
    print("".join([f"\n{i}" for i in board]))

    assert main.check_checker(G, G.wp, G.wp, wking, bking) is expected_result



    print("here")