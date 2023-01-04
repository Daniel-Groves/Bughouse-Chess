# echo-client.py
import pygame
import socket
import pickle

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

x=[]

global data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"dat1 {data}")
            recieved= pickle.loads(data)
            conn.sendall(data)



print(f"x{recieved}")


pygame.init()
screen = pygame.display.set_mode((1000, 800))
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
        
    def update(self,x,y):
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

ap = wp + bp

#data = pickle.loads(data)
#print(data)
            
for count,piece in enumerate(ap):
    piece.update(recieved[count][0],recieved[count][1])

while True:
    screen.fill(white)
    screen.blit(board_image, (200, 75))
    for i in ap:
        screen.blit(i.image, (i.placerx, i.placery))
    pygame.display.update()
        
                

    