import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(100)

print("DoS Demo Server")
print(f"Listening on {HOST}:{PORT}")
print("Waiting for connections...")

count = 0

try:
    while True:
        conn, address = server.accept()
        count += 1
        data = conn.recv(1024)
        print(f"Request #{count} received from {address[0]}:{address[1]}")
        conn.send(b"Server received your request.")
        conn.close()
except KeyboardInterrupt:
    print("\nServer stopped.")
finally:
    server.close()
