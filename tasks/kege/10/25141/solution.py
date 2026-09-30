from ipaddress import ip_network

a = ip_network("46.29.170.214/255.255.128.0", strict=False)
c = ''
g = a.hosts()
for i in g:
    d = list(map(int,str(i).split(".")))
    if d[2] == sum(d)-d[2]:
        c = max(c,str(i))
print(c)