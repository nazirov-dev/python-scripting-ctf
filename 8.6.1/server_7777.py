#!/usr/bin/python3
import socket
import os

# Serverni sozlash
HOST = "0.0.0.0"  # Hammasini tinglash
PORT = 7777       # Port raqami

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

        # Ulanishda birinchi javob yuborish
        greeting_message = "Iltimos, kvadrat bo'ladigan raqamni yuboring: s"
        client_socket.sendall(greeting_message.encode())

        # Mijozdan ma'lumot qabul qilish
        client_data = client_socket.recv(1024).decode()
        print(f"Mijozdan ma'lumot: {client_data}")

        # Javobni tanlash
        try:
            # Mijozdan kelgan ma'lumotni son sifatida ko'rib chiqish
            number = int(client_data)
            response = f"{number **2} "+" PYTHON{Vaziyatni_aniq1ash}"
        except ValueError:
            # Agar son bo'lmasa, harf deb hisoblash
            response = "PYTHON{X0'p_Bu_t0'g'ri_em45}"

        # Javobni yuborish
        client_socket.sendall(response.encode())

        # Mijoz ulanishini yopish
        client_socket.close()
except KeyboardInterrupt:
    print("\nServer to'xtatildi.")
finally:
    server_socket.close()
