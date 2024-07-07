class Client:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def print_ip(self):
        print(f"Client IP Address: {self.ip_address}")
