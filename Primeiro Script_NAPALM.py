from napalm import get_network_driver

driver = get_network_driver('ios')
device =  driver(
     hostname="192.168.81.101",
     username="roberto",
     password="cisco",
     optional_args={"port":22},
   )
device.open()

output = device.get_interfaces()
print(output)