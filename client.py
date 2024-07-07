import yaml
import os

class Client:
    def __init__(self):
        config = self.load_config()
        self.ip_address = config['ServerIPAddress']

    def load_config(self):
        config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def print_ip(self):
        print(f"Client IP Address: {self.ip_address}")

if __name__ == "__main__":
    client = Client()
    client.print_ip()
