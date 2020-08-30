import getpass
import telnetlib

HOST = "192.168.15.112"
user = input("Entre com seu usuário: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")

for vlans in range (10,16):
    tn.write(b"vlan " + str(vlans).encode('ascii') + b"\n")
    tn.write(b"name Site_ " + str(vlans).encode('ascii') + b"\n")


tn.write(b"end\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))

