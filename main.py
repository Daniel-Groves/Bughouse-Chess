import pygame
import time
#
# import pygame_menu
    # TODO: -Checking checking, -checkmate, en passant, castling, promotion, sounds
    # TODO: -checkmate
    # TODO: -en passant
    # TODO: -castling
    # TODO: - promotion
    # TODO: - sounds


pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
white = (255, 255, 255)
image_constant = (75, 75)
move = True   #move being true means white to move
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

board = [[" " for i in range(8)] for i in range(8)]
#print("".join([f"\n{i}" for i in board]))


# def start_game():
# menu.add.text_input(board)

def move_valid(item,xsquare,ysquare,wp,bp,wking,bking,newposx,newposy):
    if item.name[1] == "k":
        movevalid = king_moves(xsquare - item.xpos, ysquare - item.ypos, item) and not check_checker(wp, bp, wking,bking)
    elif item.name[1] == "q":
        print("AAAA")
        movevalid = queen_moves(-(newposx - xsquare), ysquare - newposy, newposx, newposy, item) and not check_checker(wp, bp, wking, bking)
        print(movevalid)
    elif item.name[1] == "b":
        movevalid = bishop_moves(-(newposx - xsquare), ysquare - newposy, newposx, newposy, item) and not check_checker(wp, bp, wking, bking)
    elif item.name[1] == "n":
        movevalid = knight_moves(-(newposx - xsquare), ysquare - newposy, newposx, newposy, item) and not check_checker(wp, bp, wking, bking)
    elif item.name[1] == "r":
        movevalid = rook_moves(-(newposx - xsquare), ysquare - newposy, newposx, newposy, item) and not check_checker(wp, bp, wking, bking)
    elif item.name[0:2] == "wp":
        print("got to wp")
        movevalid = white_pawn_moves(-(newposx - xsquare), ysquare - newposy, newposx, newposy, item.move_num, item,takenpiece) and not check_checker(wp, bp, wking, bking)
        if movevalid:
            item.move_num += 1
            tempitem = None
            print("movevalid")
    elif item.name[0:2] == "bp":
        print(f"check {check_checker(wp, bp, wking, bking)}")
        x = item
        movevalid = black_pawn_moves(-(newposx - xsquare), ysquare - newposy, newposx, newposy, item.move_num, item,takenpiece) and not check_checker(wp, bp, wking, bking)
        item = x
        print(f"check {check_checker(wp, bp, wking, bking)}")
        print(movevalid)
        print(item.name)
        if movevalid:
            item.move_num += 1
            tempitem = None
    else:
        movevalid = True
    return movevalid


def checkmate_checker(wp, bp, wking, bking, checking_pieces):
    checkmate = True
    print("checkmate checker")
    for i in checking_pieces:
        print(i.name)
    if move:
        pieces = bp
        king = wking
        print("TRUE")
    else:
        pieces = wp
        king = bking
        print(type(checking_pieces))
    for checker in checking_pieces:
        print("got here")
        if checker.name == "b":
            for i in range(0,wking.xpos-checker.xpos):
                for piece in pieces:
                    if move_valid(piece, checker.xpos+i, checker.ypos+i,wp,bp,wking,bking,piece.xpos,piece.ypos) and not check_checker(wp, bp, wking, bking):
                        checkmate = False
        elif checker.name[1] == "r":
            if checker.xpos - king.xpos == 0:
                for i in range(0,wking.ypos-checker.ypos):
                    for piece in pieces:
                        if move_valid(piece,checker.xpos, checker.ypos+i,wp,bp,wking,bking,piece.xpos,piece.ypos) and not check_checker(wp,bp,wking,bking):
                            checkmate = False
            if checker.ypos - king.ypos == 0:
                for i in range(0,wking.xpos-checker.xpos):
                    for piece in pieces:
                        if move_valid(piece,checker.xpos+i, checker.ypos,wp,bp,wking,bking,piece.xpos,piece.ypos) and not check_checker(wp,bp,wking,bking):
                            checkmate = False
            pass
        elif checker.name[1] == "q":
            pass
        checking_pieces = None
    return checkmate



