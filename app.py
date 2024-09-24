import http.server
import socketserver

# Port to serve the application
PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving HTTP on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
