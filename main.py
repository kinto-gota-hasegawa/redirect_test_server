import ssl
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

CERTFILE = "./localhost.pem"

with open("index.html") as f:
    index_file = f.read()

with open("redirect_url.txt") as f:
    first_line = f.readline().strip()

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/button":
            # 301 Moved Permanentlyのレスポンスを返す
            # https://developer.mozilla.org/ja/docs/Web/HTTP/Status/301
            self.send_response(301, "Moved Permanently")
            self.send_header("Location", first_line)
            self.end_headers()
        else:
            enc = sys.getfilesystemencoding()
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=%s" % enc)
            self.send_header("Cache-Control", "no-store, must-revalidate")
            self.end_headers()
            self.wfile.write(index_file.encode(enc, 'surrogateescape'))


def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(CERTFILE)
    # server_address = ('', port)
    with HTTPServer(("", 8000), MyHandler) as httpd:
        print("serving at address", httpd.server_address, "using cert file", CERTFILE)
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        httpd.serve_forever()
    

if __name__ == '__main__':
    run()