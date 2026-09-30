from ipaddress import ip_network

a = ip_network("111.222.0.124/255.255.224.0", strict=False)
c = ''
g = a.hosts()
for i in g:
    d = (str(f"{int(i):032b}")).count("1")
    f = (str(f"{int(i):032b}")).count("0")
    if (d * f) % 2 == 1:
        c = max(c, str(i))
print(sum(map(int, c.split("."))))
print(sum(map(int, str(a.broadcast_address).split("."))))

