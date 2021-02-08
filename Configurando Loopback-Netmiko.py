from  netmiko  import  ConnectHandler
R1  = {
     'device_type' : 'cisco_ios' ,
     'host' : '192.168.81.101' ,
     'username' : 'roberto' ,
     'password' : 'cisco' ,
}

connect = ConnectHandler(**R1)

loopback13 = ['interface loopback 13']

configurar = connect.send_config_set(loopback13)
output = connect.send_command("show ip int brief")
print(output)