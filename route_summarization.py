
"""
Link to the problem statement
https://py.checkio.org/mission/ip-network-route-summarization/
"""
​
​
def binary_ip(ip):
    'gives binary format for an ip address'
    return ".".join([format(int(oc), '08b') for oc in ip.split('.')])
​
​
def int_ip(binary_ip):
    'takes an ip address in binary format and returns its regular equivalent'
    return ".".join([str(int(oc, 2)) for oc in binary_ip.split('.')])
​
​
def longest_common_prefix(ips):
    'given a list of strings, finds out the longest common prefix'
    lcp = ips[0]
    for ip in ips[1:]:
        start = 0
        while start < min(len(lcp), len(ip)):
            if ip[start] != lcp[start]:
                break
            start += 1
        lcp = lcp[:start]
    return lcp
​
​
def generate_ip_from_lcp(lcp):
    nw_ip_binary = format(lcp, '0<35')
    chars = list(nw_ip_binary)
    chars[8] = chars[17] = chars[26] = '.'
    nw_ip_binary = ''.join(chars)
    return int_ip(nw_ip_binary)
​
​
def subnet_mask_from_lcp(lcp):
    return len(lcp) - lcp.count('.')
​
​
def checkio(data):
​
    binary_data = [binary_ip(ip) for ip in data]
    lcp = longest_common_prefix(binary_data)
    return "{}/{}".format(generate_ip_from_lcp(lcp), subnet_mask_from_lcp(lcp))
​
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0