import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer

CERTFILE = "./localhost.pem"

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/get_test":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header("Cache-Control", "no-store, must-revalidate")
            self.end_headers()
            self.wfile.write(b'Custom Response2!')
        else:
        # 301 Moved Permanentlyのレスポンスを返す
            self.send_response(301)
            self.send_header("Location", "https://www.google.com/maps")
            self.end_headers()

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