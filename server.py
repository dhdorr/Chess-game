from socket import *
from board import Board
import pickle
from _thread import *
server = "192.168.1.217"
port = 5555

s = socket(AF_INET, SOCK_DGRAM)
try:
    s.bind((server, port))
except:
    print("error")
print("The server is ready to receive")
b = Board()
tst = b.board
brdStandIn = [[0 for i in range(8)] for j in range(8)]

games = {}

def mainGame():
    pNum = 0
    turn = 0
    print("hello")

    while True:
        message, clientAddress = s.recvfrom(2048)
        if not message:
            break
        else:
            #test = pickle.loads(message)
            """try:
                test = pickle.loads(message)
                tst = test
                modifiedMessage = pickle.dumps(test)
                s.sendto(modifiedMessage, clientAddress)
            except:
                if message.decode() == "get":
                    modifiedMessage = pickle.dumps(tst)
                    s.sendto(modifiedMessage, clientAddress)"""
            data = pickle.loads(message)
            try:
                if data == "get":
                    modifiedMessage = pickle.dumps(b.board)
                    s.sendto(modifiedMessage, clientAddress)
                elif data == "num":
                    turn += 1
                    if turn == 2:
                        turn = 0
                    modifiedMessage = pickle.dumps(turn)
                    s.sendto(modifiedMessage, clientAddress)
                elif data == "player":
                    pNum += 1
                    if pNum > 1:
                        pNum = 0
                    modifiedMessage = pickle.dumps(turn)
                    s.sendto(modifiedMessage, clientAddress)
                elif data == "getnum":
                    modifiedMessage = pickle.dumps(turn)
                    s.sendto(modifiedMessage, clientAddress)
                elif data == "getPlayer":
                    modifiedMessage = pickle.dumps(pNum)
                    pNum += 1
                    s.sendto(modifiedMessage, clientAddress)
                else:
                    for i in range(8):
                        for j in range(8):
                            b.board[i][j] = data[i][j]
                            brdStandIn[i][j] = data[i][j]
                    modifiedMessage = pickle.dumps(brdStandIn)
                    s.sendto(modifiedMessage, clientAddress)
                    #s.sendall(modifiedMessage)
            except:
                modifiedMessage = pickle.dumps(b.board)
                s.sendto(modifiedMessage, clientAddress)

mainGame()


