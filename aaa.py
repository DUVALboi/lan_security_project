radius_server_ip = '192.168.40.100' 
radius_key = 'MyRadiusKey' 

aaa_config = [
    'aaa new-model',
    'aaa group server radius AAA-Servers',
    f'radius-server host {radius_server_ip} auth-port 1812 acct-port 1813 key {radius_key}',
    'aaa authentication login default group radius local',
    'aaa authorization exec default group radius local',
    'aaa accounting exec default start-stop group radius',
    'aaa accounting network default start-stop group radius' ]
