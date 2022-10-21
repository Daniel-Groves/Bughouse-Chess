def check_checker(wp, bp, wking, bking):
    global checking_pieces
    checking_pieces = []
    if move:
        pieces = bp
        king = wking
    else:
        pieces = wp
        king = bking
    global piece

    for piece in pieces:
        if piece.name[1] == "k":
            checktake = False
        elif piece.name[1] == "q":
            checktake = queen_moves(king.xpos - piece.xpos, king.ypos - piece.ypos, piece.xpos, piece.ypos, piece)
            if checktake:
                checking_pieces.append(piece)
                return checktake
        elif piece.name[1] == "b":
            checktake = bishop_moves(king.xpos - piece.xpos, king.ypos - piece.ypos, piece.xpos, piece.ypos, piece)
            if checktake:
                checking_pieces.append(piece)
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
            checktake = white_pawn_moves(piece.xpos - king.xpos, piece.ypos - king.ypos, king.xpos, king.ypos,
                                         piece.move_num, piece, takenpiece)
            if checktake:
                checking_pieces.append(piece)
                return checktake
        elif piece.name[0:2] == "bp":
            checktake = black_pawn_moves(piece.xpos - king.xpos, piece.ypos - king.ypos, king.xpos, king.ypos,
                                         piece.move_num, piece, takenpiece)
            if checktake:
                checking_pieces.append(piece)
                return checktake
        else:
            return False

