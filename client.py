import http.client
import ssl

def run_client():
    host = "127.0.0.1"
    port = 12345

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.load_cert_chain(certfile="client-cert.pem", keyfile="client-key.pem")
    # ssl_context.load_verify_locations(cafile="server-cert.pem")
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Use HTTPSConnection with the SSLContext
    client = http.client.HTTPSConnection(host, port, context=ssl_context)

    try:
        # Send a GET request to the server
        client.request("GET", "/")

        # Get and print the response from the server
        response = client.getresponse()
        print(f"Response from the server:\n{response.read().decode('utf-8')}")
    finally:
        # Close the connection in a finally block to ensure it's closed regardless of exceptions
        client.close()

if __name__ == "__main__":
    run_client()
