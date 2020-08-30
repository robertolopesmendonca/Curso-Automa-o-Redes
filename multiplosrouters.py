import getpass
import telnetlib

HOST = "localhost"
user = input("Entre com seu usuário: ")
password = getpass.getpass()

lista_routers = open ('routers-ip') 

for ip in lista_routers:
    ip = ip.strip()
    print('Estamos configurando o Roteador ' + (ip))
    HOST = ip
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"conf t\n")
    for interface_loopback in range(4):
        tn.write(b"interface loopback " + str(interface_loopback).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")


    print(tn.read_all().decode('ascii'))

