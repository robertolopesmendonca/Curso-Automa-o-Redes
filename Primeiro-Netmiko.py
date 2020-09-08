from  netmiko  import  ConnectHandler
R1  = {
     'device_type' : 'cisco_ios' ,
     'host' : '192.168.81.101' ,
     'username' : 'roberto' ,
     'password' : 'cisco' ,
}

connect = ConnectHandler(**R1)
output = connect.send_command("show ip int brief")
print(output)