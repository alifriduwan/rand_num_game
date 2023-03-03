import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432    # The port used by the server


def num_guess():

    while True:
        try:
            number = int(input("Enter your number: "))
            if number < 1 or number > 100:
                raise ValueError("Number should between 1 and 100")
            return number
            
        except ValueError as A :
            print(str(A))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Guess the number between 1 and 100!")
    while True:
        guess = num_guess()
        s.sendall(str(guess).encode())
        data = s.recv(1024)
        print(data.decode())
        if "Win" in data.decode():
            print("Win!!!")
            break
        elif "Lose" in data.decode():
            print("Lose!!!")
            break
        
