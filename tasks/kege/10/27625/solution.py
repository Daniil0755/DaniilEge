from ipaddress import ip_network

a = ip_network("172.16.96.0/255.255.224.0", strict=False)
c = 1
g = a.hosts()
for i in g:
    d = (str(f"{int(i):032b}")).count("1")
    if d % 2 == 0:
        c += 1
print(c)
