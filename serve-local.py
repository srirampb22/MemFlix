from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class MemflixHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/admin", "/admin/"):
            self.path = "/admin.html"
        elif self.path == "/":
            self.path = "/index.html"
        return super().do_GET()


if __name__ == "__main__":
    ThreadingHTTPServer(("localhost", 4173), MemflixHandler).serve_forever()
