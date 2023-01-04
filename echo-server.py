import socket
import pickle

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    plain_data = [[1, 7],
    [2, 7],
[3, 7],
[4, 7],
[5, 7],
[6, 7],
[7, 7],
[8, 7],
[5, 8],
[4, 8],
[3, 8],
[4, 4],
[2, 8],
[7, 8],
[1, 8],
[8, 8],
[1, 2],
[2, 2],
[3, 2],
[4, 2],
[5, 2],
[6, 2],
[7, 2],
[8, 2],
[5, 1],
[4, 1],
[3, 1],
[6, 1],
[2, 1],
[7, 1],
[1, 1],
[8, 1]]
    data = pickle.dumps(plain_data)
    s.send(data)
    data = s.recv(1024)
    data = pickle.loads(data)
print(f"Received {data}")