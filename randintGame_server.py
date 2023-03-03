import random
import socket

HOST = '127.0.0.1'
PORT = 65432

def game_num_rand(conn, addr):
    rand_num = random.randint(1, 100)
    round_play = 0

    while True:
            data = conn.recv(1024)
            if not data:
                break
            num_guess = int(data.decode())
            round_play += 1
            
            if round_play > 20:
                msg = "Lost!"
                conn.sendall(msg.encode())
                break
            
            if num_guess < rand_num:
                msg = (f"Your number guess of {num_guess} lower than random number")
                
            elif num_guess > rand_num:
                msg = (f"Your number guess of {num_guess} highter than random number")
                
            else:
                msg = "Won!"
                conn.sendall(msg.encode())
                break

            conn.sendall(msg.encode())
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        game_num_rand(conn, addr)
