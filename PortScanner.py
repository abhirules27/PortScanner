# PortScanner with Threads
import socket
import threading
import queue

IP = '192.168.0.181'
q = queue.Queue()

# Storing port Nos in Queue
for port in range (55575, 55578):
    q.put(port)


def scan():
    while not q.empty():
        port = q.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((IP, port))
                print(f'Port {port} is open!')
            except:
                pass
        q.task_done()

# Create No of threads we want to use
for port in range(30):
    t = threading.Thread(target=scan, daemon=True)
    t.start()

q.join()
print('Finished')