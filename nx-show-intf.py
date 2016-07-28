import requests
import json

"""
Modify these please
"""
url = 'http://10.91.86.244/ins'
switchuser = 'admin'
switchpassword = 'letmein'

show_int = raw_input("Enter interface to view, such as -  show int eth1/1: ")

myheaders = {'content-type': 'application/json'}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": show_int,
        "output_format": "json"
    }
}
response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword)).json()

# print response


find_intf = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['interface']
find_state = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['state']
find_mac = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_hw_addr']
find_mtu = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_mtu']
find_bw = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_bw']
find_speed = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_speed']
find_runts = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_runts']
find_giants = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_giants']
find_crc = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_crc']
find_inerr = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_inerr']
find_nobuf = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_nobuf']

print "*" * 25
print "Interface: " + find_intf
print "*" * 25
print "State: " + find_state
print "MAC: " + find_mac
print "MTU: " + find_mtu
print "BW: " , find_bw
print "SPEED: " + find_speed
print "RUNTS: " , find_runts
print "GIANTS: " ,  find_giants
print "CRC: " + find_crc
print "INGRESS ERRORS: " + find_inerr
print "NO BUFFERS: " ,  find_nobuf



