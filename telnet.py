import getpass
import telnetlib

HOST = "192.168.91.100"
user = input("Entre com seu usuário: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"interface loopback 0\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

