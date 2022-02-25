import pygame

# import pygame_menu


pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
white = (255, 255, 255)
myfont = pygame.font.SysFont("Comic Sans MS", 30)
image_constant = (75, 75)
board_image = pygame.image.load(
    r"C:\Users\dangro0809\OneDrive - Highgate School\Highgate school\Year 12\Computer Science\Images\board.png")
wking_image = pygame.image.load(
    r"C:\Users\dangro0809\OneDrive - Highgate School\Highgate school\Year 12\Computer Science\Images\wking.png").convert_alpha()
wqueen_image = pygame.image.load(r"C:\Users\dangro0809\OneDrive - Highgate School\Highgate school\Year 12\Computer Science\Images\wqueen.png")
bking_image = pygame.image.load(r"C:\Users\dangro0809\OneDrive - Highgate School\Highgate school\Year 12\Computer Science\Images\bking.png")
wpawn_image = pygame.image.load(r"C:\Users\dangro0809\OneDrive - Highgate School\Highgate school\Year 12\Computer Science\Images\wpawn.png")
wking_image = pygame.transform.scale(wking_image, image_constant)
bking_image = pygame.transform.scale(bking_image, image_constant)
wqueen_image = pygame.transform.scale(wqueen_image, image_constant)
wpawn_image = pygame.transform.scale(wpawn_image, image_constant)

board = [[" " for i in range(8)] for i in range(8)]
print("".join([f"\n{i}" for i in board]))


# def start_game():
# menu.add.text_input(board)


def piecethere(xsquare, ysquare):
    for i in ap:
        if i.xpos == xsquare and i.ypos == ysquare and i != item:
            print(i.name,i.xpos,i.ypos)
            return True

    return False


def kingmoves(x, y):
    if x < abs(2) and y < abs(2):
        returner = True
    else:
        returner = False
    return returner

def queenmoves(x, y, startx, starty):
    returner = True
    print(x,y)
    if abs(x) == abs(y) or x == 0 or y == 0:
        if abs(x) == abs(y):
            for i in range(1, abs(x)):
                print(i)
                print("i am here")
                if x <0:
                    vectorx = startx - i
                elif x > 0:
                    vectorx = startx + i
                if y <0:
                    vectory = starty - i
                elif y > 0:
                    vectory = starty + i    
                if piecethere(vectorx, vectory):
                    returner = False
                    break
                else:
                    returner = True
        elif y == 0:
            for i in range(1, x):
                if piecethere(startx + i, starty):
                    returner = False
                    break
                else:
                    returner = True
        elif x == 0:
            for i in range(1, y):
                if piecethere(startx, starty + i):
                    returner = False
                    break
                else:
                    returner = True
    else:
        returner = False
    return returner


class Piece:
    def __init__(self, name, xpos, ypos, colour, image=wking_image):
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour
        self.name = name
        self.image = image
        self.placerx = 125 + self.xpos * 75
        self.placery = self.ypos * 75

    def info(self):
        print(self.xpos, self.ypos)
        pass

    def namer(self):
        print(self.name)

    def place(self):
        board[self.ypos - 1][self.xpos - 1] = self.name


wp = []
for i in range(1, 9):
    wp.append(Piece((f"wp{i}"), i, 7, "w", wpawn_image))
wp.append(Piece((f"wk"), 4, 8, "w"))
wp.append(Piece((f"wq"), 5, 8, "w", wqueen_image))
wp.append(Piece((f"wb1"), 3, 8, "w"))
wp.append(Piece((f"wb2"), 6, 8, "w"))
wp.append(Piece((f"wn1"), 2, 8, "w"))
wp.append(Piece((f"wn2"), 7, 8, "w"))
wp.append(Piece((f"wr1"), 1, 8, "w"))
wp.append(Piece((f"wr2"), 8, 8, "w"))
for i in wp:
    (i.info())
    i.place()

print("".join([f"\n{i}" for i in board]))

bp = []
for i in range(1, 9):
    bp.append(Piece((f"bp{i}"), i, 2, "b"))
bp.append(Piece((f"bk"), 5, 1, "w", bking_image))
bp.append(Piece((f"bq"), 4, 1, "w"))
bp.append(Piece((f"bb1"), 3, 1, "w"))
bp.append(Piece((f"bb2"), 6, 1, "w"))
bp.append(Piece((f"bn1"), 2, 1, "w"))
bp.append(Piece((f"bn2"), 7, 1, "w"))
bp.append(Piece((f"br1"), 1, 1, "w"))
bp.append(Piece((f"br2"), 8, 1, "w"))

for i in bp:
    (i.info())
    i.place()
ap = wp + bp
for i in ap:
    i.namer()
print("".join([f"\n{i}" for i in board]))

pygame.init()
surface = pygame.display.set_mode((1000, 800))


def snapper(x, y):
    snapposx, snapposy = 0, 0
    for i in range(1, 9):
        if x > 200 + (i - 1) * 75 and x < 200 + i * 75:
            snapposx = i
            break
    for i in range(1, 9):
        if y > 75 + (i - 1) * 75 and y < 75 + i * 75:
            snapposy = i
            break
    return snapposx, snapposy


# menu = pygame_menu.Menu("CHESS", 1000, 600, theme=pygame_menu.themes.THEME_GREEN)
# menu.add.button("START", start_game)
# menu.mainloop(surface)
run = True
while run:
    clock.tick(120)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for count, value in enumerate(board):
        thing = myfont.render((" ".join(value)), True, (0, 0, 0))
        screen.blit(thing, (250, 100 + (30 * count)))
        screen.blit(board_image, (200, 75))
    for i in ap:
        screen.blit(i.image, (i.placerx, i.placery))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            for i in range(1, 9):
                if x > 200 + (i - 1) * 75 and x < 200 + i * 75:
                    newposx = i
                    break
            for i in range(1, 9):
                if y > 75 + (i - 1) * 75 and y < 75 + i * 75:
                    newposy = i
                    break
            for i in ap:
                if i.xpos == newposx and i.ypos == newposy:
                    i.placerx = x
                    i.placery = y
                    item = i
        if pygame.mouse.get_pressed()[0] and item:
            x, y = pygame.mouse.get_pos()
            item.placerx = x - 75 / 2
            item.placery = y - 75 / 2
        if not pygame.mouse.get_pressed()[0]:

            try:
                x, y = pygame.mouse.get_pos()
                xsquare, ysquare = snapper(x, y)
                item.placerx = 125 + xsquare * 75
                item.placery = ysquare * 75
                for i in ap:
                    if i.xpos == xsquare and i.ypos == ysquare and i != item and i.name[0]!=item.name[0]:
                        ap.remove(i)
                item.xpos = xsquare
                item.ypos = ysquare
                if xsquare == 0 or ysquare == 0:
                    item.placerx = 125 + newposx * 75
                    item.xpos = newposx
                    item.placery = newposy * 75
                    item.ypos = newposy
                displacex = abs(newposx - xsquare)
                displacey = abs(newposy - ysquare)
                print(item.name)
                movevalid = True
                if item.name[1] == "k":
                    movevalid = kingmoves(displacex, displacey)
                elif item.name[1] == "q":
                    print("AAAA")
                    movevalid = queenmoves(newposx - xsquare,newposy - ysquare, xsquare, ysquare)
                    print(movevalid)
                else:
                    movevalid = True

                if not movevalid:
                    item.placerx = 125 + newposx * 75
                    item.xpos = newposx
                    item.placery = newposy * 75
                    item.ypos = newposy
                print(item.xpos,item.ypos)


            except AttributeError:
                pass
            except NameError:
                pass
            item = None

    pygame.display.update()
