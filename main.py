# main.py

from port_scanner import get_open_ports

# Sample test calls
print(get_open_ports("scanme.nmap.org", [20, 80], True))
print(get_open_ports("209.216.230.240", [440, 445]))
print(get_open_ports("www.stackoverflow.com", [79, 82], True))
