import argparse
import sys
from src.server import RedisServer

def main():
    parser = argparse.ArgumentParser(description="STARTED THE REDIS SERVER")
    parser.add_argument('--host', type=str, default='6379', help='Host to bind to')
    parser.add_argument('--port', type=int, default=6379, help='Port to bind to')

    args = parser.parse_args()

    try:
        server = RedisServer(host=args.host, port=args.port)
        print(f"Starting the server on {args.host}:{args.port}")
        server.start()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Failed to start the server: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

