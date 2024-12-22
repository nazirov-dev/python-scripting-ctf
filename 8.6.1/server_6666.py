#!/usr/bin/python3
import socket
import os

# Serverni sozlash
HOST = "0.0.0.0"  # Hammasini tinglash
PORT = 6666       # Port raqami

# Socket yaratish
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Maksimal ulanishlar soni

print(f"Server {HOST}:{PORT} manzilida tinglamoqda...")

try:
    while True:
        # Mijozni ulanishini qabul qilish
        client_socket, client_address = server_socket.accept()
        print(f"Ulanish: {client_address}")

        # Javob yuborish
        message = "PYTHON{Mij0z_bi1an_4_Ulan3d}"
        client_socket.sendall(message.encode())

        # Mijoz ulanishini yopish
        client_socket.close()
except KeyboardInterrupt:
    print("\nServer to'xtatildi.")
finally:
    server_socket.close()

