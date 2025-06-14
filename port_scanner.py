# port_scanner.py

import socket
from common_ports import ports_and_services

# Helper to check if string is a valid IPv4 address
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)  # Checks if IP is properly formatted
        return True
    except socket.error:
        return False

# Main function to scan open ports
def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    # Resolve target to IP address
    try:
        ip = socket.gethostbyname(target)  # Resolves domain to IP
    except socket.gaierror:
        # If it's a valid IP but unreachable
        if is_valid_ip(target):
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"

    # Perform port scanning using TCP connect_ex
    for port in range(port_range[0], port_range[1] + 1):
        try:
            # Create socket for TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 1-second timeout for each port
            result = sock.connect_ex((ip, port))  # 0 means open
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception:
            continue

    # If verbose=True, return formatted string output
    if verbose:
        # Try to resolve back the hostname from the IP
        try:
            resolved_name = socket.gethostbyaddr(ip)[0]
        except Exception:
            resolved_name = target

        # Header
        output = f"Open ports for {resolved_name} ({ip})\nPORT     SERVICE"
        
        # Body (list of open ports and services)
        for port in open_ports:
            service = ports_and_services.get(port, 'unknown')
            output += f"\n{str(port).ljust(8)}{service}"
        
        return output

    # Otherwise, return just the list of open ports
    return open_ports
