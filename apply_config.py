import netmiko 
from netmiko import ConnectHandler 

def apply_config(device, config_commands):
    connection = ConnectHandler(**device)
    connection.enable()
    output = connection.send_config_set(config_commands)
    connection.save_config()
    connection.disconnect()
    return output 

def configure_device(device, device_specific_config=None, additional_configs=None):
    print(f"Connecting to device: {device['ip']}")
    if device_specific_config:
        output = apply_config(device, device_specific_config)
        print(f"Device-specific configuration applied to {device['ip']}:\n{output}")
    if additional_configs:
        for config in additional_configs:
            output = apply_config(device, config)
            print(f"Additional configuration applied to {device['ip']}:\n{output}")
    
    print(f"Configuration completed for {device['ip']}.\n")