def check_checker(wp, bp, wking, bking):
    global checking_pieces
    checking_pieces = []
    print("check checking")
    print(f"move {move}")
    print(f"turn {turn}")
    if move:
        pieces = bp
        king = wking
        print("TRUE")
    else:
        pieces = wp
        king = bking
    global piece
    for piece in pieces:
        if piece.name[1] == "k":
            checktake = False
        elif piece.name[1] == "q":
            print("checking AAAA")
            print(piece.name)
            print(king.xpos, king.ypos)
            print((piece.xpos - king.xpos), piece.ypos - king.ypos)
            print(f"AAAAAAAAA {piece.name}")
            checktake = queen_moves(king.xpos - piece.xpos, king.ypos - piece.ypos, piece.xpos, piece.ypos, piece)
            print(f"valid? {checktake}")
            if checktake:
                checking_pieces.append(piece)
                print("this is good")
                return checktake
        elif piece.name[1] == "b":
            print("checking bishop")
            if piece.name == "wb2":
                print(king.xpos - piece.xpos, king.ypos - piece.ypos, king.xpos, king.ypos, piece.name)
                print(f"bishop move yeah{bishop_moves(king.xpos - piece.xpos, king.ypos - piece.ypos, piece.xpos, piece.ypos, piece)}")
            checktake = bishop_moves(king.xpos - piece.xpos, king.ypos - piece.ypos, piece.xpos, piece.ypos, piece)
            if checktake:
                checking_pieces.append(piece)
                print("checktake")
                return checktake
        elif piece.name[1] == "n":
            checktake = knight_moves(piece.xpos - king.xpos, piece.ypos - king.ypos, king.xpos, king.ypos, piece)
            if checktake:
                checking_pieces.append(piece)
                return checktake
        elif piece.name[1] == "r":
            checktake = rook_moves(piece.xpos - king.xpos, piece.ypos - king.ypos, king.xpos, king.ypos, piece)
            if checktake:
                checking_pieces.append(piece)
                return checktake
        elif piece.name[0:2] == "wp":
            checktake = white_pawn_moves(piece.xpos - king.xpos, piece.ypos - king.ypos, king.xpos, king.ypos, piece.move_num, piece,takenpiece)
            if checktake:
                checking_pieces.append(piece)
                return checktake
        elif piece.name[0:2] == "bp":
            checktake = black_pawn_moves(piece.xpos - king.xpos, piece.ypos - king.ypos, king.xpos, king.ypos, piece.move_num, piece, takenpiece)
            if checktake:
                checking_pieces.append(piece)
                return checktake
        else:
            return False



def piecethere(xsquare, ysquare, compare):
    print("I AM HERE")
    print(xsquare,ysquare)
    for i in ap:
        if i.xpos == xsquare and i.ypos == ysquare and i!=compare:
            print(f"squares {xsquare, ysquare}")
            print(compare.name)
            print(i.name,i.xpos,i.ypos)
            return True

    return False

def piecethereexclude(xsquare, ysquare, compare):

    for i in ap:
        if i.xpos == xsquare and i.ypos == ysquare and i.name[0]!=compare.name[0]:
            print(compare.name)
            print(i.name,i.xpos,i.ypos)
            return True
    print("i shall return false")
    return False

def takenpiecechecker(takenpiece, xsquare, ysquare, compare):
    print(xsquare, ysquare, compare.name)
    print(takenpiece.name, takenpiece.xpos, takenpiece.ypos)
    if takenpiece.xpos == xsquare and takenpiece.ypos == ysquare and takenpiece.name != compare.name:
        print("TRUEUEE")
        return True
    else:
        print("FALSE")
        takenpiece = None
        return False

def king_moves(x, y, item):
    #print(f"asdasd {item.xpos, item.ypos}")
    #print(x,y)
    if abs(x) < 2 and abs(y) < 2 and not piecethere(item.xpos+x,item.ypos+y,item):
        #print("why am i here")
        returner = True
    else:
        returner = False
        #print("am i here")
    return returner

