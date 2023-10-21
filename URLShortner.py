import http.server
from http.server import BaseHTTPRequestHandler
import socketserver
from http.cookies import SimpleCookie
from urllib.parse import parse_qsl, urlparse

PORT = 8000
HOST = "localhost"

class MyHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)
    def query_data(self):
        return dict(parse_qsl(self.url.query))
    def post_data(self):
        content_length = int(self.headers.get("Content-Length",0))
        return self.rfile.read(content_length)
    def form_data(self):
        return dict(parse_qsl(self.post_data.decode("utf-8")))
    def do_GET(self):
        self.send_response(302)
        query = self.query_data()
        short_code = query["short_code"]
        webpage = ""
        self.send_header("Location", webpage)
        self.end_headers()
        
    def do_post(self):
        pass

Handler = MyHandler()

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()