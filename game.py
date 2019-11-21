import pygame
import sys
from player import Player



p = Player(150, 0, 50, 50, 'kw')
class Game:
    def __init__(self):
        self.clickCount = 0
        self.pTemp = p
        self.turnCount = 0
        self.epCount = 0
        #self.id = id
        self.moveString = "None"
        self.helpString = [""]
        self.ready = False


    def check_events(self, pieces, enemies, brd, n, tc):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.clickCount == 0:
                    self.click1(pieces, pos)
                elif self.clickCount == 1:
                    self.click2(self.pTemp, pieces, pos, enemies, brd, n, tc)

                    #self.turnCount += 1
                    #if self.turnCount == 2:
                        #self.turnCount = 0
        #print(self.turnCount)


    def click1(self, pieces, pos):
        """Select your piece"""
        for ps in pieces:
            if ps.click(pos):
                self.pTemp = ps
                self.pTemp.pickedUp = True
                self.clickCount = 1
                #print(ps.type)

    def click2(self, player, pieces, pos, enemies, brd, n, tc):
        if player.checkMove(pos, player, enemies, pieces, self):
            if self.pTemp.pickedUp:
                self.turnCount = tc.getTurnCount()
                self.clickCount -= 1
                tc.turnCounter = n.send("num")
                self.pTemp.move(pos, pieces, enemies, brd, n, self)

                #print(tc.turnCounter)

        else:
            self.pTemp.pickedUp = False
            self.clickCount = 0

    def take_piece(self, pos, player, enemies):
        for ep in enemies:
            if ep.click(pos):
                print(player.type, " takes ", ep.type)
                enemies.remove(ep)

    def take_enpassant(self, player, enemy, enemies):
        #print(player.type, " takes ", enemy.type)
        enemies.remove(enemy)

    def rebuildBoard(self, pieces, enemies, brd, n):
        #print("board rebuilt")
        tmpB = n.send(brd)
        #print(tmpB)
        self.sentFromServer(tmpB, pieces, enemies)

    def sentFromServer(self, brd, pieces, enemies):
        #print(self.turnCount)
        """if self.turnCount == 2:
            self.turnCount = 0"""
        pieces.clear()
        enemies.clear()
        if self.turnCount == 0:
            for p in range(len(brd)):
                for j in range(len(brd[p])):
                    if brd[p][j] == 'pw' or brd[p][j] == 'p':
                        if brd[p][j] == 'pw':
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'pw'))
                        else:
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'p'))
                    elif brd[p][j] == 'rw' or brd[p][j] == 'r':
                        if brd[p][j] == 'rw':
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'rw'))
                        else:
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'r'))
                    elif brd[p][j] == 'nw' or brd[p][j] == 'n':
                        if brd[p][j] == 'nw':
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'nw'))
                        else:
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'n'))
                    elif brd[p][j] == 'bw' or brd[p][j] == 'b':
                        if brd[p][j] == 'bw':
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'bw'))
                        else:
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'b'))
                    elif brd[p][j] == 'kw' or brd[p][j] == 'k':
                        if brd[p][j] == 'kw':
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'kw'))
                        else:
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'k'))
                    elif brd[p][j] == 'qw' or brd[p][j] == 'q':
                        if brd[p][j] == 'qw':
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'qw'))
                        else:
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'q'))
        elif self.turnCount == 1:
            for p in range(len(brd)):
                for j in range(len(brd[p])):
                    if brd[p][j] == 'pw' or brd[p][j] == 'p':
                        if brd[p][j] == 'pw':
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'pw'))
                        else:
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'p'))
                    elif brd[p][j] == 'rw' or brd[p][j] == 'r':
                        if brd[p][j] == 'rw':
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'rw'))
                        else:
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'r'))
                    elif brd[p][j] == 'nw' or brd[p][j] == 'n':
                        if brd[p][j] == 'nw':
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'nw'))
                        else:
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'n'))
                    elif brd[p][j] == 'bw' or brd[p][j] == 'b':
                        if brd[p][j] == 'bw':
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'bw'))
                        else:
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'b'))
                    elif brd[p][j] == 'kw' or brd[p][j] == 'k':
                        if brd[p][j] == 'kw':
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'kw'))
                        else:
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'k'))
                    elif brd[p][j] == 'qw' or brd[p][j] == 'q':
                        if brd[p][j] == 'qw':
                            enemies.append(Player(50 * j, 50 * p, 50, 50, 'qw'))
                        else:
                            pieces.append(Player(50 * j, 50 * p, 50, 50, 'q'))

        #print(brd)

    def sentFromServer2(self, brd, pieces, enemies):
        # print(self.turnCount)
        """if self.turnCount == 2:
            self.turnCount = 0"""
        pieces.clear()
        enemies.clear()
        for p in range(len(brd)):
            for j in range(len(brd[p])):
                if brd[p][j] == 'pw' or brd[p][j] == 'p':
                    if brd[p][j] == 'pw':
                        pieces.append(Player(50 * j, 50 * p, 50, 50, 'pw'))
                    else:
                        enemies.append(Player(50 * j, 50 * p, 50, 50, 'p'))
                elif brd[p][j] == 'rw' or brd[p][j] == 'r':
                    if brd[p][j] == 'rw':
                        pieces.append(Player(50 * j, 50 * p, 50, 50, 'rw'))
                    else:
                        enemies.append(Player(50 * j, 50 * p, 50, 50, 'r'))
                elif brd[p][j] == 'nw' or brd[p][j] == 'n':
                    if brd[p][j] == 'nw':
                        pieces.append(Player(50 * j, 50 * p, 50, 50, 'nw'))
                    else:
                        enemies.append(Player(50 * j, 50 * p, 50, 50, 'n'))
                elif brd[p][j] == 'bw' or brd[p][j] == 'b':
                    if brd[p][j] == 'bw':
                        pieces.append(Player(50 * j, 50 * p, 50, 50, 'bw'))
                    else:
                        enemies.append(Player(50 * j, 50 * p, 50, 50, 'b'))
                elif brd[p][j] == 'kw' or brd[p][j] == 'k':
                    if brd[p][j] == 'kw':
                        pieces.append(Player(50 * j, 50 * p, 50, 50, 'kw'))
                    else:
                        enemies.append(Player(50 * j, 50 * p, 50, 50, 'k'))
                elif brd[p][j] == 'qw' or brd[p][j] == 'q':
                    if brd[p][j] == 'qw':
                        pieces.append(Player(50 * j, 50 * p, 50, 50, 'qw'))
                    else:
                        enemies.append(Player(50 * j, 50 * p, 50, 50, 'q'))





