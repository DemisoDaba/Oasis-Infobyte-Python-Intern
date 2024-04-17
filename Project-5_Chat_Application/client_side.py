import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            client_socket.close()
            break

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Continuously send messages without waiting for input
while True:
    try:
        message = input()
        client_socket.send(message.encode())
    except Exception as e:
        print(f"Error sending message: {e}")
        client_socket.close()
        break
