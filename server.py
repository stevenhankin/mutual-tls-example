import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl
from OpenSSL import crypto

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        # Accessing client certificate details
        
        client_cert = self.connection.getpeercert(binary_form=True)

        # Check if SSL/TLS context is available
        # if hasattr(self.connection, "context"):
        #     client_cert = self.connection.context.getpeercert(binary_form=True)
        # else:
        #     client_cert = self.connection.getpeercert(binary_form=True)

        # client_cert = self.connection.getpeercert(binary_form=True)
        print(client_cert)
        x509 = crypto.load_certificate(crypto.FILETYPE_ASN1, client_cert)

        # Extracting client certificate details
        subject = x509.get_subject()
        issuer = x509.get_issuer()
        common_name = subject.commonName
        organization = subject.organizationName

        print("Client Certificate Details:")
        print(f"Common Name: {common_name}")
        print(f"Issuer: {issuer.commonName}")
        print(f"Organization: {organization}")


        print(self.headers)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, client! This is the server.")

def run_server():
    host = "127.0.0.1"
    port = 12345

    server = HTTPServer((host, port), MyHandler)

    # Create an SSL context
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile="server-cert.pem", keyfile="server-key.pem")
    ssl_context.verify_mode = ssl.CERT_REQUIRED


    # Wrap the server socket in SSL/TLS
    # server.socket = ssl.wrap_socket(server.socket, certfile="server-cert.pem", keyfile="server-key.pem", server_side=True, ssl_version=ssl.PROTOCOL_TLSv1_2)
    server.socket = ssl_context.wrap_socket(server.socket, server_side=True)


    # Request a client certificate
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    # server.socket.bind((host, port))
    server.socket.listen(1)

    print(f"Server listening on {host}:{port}")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
