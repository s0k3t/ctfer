import requests
import iptools
import socket
import nmap
from urllib import parse
from pyfiglet import Figlet

f=Figlet(font='digital')  # for other fonts, info: http://www.figlet.org/examples.html
print(f.renderText('CTFer'))

def nmap_url():
    link = input("\nintroduce the full url: ")
    if not link.startswith('http'):
        print("The link must start with a scheme(http(s)://). Try again!\n")
        class_instance.choose()
    else:
        print('')
        req = requests.get(link)
        print("Headers:\n\n", req.headers, '\n')

        h_name = parse.urlsplit(link)
        get_ip =socket.gethostbyname(h_name.netloc)

        print(f"The IP address of your url is: {get_ip}\n")

        port =  input("Introduce your port range(p-p): ")
        nm_arg = input("Introduce your favorite nmap command: ")
        print('')
        print("Please wait for the nmap scan results.\n")

        nm = nmap.PortScanner()
        nm.scan(get_ip, port, arguments=nm_arg) # ip, port range, nmap_arguments
        print("Command line used: ", nm.command_line(), "\n")
        print(nm.csv())


def nmap_ip():
    ip = input("\nIntroduce the IP address: ")
    if iptools.ipv4.validate_ip(ip) is True:
        print('')
        port = input("Introduce your port range(p-p): ")
        nm_arg = input("Introduce your favorite nmap command: ")
        print('')
        print("Please wait for the nmap scan result.\n")

        nm = nmap.PortScanner()
        nm.scan(ip, port, arguments=nm_arg) # ip, port range, nmap_arguments
        print("Command line used: ", nm.command_line(), "\n")
        print(nm.csv())

    else:
        print("The ip address is not valid. Try again!\n")
        class_instance.choose()

class Again:
    def choose(self):
        return choice()

class_instance = Again()

def choice():
    choice = input('What do you want to nmap?\nFull url: 1\nIP address: 2\n(q)uit\n\nSelect: ')

    if choice == '1':
        nmap_url()
    elif choice == '2':
        nmap_ip()
    elif choice == 'q':
        exit()
    else:
        print("Choose between 1 or 2 or (q)uit, try again!\n")
        class_instance.choose()
        


if __name__=="__main__":
    choice()
