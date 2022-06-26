from ipaddress import IPv4Address

# ip1 = 2149583361 -> "128.32.10.1"
# ip2 = 32         -> "0.0.0.32"
# ip3 = 0          -> "0.0.0.0"

def int32_to_ip(int32):
    s = IPv4Address(int32)
    return str(s)

if __name__ == '__main__':
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"



