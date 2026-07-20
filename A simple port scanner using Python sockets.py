import socket
from datetime import datetime

def scan_port(target_ip, port, timeout=1):
    """Try to connect to a single port. Return True if open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((target_ip, port))
        return result == 0
    finally:
        sock.close()

def scan_range(target, start_port, end_port, timeout=1):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Could not resolve hostname: {target}")
        return

    print(f"Scanning {target} ({target_ip})")
    print(f"Ports {start_port}-{end_port} | Started at {datetime.now()}")
    print("-" * 50)

    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port, timeout):
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "unknown"
            print(f"Port {port:5d} OPEN   ({service})")
            open_ports.append(port)

    print("-" * 50)
    print(f"Scan complete. {len(open_ports)} open port(s) found.")
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ").strip()
    start = int(input("Start port (e.g. 1): ") or 1)
    end = int(input("End port (e.g. 1024): ") or 1024)
    scan_range(target, start, end)