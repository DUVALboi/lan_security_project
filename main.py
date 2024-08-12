from devices import devices 
from configs import toisp_router_config 
from aaa import aaa_config 
from acls import acl_101, acl_102, acl_103, acl_104 
from apply_config import configure_device 

if __name__ == '__main__':
    for device in devices:
        if device['ip'] in ['11.11.11.2', '12.12.12.2']: # ToISP_Router
            configure_device(device, device_specific_config=toisp_router_config)
        else:
            configure_device(device, additional_configs=[aaa_config, acl_101, acl_102, acl_103, acl_104])
