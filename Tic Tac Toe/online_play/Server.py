import socket
from _thread import start_new_thread
from .game import GameBoard
from random import choice
import pickle

def start_server(ip_addr):
    global s, Game

    server = ip_addr
    print(server)
    port = 5555

    #for create server - start
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        s.bind((server,port))
    except socket.error as e:
        print(str(e))

    s.listen(2) #limit of connection only 2 player
    print("Waiting For A Connection, Server Started.")
    #end

    #list of players data(objects)
    Game = GameBoard()
    idCount = 0
    p = choice(["O","X"])

    while True:
        conn,addr = s.accept()
        print("Connected to :",addr)

        idCount += 1
        
        if idCount%2 == 1:
            pass
        else:
            Game.ready = True
            p = "X" if p == "O" else "O"

        start_new_thread(threaded_client,(conn, p))

        if idCount == 2:
            break

def threaded_client(conn, player_sign):
    global Game

    conn.send(str.encode(player_sign))

    while True:
        try:
            data = conn.recv(1024).decode()

            if not data:
                print("Disconnected.")
                break
            else:
                if data == "reset":
                    Game.reset_board()
                elif data == "leave":
                    Game.leave = True
                elif data != "get":
                    Game.play(player_sign, (int(data[0]),int(data[1])))

            conn.sendall(pickle.dumps(Game))
        except:
            break
        
    print("Lost Connection.")
    conn.close()

if __name__ == "__main__":
    start_server("localhost")