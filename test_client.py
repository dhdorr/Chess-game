import pygame
from socket import *
import pickle
from player import Player
from game import Game
from network import Network
"""server = "192.168.1.217"
port = 5555
s = socket(AF_INET, SOCK_DGRAM)
message = "get"
s.sendto(message.encode(), (server, port))
modifiedMessage, serverAddress = s.recvfrom(2048)
brd = pickle.loads(modifiedMessage)

print(brd)"""
#s.close()

pygame.font.init()
width = 600
height = 500
win = pygame.display.set_mode((width, height))
chessBoard = pygame.image.load('images/chessBoard.png')
pygame.display.set_caption("Client")

pieces = []
enemies = []
"""x = 0
y = 0
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
                enemies.append(Player(50 * j, 50 * p, 50, 50, 'q'))"""
class TurnCounter:
    def __init__(self):
        self.turnCounter = 0
        self.playerNum = 3
    def getTurnCount(self):
        return self.turnCounter

def main():

    clock = pygame.time.Clock()
    #print(len(brd))
    g = Game()
    n = Network()
    tc = TurnCounter()

    text = "getPlayer"
    pNum = n.send(text)
    text = "get"
    brd = n.send(text)
    g.sentFromServer(brd, pieces, enemies)


    #turnCount = 0

    while True:
        clock.tick(10)
        #modifiedMessage, serverAddress = s.recvfrom(2048)
        #newBoard = pickle.loads(modifiedMessage)
        """keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            try:
                text = "get"
                brd = n.send(text)
                g.sentFromServer(brd, pieces, enemies)
            except:
                pass
        elif keys[pygame.K_d]:
            try:
                text = [['rw', 'nw', 'bw', 'kw', 'qw', 'bw', 'nw', 'rw'],
                        [0, 'pw', 'pw', 'pw', 'pw', 'pw', 'pw', 'pw'],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        ['pw', 0, 0, 0, 0, 0, 0, 0],
                        ['p', 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                        ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']]
                brd = n.send(text)
                g.sentFromServer(brd, pieces, enemies)
            except:
                pass"""
        #getFromServer(n,)
        #g.rebuildBoard(pieces, enemies, brd, n)
        #print(tc.getTurnCount())
        text = "getnum"
        tc.turnCounter = n.send(text)
        #print(tc.turnCounter)
        if tc.turnCounter == 0 and pNum == 0:
            text = "get"
            brd = n.send(text)
            g.sentFromServer2(brd, pieces, enemies)
            g.check_events(pieces, enemies, brd, n, tc)

            #g.rebuildBoard(pieces, enemies, brd, n)
            #sendToServer()
        elif tc.turnCounter == 1 and pNum == 1:
            text = "get"
            brd = n.send(text)
            g.sentFromServer2(brd, pieces, enemies)
            g.check_events(enemies, pieces, brd, n, tc)

            #g.rebuildBoard(enemies, pieces, brd, n)
            #sendToServer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()

        redrawWindow(win)
    #s.close()

def redrawWindow(win):
    win.fill((102, 102, 102))
    win.blit(chessBoard, (0, 0))

    for piece in pieces:
        piece.draw(win)
    for en in enemies:
        en.draw(win)
    #sendToServer(board)

    pygame.display.update()

def getFromServer():
    print("retrieve from server")


"""def sentFromServer(brd):
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
    print("ehllo")"""

def sendToServer():
    print("at send to server")
    board = [[0 for i in range(8)] for j in range(8)]
    for p in pieces:
        if p.type == 'pw':
            board[p.y/50][p.x/50] = p.type
        elif p.type == 'rw':
            board[p.y/50][p.x/50] = p.type
        elif p.type == 'bw':
            board[p.y/50][p.x/50] = p.type
        elif p.type == 'nw':
            board[p.y/50][p.x/50] = p.type
        elif p.type == 'qw':
            board[p.y/50][p.x/50] = p.type
        elif p.type == 'kw':
            board[p.y/50][p.x/50] = p.type
    for e in enemies:
        if e.type == 'pw':
            board[e.y/50][e.x/50] = e.type
        elif e.type == 'rw':
            board[e.y/50][e.x/50] = e.type
        elif e.type == 'bw':
            board[e.y/50][e.x/50] = e.type
        elif e.type == 'nw':
            board[e.y/50][e.x/50] = e.type
        elif e.type == 'qw':
            board[e.y/50][e.x/50] = e.type
        elif e.type == 'kw':
            board[e.y/50][e.x/50] = e.type
    print(board)

    """message = pickle.dumps(board)
    #message = pickle.dumps("Stinky")
    #msg =  pickle.dumps(message)
    s.sendto(message, (server, port))
    modifiedMessage, serverAddress = s.recvfrom(2048)
    brd1 = pickle.loads(modifiedMessage)
    #print(brd1)
    sentFromServer2(brd1)
    #modifiedMessage, serverAddress = s.recvfrom(2048)
    #newMsg = pickle.loads(modifiedMessage)"""

def sentFromServer2(brd1):
    pieces.clear()
    enemies.clear()
    for p in range(len(brd1)):
        for j in range(len(brd1[p])):
            if brd1[p][j] == 'pw' or brd1[p][j] == 'p':
                if brd1[p][j] == 'pw':
                    pieces.append(Player(50 * j, 50 * p, 50, 50, 'pw'))
                else:
                    enemies.append(Player(50 * j, 50 * p, 50, 50, 'p'))
            elif brd1[p][j] == 'rw' or brd1[p][j] == 'r':
                if brd1[p][j] == 'rw':
                    pieces.append(Player(50 * j, 50 * p, 50, 50, 'rw'))
                else:
                    enemies.append(Player(50 * j, 50 * p, 50, 50, 'r'))
            elif brd1[p][j] == 'nw' or brd1[p][j] == 'n':
                if brd1[p][j] == 'nw':
                    pieces.append(Player(50 * j, 50 * p, 50, 50, 'nw'))
                else:
                    enemies.append(Player(50 * j, 50 * p, 50, 50, 'n'))
            elif brd1[p][j] == 'bw' or brd1[p][j] == 'b':
                if brd1[p][j] == 'bw':
                    pieces.append(Player(50 * j, 50 * p, 50, 50, 'bw'))
                else:
                    enemies.append(Player(50 * j, 50 * p, 50, 50, 'b'))
            elif brd1[p][j] == 'kw' or brd1[p][j] == 'k':
                if brd1[p][j] == 'kw':
                    pieces.append(Player(50 * j, 50 * p, 50, 50, 'kw'))
                else:
                    enemies.append(Player(50 * j, 50 * p, 50, 50, 'k'))
            elif brd1[p][j] == 'qw' or brd1[p][j] == 'q':
                if brd1[p][j] == 'qw':
                    pieces.append(Player(50 * j, 50 * p, 50, 50, 'qw'))
                else:
                    enemies.append(Player(50 * j, 50 * p, 50, 50, 'q'))
    print("ehllo2")

main()