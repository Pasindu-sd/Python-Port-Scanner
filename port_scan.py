import socket
import threading

# Get Target IP Address
target = input("Enter the IP address to scan: ")

# Get Port range
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

# Scan function
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # 1s timeout
        result = s.connect_ex((ip, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
        s.close()
    except:
        pass

# Thread list to keep track
threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(target, port))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("\nScanning Completed!")
