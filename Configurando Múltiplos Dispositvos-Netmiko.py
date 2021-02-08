from  netmiko  import  ConnectHandler
R1  = {
     'device_type' : 'cisco_ios' ,
     'host' : '192.168.81.101' ,
     'username' : 'roberto' ,
     'password' : 'cisco' ,
}

R2  = {
     'device_type' : 'cisco_ios' ,
     'host' : '192.168.81.102' ,
     'username' : 'roberto' ,
     'password' : 'cisco' ,
}

R3  = {
     'device_type' : 'cisco_ios' ,
     'host' : '192.168.81.103' ,
     'username' : 'roberto' ,
     'password' : 'cisco' ,
}

for routers in (R1,R2,R3):
     connect = ConnectHandler(**routers)
     print(connect.find_prompt())
     connect.disconnect()

print('Script Finalizado !!')




