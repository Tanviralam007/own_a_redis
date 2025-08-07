import socket, threading, time

class RedisServer:
    def __init__(self, host='127.0.1', port=6379):
        self.host = host
        self.port = port
        self.server_socket = None
        self.is_running = False
    
    def start(self):
        print(f"Initializing server on {self.host}:{self.port}")
        print("ENV setup completed")


if __name__ == "__main__":
    server = RedisServer()
    server.start()