import os
OS_TYPE = os.name
count = '-n' if OS_TYPE == 'nt' else '-c'
from pythonping import ping
from getmac import get_mac_address as gma

ip_list=['192.168.0.129','192.168.16.5']

print("IP:",ip_list[0],"MAC ADDRESS:",gma(ip='192.168.0.1'))
print("IP:",ip_list[1],"MAC ADDRESS:",gma(ip='192.168.16.5'))

def ping_device(ip_list):
    for ip in ip_list:
        response = os.popen(f"ping {ip} {count} 1").read()
        print(ping(ip,verbose=True))
        if "Received = 1" and "Approximate" in response:
            print(f"UP {ip} Ping Successful")           
        else:
            print(f"Down {ip} Ping Unsuccessful")


if __name__ == "__main__":
    ping_device(ip_list)
