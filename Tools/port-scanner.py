import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def scan_range(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    scan_range(target_ip, 1, 1024)

