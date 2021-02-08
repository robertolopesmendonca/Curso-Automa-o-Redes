from napalm import get_network_driver
import json
import napalm.junos

driver = get_network_driver("ios")

device = driver(
        hostname="192.168.81.101",
        username="roberto",
        password="cisco",
        optional_args={"port": 22},
    )
device.open()

output = device.get_bgp_neighbors()
print(json.dumps(output, indent=4))

print('Configurando BGP no Router... Aguarde...')

device.load_merge_candidate(filename='r1-config.cfg')
device.commit_config()
device.close()

print('Configuração Efetuada com Sucesso')