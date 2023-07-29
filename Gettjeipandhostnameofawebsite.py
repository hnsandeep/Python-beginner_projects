import socket
def get_hostname_IP():
    hostname = input("Pleasse enter website addresss(URL):")
    try:
        print(f'Hostman: {hostname}')
        print(f'IP:{socket.gethostname(hostnme)}')
    except socket.gaierror as error:
        print(f'Invalid Hostname, error raised is {error}')
# `get_hostname_IP()` is a Python function that prompts the user to enter a website address (URL) and
# then attempts to retrieve the hostname and IP address of the website using the `socket` module. If
# the hostname is valid, the function prints the hostname and IP address. If the hostname is invalid,
# the function prints an error message indicating that the hostname is invalid.
get_hostname_IP()