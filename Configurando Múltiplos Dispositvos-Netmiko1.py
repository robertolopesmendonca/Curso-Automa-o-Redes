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

with open('Config_Router_File') as file:
     config_line = file.read().splitlines()

lista_routers = [R1, R2, R3]

for routers in lista_routers:
     connect = ConnectHandler(**routers)
     configure = connect.send_config_set(config_line)
     print(configure)
     connect.disconnect()

print('Script Finalizado !! Chupa que é de UVA !!')




