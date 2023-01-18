# client1.py
import pygame
import socket
import pickle

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('CLIENT 2')
clock = pygame.time.Clock()

image_constant = (75, 75)
white = (255, 255, 255)
king_vectors = [(0, 1), (1, 1), (1, 0), (-1, 1), (0, -1), (-1, -1), (-1, 0), (1, -1)]
move = True  # move being true means white to move
board_image = pygame.image.load(
    r"Images\board.png")
wking_image = pygame.image.load(
    r"Images\wking.png").convert_alpha()
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

wking_image = pygame.transform.scale(wking_image, image_constant)
wqueen_image = pygame.transform.scale(wqueen_image, image_constant)
wbishop_image = pygame.transform.scale(wbishop_image, image_constant)
wknight_image = pygame.transform.scale(wknight_image, image_constant)
wrook_image = pygame.transform.scale(wrook_image, image_constant)
wpawn_image = pygame.transform.scale(wpawn_image, image_constant)

bking_image = pygame.transform.scale(bking_image, image_constant)
bqueen_image = pygame.transform.scale(bqueen_image, image_constant)
bbishop_image = pygame.transform.scale(bbishop_image, image_constant)
bknight_image = pygame.transform.scale(bknight_image, image_constant)
brook_image = pygame.transform.scale(brook_image, image_constant)
bpawn_image = pygame.transform.scale(bpawn_image, image_constant)


def snapper(x, y):
    snapposx, snapposy = 0, 0
    for i in range(1, 9):
        if 200 + (i - 1) * 75 < x < 200 + i * 75:
            snapposx = i
            break
    for i in range(1, 9):
        if 75 + (i - 1) * 75 < y < 75 + i * 75:
            snapposy = i
            break
    return snapposx, snapposy


class Game:
    def __init__(self, wp, bp, move, wking, bking, checking_pieces=[]):
        self.wp = wp
        self.bp = bp
        self.ap = wp + bp
        self.move = move
        self.wking = wking
        self.bking = bking
        self.checking_pieces = checking_pieces


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

    def update(self, x, y):
        self.xpos = x
        self.ypos = y
        self.placerx = 125 + self.xpos * 75
        self.placery = self.ypos * 75


wp = []
for i in range(1, 9):
    wp.append(Piece(f"wp{i}", i, 7, "w", wpawn_image))
wking = Piece(f"wk", 5, 8, "w", wking_image)
wp.append(wking)
wp.append(Piece(f"wq", 4, 8, "w", wqueen_image))
wp.append(Piece(f"wb1", 3, 8, "w", wbishop_image))
wp.append(Piece(f"wb2", 6, 8, "w", wbishop_image))
wp.append(Piece(f"wn1", 2, 8, "w", wknight_image))
wp.append(Piece(f"wn2", 7, 8, "w", wknight_image))
wp.append(Piece(f"wr1", 1, 8, "w", wrook_image))
wp.append(Piece(f"wr2", 8, 8, "w", wrook_image))

board = [[" " for i in range(8)] for i in range(8)]
print("".join([f"\n{i}" for i in board]))

bp = []
for i in range(1, 9):
    bp.append(Piece(f"bp{i}", i, 2, "b", bpawn_image))
bking = (Piece(f"bk", 5, 1, "w", bking_image))
bp.append(bking)
bp.append(Piece(f"bq", 4, 1, "w", bqueen_image))
bp.append(Piece(f"bb1", 3, 1, "w", bbishop_image))
bp.append(Piece(f"bb2", 6, 1, "w", bbishop_image))
bp.append(Piece(f"bn1", 2, 1, "w", bknight_image))
bp.append(Piece(f"bn2", 7, 1, "w", bknight_image))
bp.append(Piece(f"br1", 1, 1, "w", brook_image))
bp.append(Piece(f"br2", 8, 1, "w", brook_image))

G = Game(wp, bp, True, wking, bking)

