# test_module.py

import unittest
from port_scanner import get_open_ports

class TestPortScanner(unittest.TestCase):

    def test_valid_hostname_verbose(self):
        result = get_open_ports("scanme.nmap.org", [20, 80], True)
        self.assertIn("Open ports for", result)
        self.assertIn("22", result)  # SSH
        self.assertIn("80", result)  # HTTP

    def test_valid_ip_non_verbose(self):
        ports = get_open_ports("45.33.32.156", [20, 80])
        self.assertIsInstance(ports, list)
        self.assertIn(22, ports)
        self.assertIn(80, ports)

    def test_invalid_hostname(self):
        result = get_open_ports("invalid.hostname.test", [20, 25])
        self.assertEqual(result, "Error: Invalid hostname")

    def test_invalid_ip(self):
        result = get_open_ports("123.456.789.000", [20, 25])
        self.assertEqual(result, "Error: Invalid IP address")

    def test_service_mapping(self):
        result = get_open_ports("scanme.nmap.org", [22, 22], True)
        self.assertIn("ssh", result)

if __name__ == '__main__':
    unittest.main()
