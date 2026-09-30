from ipaddress import ip_network

a = ip_network("146.180.173.153/255.192.0.0", strict=False)

h = a.broadcast_address
h = str(h)
print(sum(map(int, h.split('.'))) - 1)
