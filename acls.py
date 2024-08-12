acl_101 = [
    'access-list 101 permit ip 11.11.11.0 0.0.0.3 any',
    'access-list 101 permit ip 12.12.12.0 0.0.0.3 any',
    'access-list 101 deny ip any any log' ] 

acl_102 = [
    'access-list 102 permit tcp any any eq 80',
    'access-list 102 permit tcp any any eq 443',
    'access-list 102 permit udp any any eq 53',
    'access-list 102 deny ip any any log' ] 

acl_103 = [
    'access-list 103 permit ip 192.168.40.0 0.0.0.255 192.168.10.0 0.0.0.255',
    'access-list 103 permit ip 192.168.40.0 0.0.0.255 192.168.20.0 0.0.0.255',
    'access-list 103 permit ip 192.168.10.0 0.0.0.255 192.168.99.0 0.0.0.255',
    'access-list 103 permit ip 192.169.10.0 0.0.0.255 192.169.20.0 0.0.0.255',
    'access-list 103 permit ip 192.169.10.0 0.0.0.255 192.169.30.0 0.0.0.255',
    'access-list 103 deny ip any any log' ] 

acl_104 = [
    'access-list 104 permit ip 192.168.40.0 0.0.0.255 any',
    'access-list 104 permit ip 192.168.10.0 0.0.0.255 any',
    'access-list 104 permit ip 192.168.20.0 0.0.0.255 any',
    'access-list 104 permit ip 192.168.99.0 0.0.0.255 any',
    'access-list 104 permit ip 192.169.10.0 0.0.0.255 any',
    'access-list 104 permit ip 192.169.20.0 0.0.0.255 any',
    'access-list 104 permit ip 192.169.30.0 0.0.0.255 any',
    'access-list 104 permit ip 192.169.98.0 0.0.0.255 any',
    'access-list 104 deny ip any any log' ]
