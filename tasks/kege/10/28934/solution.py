from ipaddress import ip_network

a = ip_network("191.89.109.206/255.255.224.0", strict=False)

h = a.broadcast_address
h = str(h)
print(sum(map(int, h.split('.'))) - 1)
