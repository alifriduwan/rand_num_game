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
                print("lose")
                break
            
            if num_guess < rand_num:
                print(f"Your num_guess of {num_guess} is too low")
                
            elif num_guess > rand_num:
                print(f"Your num_guess of {num_guess} is too high")
                
            else:
                print("win")
                break

    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        game_num_rand(conn, addr)
