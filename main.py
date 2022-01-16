from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write("SUP".encode())


def main():
    PORT = 1234
    server = HTTPServer(('', PORT), Handler)
    print("Server is up and running")
    server.serve_forever()
    server.close()


if __name__ == "__main__":
    main()
