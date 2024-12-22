#!/usr/bin/python3
import socket
import random
import time

# Server sozlamalari
HOST = "0.0.0.0"
PORT = 8888

# Socketni sozlash
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server {HOST}:{PORT} manzilida ishlayapti...")

try:
    while True:
        # Mijoz ulanishini qabul qilish
        client_socket, client_address = server_socket.accept()
        print(f"Ulanish o'rnatildi: {client_address}")

        try:
            # Salomlashish va topshiriqni tushuntirish
            greeting_message = "Iltimos, berilgan dastlabki ikki sonni qo'shing va oxirgi son bilan ko'paytiring: (a+b)*c.\n"
            greeting_message = greeting_message + "Bu 3 soniya ichida bajarilishi kerak\n"

            # Tasodifiy sonlarni yaratish
            first = random.randint(1, 10)
            second = random.randint(1, 10)
            third = random.randint(1, 5)

            # Sonlarni yuborish
            greeting_message +=f"First: {first}\n"
            greeting_message +=f"Second: {second}\n"
            greeting_message +=f"Third: {third}"
            client_socket.sendall(greeting_message.encode())
            start_time = time.time()
            # To'g'ri javobni hisoblash
            correct_answer = (first + second) * third

            # Mijozning javobini qabul qilish
            client_response = client_socket.recv(1024).decode().strip()
            elapsed_time = time.time() - start_time

            # Javobni tekshirish
            if elapsed_time <= 3 and client_response.isdigit() and int(client_response) == correct_answer:
                response = "PYTHON{Eng_t3z_k0d3r_G'arbda}"
                client_socket.sendall(response.encode())
            else:
                print("Javob noto'g'ri yoki vaqt tugagan.")

        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")

        # Mijoz ulanishini yopish
        client_socket.close()
except KeyboardInterrupt:
    print("\nServer to'xtatildi.")
finally:
    server_socket.close()