def queen_moves(x, y, startx, starty, queen):
    print(f"ASHDASKDKJASDKJASDK {queen.name}")
    returner = True
    print(f"vactors {x,y}")
    print(startx,starty)
    if abs(x) == abs(y) or x == 0 or y == 0:
        if abs(x) == abs(y):
            for i in range(0, abs(x)+1):
                print(queen.name)
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
                print(f"FFFF {vectorx, vectory}")
                if abs(x) == i:
                    print("passed first")
                if abs(x) == i and piecethereexclude(vectorx,vectory,queen):
                    print("yooooo")
                    return True
                elif piecethere(vectorx, vectory, queen):
                    print("we aer her")
                    returner = False
                    print(f"here {returner}")
                    return returner
                else:
                    returner = True
        elif y == 0:
            for i in range(1, abs(x)+1):
                #print(f"look {i}")
                if x > 0:
                    vectorx = startx + i
                if x < 0:
                    vectorx = startx - i
                if abs(x) == i and piecethereexclude(vectorx,starty, queen):
                    return True
                elif piecethere(vectorx, starty, queen):
                    returner = False
                    break
                else:
                    returner = True
        elif x == 0:

            for i in range(1, abs(y)+1):
                if y > 0:
                    vectory = starty + i
                if y < 1:
                    vectory = starty - i
                if abs(y) == i and piecethereexclude(startx,vectory, queen):
                    return True
                elif piecethere(startx, vectory, queen):
                    returner = False
                    break
                else:
                    returner = True
    else:
        returner = False
    return returner

def bishop_moves(x, y, startx, starty, bishop):
    if abs(x) == abs(y):
        for i in range(0, abs(x) + 1):
            # print(i)
            # print("i am here")
            if x < 0:
                vectorx = startx - i
            elif x > 0:
                vectorx = startx + i
            if y < 0:
                vectory = starty - i
            elif y > 0:
                vectory = starty + i

            if abs(x) == i and piecethereexclude(vectorx, vectory, bishop):
                return True
            elif piecethere(vectorx, vectory, bishop):
                returner = False
                return returner
            else:
                returner = True
    else:
        returner = False
    return returner

def knight_moves(x, y, startx, starty, knight):
    print(x,y)
    print(startx, starty)
    if (abs(x) == 1 and abs(y) == 2) or (abs(x) == 2 and abs(y) == 1):
        print("got here")
        if piecethereexclude(startx + x, starty + y, knight) or not piecethere(startx + x, starty + y, knight):
            return True
    else:
        return False

def rook_moves(x, y, startx, starty, rook):
    if x == 0 or y == 0:
        if y == 0:
            for i in range(1, abs(x)+1):
                #print(f"look {i}")
                if x > 0:
                    vectorx = startx + i
                if x < 0:
                    vectorx = startx - i
                if abs(x) == i and piecethereexclude(vectorx,starty, rook):
                    return True
                elif piecethere(vectorx, starty, rook):
                    returner = False
                    break
                else:
                    returner = True
        elif x == 0:

            for i in range(1, abs(y)+1):
                if y > 0:
                    vectory = starty + i
                if y < 1:
                    vectory = starty - i
                if abs(y) == i and piecethereexclude(startx,vectory, rook):
                    return True
                elif piecethere(startx, vectory, rook):
                    returner = False
                    break
                else:
                    returner = True
    else:
        returner = False
    return returner

def white_pawn_moves(x, y, startx, starty, first, wpa, takenpiece):
    if x == 0 and y == -1 and not piecethere(startx, starty - 1, wpa):
        return True
    elif abs(x)==1 and y == -1 and takenpiecechecker(takenpiece,startx + x, starty - 1, wpa):
        return True
    elif x == 0 and y == -2 and not piecethere(startx + x, starty - 1, wpa) and first == 0:
        return True
    else:
        return False

def black_pawn_moves(x, y, startx, starty, first, bpa, takenpiece):
    if x == 0 and y == 1 and not piecethere(startx, starty + 1, bpa):
        return True
    elif abs(x)==1 and y == 1 and takenpiecechecker(takenpiece, startx + x, starty + 1, bpa):
        return True
    elif x == 0 and y == 2 and not piecethere(startx + x, starty + 1, bpa) and first == 0:
        return True
    else:
        return False

class Piece:
    def __init__(self, name, xpos, ypos, colour, image=wking_image, move_num = 0):
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




wp = []
for i in range(1, 9):
    wp.append(Piece((f"wp{i}"), i, 7, "w", wpawn_image))
wking = Piece((f"wk"), 5, 8, "w", wking_image)
wp.append(wking)
wp.append(Piece((f"wq"), 4, 8, "w", wqueen_image))
wp.append(Piece((f"wb1"), 3, 8, "w", wbishop_image))
wp.append(Piece((f"wb2"), 6, 8, "w", wbishop_image))
wp.append(Piece((f"wn1"), 2, 8, "w", wknight_image))
wp.append(Piece((f"wn2"), 7, 8, "w", wknight_image))
wp.append(Piece((f"wr1"), 1, 8, "w", wrook_image))
wp.append(Piece((f"wr2"), 8, 8, "w", wrook_image))
for i in wp:
    print(i)

