import threading
from socket import *
import time
import sys

PORT = 12000
ADDR = (SERVER, PORT)
DISCONNECT = 'disconnect'
MAX_BUFFER = 1024
#SERVER = 'enter IP here'

## Establish socket ##
try:
    client_socket = socket(AF_INET, SOCK_STREAM)
except socket.error as e1:
    print("[WARNING] Error creating socket: %s" % e1)
    sys.exit(1)

## Bind socket to IP and Port + listen on port ##
client_socket.bind(ADDR)
client_socket.listen(1)

## Outside client trying to connect to us ##
def receive_connection():
    try:
        connection, addr = client_socket.accept()
        thread = threading.Thread(target = receive_message, args = (connection, addr))
        thread.start()
    except socket.error as e2:
        print("[WARNING] Error accepting connection from client: %s" % e2)
        sys.exit(1)

## Receiving message from other client ##
def receive_message(connection, addr):
    print(f"[SUCCESS] Successful connection with {addr}")

    connected = True
    while connected:
        message_received = connection.recv(MAX_BUFFER).decode()

        if message_received == DISCONNECT:
            connected = False
            print(f"[DISCONNECTED] {addr} has disconnected from the chat...")
            connection.close()
        else:
            print(f"[RECEIVED] Message received from {addr}: {message_received}")


