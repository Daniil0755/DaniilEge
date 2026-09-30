from ipaddress import ip_network

a = ip_network("172.16.160.0/255.255.240.0", strict=False)
c = 0
g = a.hosts()
for i in g:
    d = (str(f"{int(i):032b}")).count("1")
    if d % 2 == 0:
        c += 1
print(c)