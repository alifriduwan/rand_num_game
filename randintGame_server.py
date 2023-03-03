import random
import socket

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    print('Connected by', addr)
    rand_num = random.randint(1, 100)
    round_play = 0

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            num_guess = int(data.decode())
            
            if round_play > 20:
                msg = "Lose"
                conn.sendall(msg.encode())
                break
            round_play += 1
            if num_guess < rand_num:
                msg = (f"Your number guess of {num_guess} lower than random number")
                
            elif num_guess > rand_num:
                msg = (f"Your number guess of {num_guess} highter than random number")
                
            else:
                msg = "Win"
                conn.sendall(msg.encode())
                break
                
            conn.sendall(msg.encode())

        except ValueError:
            conn.sendall("Invalid input, please enter a number between 1 and 100".encode())

    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        handle_client(conn, addr)
