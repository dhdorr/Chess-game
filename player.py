import pygame
import math
from board import Board


boardx = [0, 50, 100, 150, 200, 250, 300, 350]
boardy = [0, 50, 100, 150, 200, 250, 300, 350]


class Player:
    def __init__(self, x=0, y=0, width=0, height=0, type='l'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (x,y,width,height)
        self.hasMoved = False
        self.pickedUp = False
        self.x1Prev = x
        self.y1Prev = y
        self.type = type
        self.isCastling = False
        self.enPassantable = False


    def getImage(self):
        if self.type == 'p':
            self.image = pygame.image.load('images/myPawn.png')
        elif self.type == 'k':
            self.image = pygame.image.load('images/myKing.png')
        elif self.type == 'q':
            self.image = pygame.image.load('images/myQueen.png')
        elif self.type == 'r':
            self.image = pygame.image.load('images/myRook.png')
        elif self.type == 'n':
            self.image = pygame.image.load('images/myKnight.png')
        elif self.type == 'b':
            self.image = pygame.image.load('images/myBishop.png')

        elif self.type == 'pw':
            self.image = pygame.image.load('images/myPawnW.png')
        elif self.type == 'kw':
            self.image = pygame.image.load('images/myKingW.png')
        elif self.type == 'qw':
            self.image = pygame.image.load('images/myQueenW.png')
        elif self.type == 'rw':
            self.image = pygame.image.load('images/myRookW.png')
        elif self.type == 'nw':
            self.image = pygame.image.load('images/myKnightW.png')
        elif self.type == 'bw':
            self.image = pygame.image.load('images/myBishopW.png')


    def draw(self, win):
        self.getImage()
        """pygame.draw.rect(win, self.color, self.rect)"""
        win.blit(self.image, self.rect)


    def checkMove(self, pos, player, enemies, myPieces, g):
        for p in myPieces:
            if p.enPassantable:
                p.enPassantable = False
        legalMove = False

        """Check in bounds of board"""
        x1 = pos[0]
        y1 = pos[1]

        if 0 < x1 < 400 and 0 < y1 < 400:
            for i in range(8):
                if boardx[i] <= x1 <= boardx[i] + 50:
                    x1 = boardx[i]
                    for j in range(8):
                        if boardy[j] <= y1 <= boardy[j] + 50:
                            y1 = boardy[j]

            dist = math.sqrt(((x1 - self.x1Prev) ** 2 + (y1 - self.y1Prev) ** 2))
            print(dist)

            tempX = x1
            tempY = y1
            legalMove2 = True

            """Check if move follows rules of piece type"""
            if player.type == 'p' or player.type == 'pw':
                #print("This is a pawn")
                """if self.enPassantable == True:
                    self.enPassantable = False"""
                if self.hasMoved == False:
                    if 50 <= dist <= 100 and x1 == self.x1Prev:
                        self.hasMoved = True
                        legalMove = True
                        self.enPassantable = True
                        for e in enemies:
                            if e.click(pos):
                                legalMove = False
                else:
                    if dist == 50 and x1 == self.x1Prev:
                        if player.type == 'p' and y1 < self.y1Prev:
                            legalMove = True
                        elif player.type == 'pw' and y1 > self.y1Prev:
                            legalMove = True
                        for e in enemies:
                            if e.click(pos):
                                legalMove = False
                    elif 70 < dist < 71:
                        for e in enemies:
                            if e.click(pos):
                                if player.type == 'p' and e.y <= player.y:
                                    legalMove = True
                                    g.take_piece(pos, player, enemies)
                                elif player.type == 'pw' and e.y >= player.y:
                                    legalMove = True
                                    g.take_piece(pos, player, enemies)
                            elif e.enPassantable and player.type == 'p':
                                if x1 == e.x and y1 == e.y - 50:
                                    legalMove = True
                                    g.take_enpassant(player, e, enemies)
                            elif e.enPassantable and player.type == 'pw':
                                if x1 == e.x and y1 == e.y + 50:
                                    legalMove = True
                                    g.take_enpassant(player, e, enemies)

            elif player.type == 'k' or player.type == 'kw':
                #print("This is a king")
                player.isCastling = False
                if dist == 50:
                    legalMove = True
                elif 70 < dist < 71:
                    legalMove = True
                elif dist == 100:
                    if player.hasMoved == False:
                        legalMove = True
                        player.isCastling = True

            elif player.type == 'q' or player.type == 'qw':
                #print("This is a queen")
                for i in range(1, 8):
                    if i * 50 == dist:
                        legalMove = True
                    elif i * 70 < dist < i * 71:
                        legalMove = True

            elif player.type == 'b' or player.type == 'bw':
                #print("This is a bishop")
                for i in range(1, 8):
                    if i * 70 < dist < i * 71:
                        legalMove = True

            elif player.type == 'r' or player.type == 'rw':
                #print("This is a rook")
                for i in range(1, 8):
                    if i * 50 == dist:
                        legalMove = True

            elif player.type == 'n' or player.type == 'nw':
                #print("This is a knight")
                if 111 <= dist <= 112:
                    legalMove = True
                    legalMove2 = True
                    for mp in myPieces:
                        if x1 == mp.x and y1 == mp.y:
                            legalMove = False
                            legalMove2 = False

            # check for pieces in the way
            if player.type != 'n' or player.type != 'nw':
                coords = [tempX, tempY]
                legalMove2 = self.check_in_way(myPieces, enemies, coords)

            # check for castling
            if player.isCastling:
                coords2 = [x1, y1]
                #print(coords2[0], coords2[1])
                legalMove = self.castle_rook(myPieces, coords2, enemies)

            # decide whether move is good or not
            if legalMove and legalMove2:
                print(legalMove2)
                print(self.x1Prev, self.y1Prev, " : ", x1, y1)
                g.moveString = "{} moves to {}"
                #print(g.moveString.format(self.type,(x1,y1)))
                #appended helper string
                g.helpString.insert(1, g.moveString.format(self.type,(x1,y1)))
                g.take_piece(pos, player, enemies)
                return True
            else:
                #print("Illegal move")
                return False
        else:
            return False

    def pawn_end_zone(self):
        if self.y == 350:
            self.type = 'qw'
            #print("pw evolved into ", self.type)
        elif self.y == 0:
            self.type = 'q'
            #print("p evolved into ", self.type)
        self.getImage()

    def check_in_way(self, myPieces, enemies, coords):
        x1 = coords[0]
        y1 = coords[1]
        legalMove = True
        if coords[0] != self.x1Prev and coords[1] != self.y1Prev:
            while coords[0] != self.x1Prev and coords[1] != self.y1Prev:
                for mp in myPieces:
                    if mp.x == coords[0] and mp.y == coords[1]:
                        if mp.x != x1 and mp.y != y1:
                            legalMove = False
                if coords[0] > self.x1Prev and coords[1] > self.y1Prev:
                    coords[0] -= 50
                    coords[1] -= 50
                elif coords[0] < self.x1Prev and coords[1] < self.y1Prev:
                    coords[0] += 50
                    coords[1] += 50
                elif coords[0] > self.x1Prev and coords[1] < self.y1Prev:
                    coords[0] -= 50
                    coords[1] += 50
                elif coords[0] < self.x1Prev and coords[1] > self.y1Prev:
                    coords[0] += 50
                    coords[1] -= 50
                for en in enemies:
                    if en.x == coords[0] and en.y == coords[1]:
                        legalMove = False

        else:
            while coords[0] != self.x1Prev or coords[1] != self.y1Prev:
                for mp in myPieces:
                    if mp.x == coords[0] and mp.y == coords[1]:
                        legalMove = False
                        if mp.x != x1 and mp.y != y1:
                            legalMove = False

                if coords[1] > self.y1Prev:
                    coords[1] -= 50
                elif coords[1] < self.y1Prev:
                    coords[1] += 50
                elif coords[0] > self.x1Prev:
                    coords[0] -= 50
                elif coords[0] < self.x1Prev:
                    coords[0] += 50
                for en in enemies:
                    if en.x == coords[0] and en.y == coords[1]:
                        legalMove = False
        return legalMove

    def castle_rook(self, myPieces, coords, enemies):
        pInWay = False
        legalMove = False
        for mp in myPieces:
            if (mp.x == coords[0] + 100 and mp.y == coords[1]) and (mp.type == 'r' or mp.type == 'rw'):
                for pc in myPieces:
                    if mp.x - 50 == pc.x and mp.y == pc.y:
                        pInWay = True
                        legalMove = False
                if pInWay == False:
                    mp.x = coords[0] - 50
                    mp.y = coords[1]
                    coords2 = [mp.x, mp.y]
                    mp.move(coords2, myPieces, enemies)
                    legalMove = True
                    #print("Castling")
            elif (mp.x == coords[0] - 50 and mp.y == coords[1]) and (mp.type == 'r' or mp.type == 'rw'):
                mp.x = coords[0] + 50
                mp.y = coords[1]
                coords2 = [mp.x, mp.y]
                mp.move(coords2, myPieces, enemies)
                legalMove = True
                #print("Castling")
        return legalMove

    def move(self, pos, pieces, enemies, brd, n, g):
        x1 = pos[0]
        y1 = pos[1]
        pX = int(self.x1Prev / 50)
        pY = int(self.y1Prev / 50)
        #print("X", pX, "Y", pY)

        """This for loop snaps piece to grid"""
        for i in range(8):
            if boardx[i] <= x1 <= boardx[i] + 50:
                self.x = boardx[i]
                for j in range(8):
                    if boardy[j] <= y1 <= boardy[j] + 50:
                        self.y = boardy[j]
                        brd[j][i] = self.type
                        brd[pY][pX] = 0


        if self.type == 'p' or self.type == 'pw':
            self.pawn_end_zone()

        self.update(pieces)

        #check what array slot the x and y would fit in to, update array
        self.x1Prev = self.x
        self.y1Prev = self.y
        g.rebuildBoard(pieces, enemies, brd, n)



    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:

            return True
        else:
            return False

    def update(self, pieces):
        """self.x1Prev = self.x
        self.y1Prev = self.y"""
        self.hasMoved = True
        for p in pieces:
            p.rect = (p.x, p.y, p.width, p.height)