clock.tick(120)
screen.fill(white)
# print(check_checker(wp, bp, wking, bking))


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

client_socket.send("client2".encode())

while True:
    clock.tick(120)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(board_image, (200, 75))
    for i in G.ap:
        screen.blit(i.image, (9*75 - i.placerx + 250, 9*75 - i.placery))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            for j in range(1, 9):
                if 200 + (j - 1) * 75 < x < 200 + j * 75:
                    newposx = j
                    break
            for j in range(1, 9):
                if 75 + (j - 1) * 75 < y < 75 + j * 75:
                    newposy = j
                    break
            for i in G.ap:
                if i.xpos == 9-newposx and i.ypos == 9-newposy:
                    i.placerx = x
                    i.placery = y
                    item = i
        if pygame.mouse.get_pressed()[0] and item:
            x, y = pygame.mouse.get_pos()
            item.placerx = 9*75 - (x - 75 / 2) + 250
            item.placery = 9*75 - (y - 75 / 2)
        if not pygame.mouse.get_pressed()[0]:

            try:
                x, y = pygame.mouse.get_pos()
                xsquare, ysquare = snapper(x,
                                           y)  # xsquare and ysquare are the squares the piece is trying to be placed on
                item.placerx = 125 + (9-xsquare) * 75
                item.placery = (9-ysquare) * 75
                movevalid = True
                tempx = item.xpos
                tempy = item.ypos
                item.xpos = xsquare
                item.ypos = ysquare
                for i in G.ap:
                    if i.xpos == xsquare and i.ypos == 9 - ysquare and i.name[0] != item.name[0]:
                        G.ap.remove(i)
                        takenpiece = i
                        if i.name[0] == "w":
                            G.wp.remove(i)
                        else:
                            G.bp.remove(i)
                        tempitem = i


                if G.move == False:
                    print("sending")
                    print(xsquare, ysquare)
                    print(9 - xsquare,9 - ysquare)
                    data = pickle.dumps([item.name, 9 - xsquare, 9 - ysquare])
                    while True:
                        try:
                            client_socket.sendall(data)
                            break
                        except OSError:
                            pass
                    client_socket.settimeout(100000)
                    result = pickle.loads(client_socket.recv(1024))
                else:
                    result = False
                if result:
                    tempitem = None
                if not result:
                    item.placerx = 125 + tempx * 75
                    item.xpos = tempx
                    item.placery = tempy * 75
                    item.ypos = tempy
                    if tempitem:
                        G.ap.append(tempitem)
                        if tempitem.name[0] == "w":
                            G.wp.append(tempitem)
                        else:
                            G.bp.append(tempitem)
                if result:
                    G.move = not G.move
            except AttributeError:
                pass
            except NameError:
                pass
            item = None

            client_socket.settimeout(0.0000001)  # Set a short timeout
            try:
                result = pickle.loads(client_socket.recv(1024))
                print(f"result {result}")
                G.move = not G.move
                for i in G.ap:
                    if i.name[:2] == "bn":
                        print(f" knight {i.name, i.xpos,i.ypos}")
                    if (9-i.xpos) == result[1] and (9-i.ypos) == result[2]:
                        G.ap.remove(i)
                        if i.name[0] == "w":
                            G.wp.remove(i)
                        else:
                            G.bp.remove(i)
                    if i.name == result[0]:
                        i.xpos, i.ypos = result[1],result[2]
                        i.placerx = 125 + result[1] * 75
                        i.placery = result[2] * 75
            except socket.timeout:
                # No result was received within the timeout
                continue




    pygame.display.update()

# data = pickle.loads(data)
# print(data)

# for count,piece in enumerate(ap):
# piece.update(recieved[count][0],recieved[count][1])

# while True:
# screen.fill(white)
# screen.blit(board_image, (200, 75))
# for i in ap:
#      screen.blit(i.image, (i.placerx, i.placery))
#  pygame.display.update()




