#!/opt/homebrew/bin/python3.9
import ipaddress

netip0 = '172.16.98.0/24'
netip1 = '172.16.99.0/24'
netip2 = '172.16.108.254/32'
netip3 = '172.16.109.0/26'
netip4 = '172.16.109.64/26'
netip5 = '172.16.109.128/26'
netip6 = '10.44.0.0/16'
netip7 = '10.45.0.0/16'
netip8 = '10.46.0.0/16'

net0 = ipaddress.ip_network(netip0)
net1 = ipaddress.ip_network(netip1)
net2 = ipaddress.ip_network(netip2)
net3 = ipaddress.ip_network(netip3)
net4 = ipaddress.ip_network(netip4)
net5 = ipaddress.ip_network(netip5)
net6 = ipaddress.ip_network(netip6)
net7 = ipaddress.ip_network(netip7)
net8 = ipaddress.ip_network(netip8)

inlst1 = [net0, net1]
inlst2 = [net2, net3, net4, net5]
inlst3 = [net6, net7, net8]


def test1(netlst, num):
    subnet_lst = []
    for i in netlst:
        if i.prefixlen is int('32'):
            subnet_lst.append(i)
        else:
            snet = i.supernet(prefixlen_diff=1)
            subnet_lst.append(snet)
    num = str(num)
    netlst = set(netlst)
    subnet_lst = set(subnet_lst)

    print(f'{num} Input:\t', ', '.join(map(str, netlst)))
    print(f'   Output:\t', ', '.join(map(str, subnet_lst)))

def supernet_calculator(prefixes: list[str]) -> list[str]:
    pass

test1(inlst1, '1.')
test1(inlst2, '2.')
test1(inlst3, '3.')