print("".join([f"\n{i}" for i in board]))

bp = []
for i in range(1, 9):
    bp.append(Piece((f"bp{i}"), i, 2, "b", bpawn_image))
bking = (Piece((f"bk"), 5, 1, "w", bking_image))
bp.append(bking)
bp.append(Piece((f"bq"), 4, 1, "w", bqueen_image))
bp.append(Piece((f"bb1"), 3, 1, "w", bbishop_image))
bp.append(Piece((f"bb2"), 6, 1, "w", bbishop_image))
bp.append(Piece((f"bn1"), 2, 1, "w", bknight_image))
bp.append(Piece((f"bn2"), 7, 1, "w", bknight_image))
bp.append(Piece((f"br1"), 1, 1, "w", brook_image))
bp.append(Piece((f"br2"), 8, 1, "w", brook_image))

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
takenpiece = None
while run:
    turn = True
    clock.tick(120)
    screen.fill(white)
    if check_checker(wp, bp, wking, bking):
        print("early")
        print(checking_pieces)
        if checkmate_checker(wp, bp,wking,bking,checking_pieces):
            print("CHECKMATE")
            time.sleep(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for count, value in enumerate(board):
        #thing = myfont.render((" ".join(value)), True, (0, 0, 0))
        #screen.blit(thing, (250, 100 + (30 * count)))
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
                xsquare, ysquare = snapper(x, y) #xsquare and ysquare are the squares the piece is trying to be placed on
                item.placerx = 125 + xsquare * 75
                item.placery = ysquare * 75
                #if xsquare == 0 or ysquare == 0:
                    #item.placerx = 125 + newposx * 75
                    #item.xpos = newposx
                    #item.placery = newposy * 75
                    #item.ypos = newposy
                displacex = abs(newposx - xsquare)  #displacex and displacey represent absolute vector
                displacey = abs(newposy - ysquare)
                print(item.name)
                movevalid = True
                tempx = item.xpos
                tempy = item.ypos
                item.xpos = xsquare
                item.ypos = ysquare
                for i in ap:
                    print("testing")
                    if i.xpos == xsquare and i.ypos == ysquare and i.name[0] != item.name[0]:
                        ap.remove(i)
                        print("removed")
                        takenpiece= i
                        print(takenpiece.name)
                        if i.name[0] == "w":
                            wp.remove(i)
                        else:
                            bp.remove(i)
                        tempitem = i
                print("hello", item.name[0])
                if item.name[0] == "w" and move == True:
                    turn = True
                elif item.name[0] == "b" and move == False:
                    turn = True
                else:
                    turn = False
                print(move)
                print(turn)

                movevalid = move_valid(item, xsquare, ysquare, wp, bp, wking, bking, newposx, newposy)

                if movevalid:
                    tempitem = None
                print(f"{movevalid} move valid")
                if not movevalid or not turn:
                    print("HOLA")
                    print(tempx,tempy)
                    print(item.name)
                    item.placerx = 125 + tempx * 75
                    item.xpos = tempx
                    item.placery = tempy * 75
                    item.ypos = tempy
                    if tempitem:
                        print("WHYYWYEHA")
                        ap.append(tempitem)
                        if tempitem.name[0] == "w":
                            wp.append(tempitem)
                        else:
                            bp.append(tempitem)
                print(item.xpos,item.ypos)
                #for i in wp:
                    #print(i.name,i.xpos,i.ypos)
                if movevalid and turn:
                    print("NICE")
                    move = not move
                    print("hello am here")
                    print(xsquare,ysquare)
                    for i in ap:
                        if i.xpos == xsquare and i.ypos == ysquare and i.name[0]!=item.name[0]:
                            print(f"am also here {i.name}")
                            ap.remove(i)
                            if i.name[0]=="w":
                                wp.remove(i)
                            else:
                                bp.remove(i)
                    #item.xpos = tempx
                    #item.ypos = tempy
                    print(f"updated {item.xpos, item.ypos}")
                #for i in wp:
                    #print(i.name,i.xpos,i.ypos)
                #for i in bp:
                    #print(i.name,i.xpos,i.ypos)


            except AttributeError:
                pass
            except NameError:
                pass
            item = None

    pygame.display.update()