def checkmate_checker(wp, bp, wking, bking, checking_pieces):
    checkmate = True
    if move:
        pieces = wp
        king = wking
        constant = 1
    else:
        pieces = bp
        king = bking
        constant = -1

    for vector in king_vectors:
        tempx = king.xpos
        tempy = king.ypos
        king.xpos = king.xpos + vector[0]
        king.ypos = king.ypos + vector[1]
        blockage = False
        for piece in pieces:
            if (piece.xpos, piece.ypos) == (king.xpos, king.ypos) and piece.name[0] != king.name[0]:
                blockage = True
        if move_valid(king, king.xpos, king.ypos, wp, bp, wking, bking, tempx, tempy) and not check_checker(wp, bp,
                                                                                                            wking,
                                                                                                            bking) and king.xpos > 0 and king.ypos > 0 and not blockage:
            checkmate = False
        king.xpos = tempx
        king.ypos = tempy

    for checker in checking_pieces:
        if checker.name[1] == "b":
            for i in range(0, abs(king.xpos - checker.xpos)+1):
                for piece in pieces:
                    if piece.name[1] == "k":
                        continue
                    tempx = piece.xpos
                    tempy = piece.ypos
                    piece.xpos = checker.xpos + (numpy.sign(king.xpos - checker.xpos) * i)
                    piece.ypos = checker.ypos + (numpy.sign(king.ypos - checker.ypos) * i)
                    if i == 0:
                        ap.remove(checker)
                        takenpiece = checker
                        if checker.name[0] == "w":
                            wp.remove(checker)
                        else:
                            bp.remove(checker)
                        tempitem = checker
                    if move_valid(piece, piece.xpos, piece.ypos, wp, bp, wking, bking, tempx,
                                  tempy) and not check_checker(wp, bp, wking, bking):
                        checkmate = False
                        piece.xpos = tempx
                        piece.ypos = tempy
                    else:
                        piece.xpos = tempx
                        piece.ypos = tempy
                    if tempitem:
                        ap.append(tempitem)
                        if tempitem.name[0] == "w":
                            wp.append(tempitem)
                        else:
                            bp.append(tempitem)
                        tempitem = None
        elif checker.name[1] == "r":
            if checker.xpos - king.xpos == 0:
                for i in range(0, abs(king.ypos - checker.ypos)):
                    for piece in pieces:
                        if piece.name[1] == "k":
                            continue
                        tempx = piece.xpos
                        tempy = piece.ypos
                        piece.ypos = checker.ypos + (numpy.sign(king.ypos - checker.ypos) * i)
                        if i == 0:
                            ap.remove(checker)
                            takenpiece = checker
                            if checker.name[0] == "w":
                                wp.remove(checker)
                            else:
                                bp.remove(checker)
                            tempitem = checker
                        if move_valid(piece, checker.xpos, piece.ypos, wp, bp, wking, bking, tempx,
                                      tempy) and not check_checker(wp, bp, wking, bking):
                            checkmate = False
                            piece.xpos = tempx
                            piece.ypos = tempy
                        else:
                            piece.xpos = tempx
                            piece.ypos = tempy
                        if tempitem:
                            ap.append(tempitem)
                            if tempitem.name[0] == "w":
                                wp.append(tempitem)
                            else:
                                bp.append(tempitem)
                            tempitem = None
            if checker.ypos - king.ypos == 0:
                for i in range(0, abs(wking.xpos - checker.xpos) + 1):
                    for piece in pieces:
                        if piece.name[1] == "k":
                            continue
                        tempx = piece.xpos
                        tempy = piece.ypos
                        piece.xpos = checker.xpos + (numpy.sign(king.xpos - checker.xpos) * i)
                        piece.ypos = checker.ypos
                        if i == 0:
                            ap.remove(checker)
                            takenpiece = checker
                            if checker.name[0] == "w":
                                wp.remove(checker)
                            else:
                                bp.remove(checker)
                            tempitem = checker
                        if move_valid(piece, piece.xpos, piece.ypos, wp, bp, wking, bking, tempx, tempy):
                            checkmate = False
                            piece.xpos = tempx
                            piece.ypos = tempy
                        else:
                            piece.xpos = tempx
                            piece.ypos = tempy
                        if tempitem:
                            ap.append(tempitem)
                            if tempitem.name[0] == "w":
                                wp.append(tempitem)
                            else:
                                bp.append(tempitem)
                            tempitem = None
            pass
        elif checker.name[1] == "q":
            if checker.xpos - king.xpos == 0:
                for i in range(0, abs(king.ypos - checker.ypos) + 1):
                    for piece in pieces:
                        if piece.name[1] == "k":
                            continue
                        tempx = piece.xpos
                        tempy = piece.ypos
                        piece.xpos = checker.xpos
                        piece.ypos = checker.ypos + (constant * i)
                        if i == 0:
                            ap.remove(checker)
                            takenpiece = checker
                            if checker.name[0] == "w":
                                wp.remove(checker)
                            else:
                                bp.remove(checker)
                            tempitem = checker
                        if move_valid(piece, checker.xpos, checker.ypos + (constant * i), wp, bp, wking, bking, tempx,
                                      tempy):
                            checkmate = False
                            piece.xpos = tempx
                            piece.ypos = tempy
                        else:
                            piece.xpos = tempx
                            piece.ypos = tempy
                        if tempitem:
                            ap.append(tempitem)
                            if tempitem.name[0] == "w":
                                wp.append(tempitem)
                            else:
                                bp.append(tempitem)
                            tempitem = None
            if checker.ypos - king.ypos == 0:
                for i in range(0, abs(wking.xpos - checker.xpos) + 1):
                    for piece in pieces:
                        if piece.name[1] == "k":
                            continue
                        tempx = piece.xpos
                        tempy = piece.ypos
                        piece.xpos = checker.xpos + (numpy.sign(king.xpos - checker.xpos) * i)
                        piece.ypos = checker.ypos
                        if i == 0:
                            ap.remove(checker)
                            takenpiece = checker
                            if checker.name[0] == "w":
                                wp.remove(checker)
                            else:
                                bp.remove(checker)
                            tempitem = checker
                        if move_valid(piece, piece.xpos, piece.ypos, wp, bp, wking, bking, tempx,
                                      tempy):
                            checkmate = False
                            piece.xpos = tempx
                            piece.ypos = tempy
                        else:
                            piece.xpos = tempx
                            piece.ypos = tempy
                        if tempitem:
                            ap.append(tempitem)
                            if tempitem.name[0] == "w":
                                wp.append(tempitem)
                            else:
                                bp.append(tempitem)
                            tempitem = None
            else:
                for i in range(0, abs(king.xpos - checker.xpos) + 1):
                    for piece in pieces:
                        if piece.name[1] == "k":
                            continue
                        tempx = piece.xpos
                        tempy = piece.ypos
                        piece.xpos = checker.xpos + (numpy.sign(king.xpos - checker.xpos) * i)
                        piece.ypos = checker.ypos + (numpy.sign(king.ypos - checker.ypos) * i)
                        if i == 0:
                            ap.remove(checker)
                            takenpiece = checker
                            if checker.name[0] == "w":
                                wp.remove(checker)
                            else:
                                bp.remove(checker)
                            tempitem = checker
                        if move_valid(piece, piece.xpos, piece.ypos, wp, bp, wking, bking, tempx,
                                      tempy):
                            checkmate = False
                            piece.xpos = tempx
                            piece.ypos = tempy
                        else:
                            piece.xpos = tempx
                            piece.ypos = tempy
                        if tempitem:
                            ap.append(tempitem)
                            if tempitem.name[0] == "w":
                                wp.append(tempitem)
                            else:
                                bp.append(tempitem)
                            tempitem = None
            pass
        checking_pieces = None
    return checkmate