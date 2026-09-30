from ipaddress import ip_network

a = ip_network("190.202.83.62/255.255.252.0", strict=False)
c=a.broadcast_address
print(sum(map(int,str(c).split('.'))))
