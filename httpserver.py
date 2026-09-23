import socket
import time
import signal
import traceback
from datetime import date
import os



def main():

    server = create_connection(port = 8080)

    while True:
        # 1. Wait for the browser to send a HTTP Request
        connection_to_browser = accept_browser_connection_to(server)

        # 2. Read the HTTP Request from the browser
        reader_from_browser = connection_to_browser.makefile(mode='rb')
        try:
            request_line = reader_from_browser.readline().decode("utf-8") # decode converts from bytes to text
            print()
            print('Request:')
            print(request_line)
        except Exception as e:
            print("Error while reading HTTP Request:", e)
            traceback.print_exc() # Print what line the server crashed on.
            shutdown_connection(connection_to_browser)
            continue

        # 3. Write the HTTP Response back to the browser
        writer_to_browser = connection_to_browser.makefile(mode='wb')
        try:
            # TODO: read "Hello, World!" from an HTML file instead of this encoded string.
            
            filename = get_requested_filename(request_line)

            if(filename == "./public/shutdown.html"):
                print("Server Shutting Down")
                shutdown_connection(connection_to_browser)
                exit(0)
                
            content = get_file_type(filename)

            with open(filename,"rb") as file:
                file_contents = file.read()

            file.closed
            response_body = file_contents

            content_type = get_content_type(content)+'; charset=utf-8'

            response_headers = "\r\n".join([
                'HTTP/1.1 200 OK',
                f'Content-Type: {content_type}',
                f'Content-length: {len(response_body)}',
                'Connection: close',
                '\r\n'
            ]).encode("utf-8") # encode converts strings to raw bytes

            # These lines just PRINT the HTTP Response to your Terminal.
            print()
            print('Response headers:')
            print(response_headers)
            print()
            print('Response body:')
            print(response_body)
            print()

            # These lines do the real work; they WRITE the HTTP Response to the Browser.
            writer_to_browser.write(response_headers)
            writer_to_browser.write(response_body)
            writer_to_browser.flush()
        except Exception as e:
            print("Error while writing HTTP Response:", e)
            traceback.print_exc() # print what line the server crashed on
    
        shutdown_connection(connection_to_browser)

def get_requested_filename(request_line):
    Str_arr = request_line.split(" ")

    
    return "./public"+Str_arr[1]

def get_file_type(filename):
    
    if(filename.endswith('html')):
        return "html"
    
    elif (filename.endswith('jpeg')):
        return "jpeg"
    
    elif(filename.endswith('png')):
        return "png"

    elif(filename.endswith('ico')):
        return "ico"
    
    elif(filename.endswith('js')):
            return "js"
    
    elif(filename.endswith('css')):
                return "css"

def get_content_type(content):
    if (content == 'png'):
        return 'image/png'
    
    elif(content == 'jpeg'):
        return 'image/jpeg'
    
    elif(content == 'html'):
        return 'text/html'
    
    elif(content == 'ico'):
            return 'image/x-icon'
    
    elif(content == 'js'):
            return 'text/javascript'
    elif(content == 'css'):
            return 'text/css'
    
    
    

# Don't worry about the details of the rest of the code below.
# It is VERY low-level code for creating the underlying connection to the browser.

def create_connection(port):
    addr = ("", port)  # "" = all network adapters; usually what you want.
    server = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True) # prevent rare IPV6 softlock on localhost connections
    server.settimeout(2)
    print(f'Server started on port {port}. Try: http://localhost:{port}/bad-example.html')
    return server

def accept_browser_connection_to(server):
    while True:
        try:
            (conn, address) = server.accept()
            conn.settimeout(2)
            return conn
        except socket.timeout:
            print(".", end="", flush=True)
        except KeyboardInterrupt:
            exit(0)

def shutdown_connection(connection_to_browser):
    connection_to_browser.shutdown(socket.SHUT_RDWR)
    connection_to_browser.close()


if __name__ == "__main__":
    print()
    main()

