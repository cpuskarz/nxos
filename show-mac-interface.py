import requests
import json

"""
Modify these please
"""
url='http://10.91.86.244/ins'
switchuser='admin'
switchpassword='9letmein'

def getip():
    user_ip = raw_input("Enter IP address: ")
    #print "IP Address: " + user_ip
    return user_ip

# Enter show ip arp <ip address>
# find mac from response, save to a variable, then do
# show mac address-table <mac> to get interface/port, vlan and type
def iparp(ip):
    show_ip = "show ip arp " + ip
    iparp_myheaders={'content-type':'application/json'}
    iparp_payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": show_ip,
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(iparp_payload), headers=iparp_myheaders,auth=(switchuser,switchpassword)).json()

    find_mac =  response['ins_api']['outputs']['output']['body']['TABLE_vrf']['ROW_vrf']['TABLE_adj']['ROW_adj']['mac']
    intfout =  response['ins_api']['outputs']['output']['body']['TABLE_vrf']['ROW_vrf']['TABLE_adj']['ROW_adj']['intf-out']
    #print "MAC: " + find_mac + "   " + "Interface: " + intfout
    return (find_mac, intfout)


def macintf(my_mac):
    get_mac_intf = "show mac address-table address " + my_mac
    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": get_mac_intf,
        "output_format": "json"
      }
    }
    get_mac_response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    found_intf = get_mac_response['ins_api']['outputs']['output']['body']['TABLE_mac_address']['ROW_mac_address']['disp_port']
    found_vlan = get_mac_response['ins_api']['outputs']['output']['body']['TABLE_mac_address']['ROW_mac_address']['disp_vlan']
    #print "Interface: " + found_intf + "   " +  "VLAN: " + found_vlan
    return (found_intf, found_vlan)


def PrintVmInfo():
        col_widths = [20, 20, 20, 20, 20]
        template = ''
        for idx, width in enumerate(col_widths):
            template += '{%s:%s} ' % (idx, width)
        #print("")
        print ""
        print "[***  IP ARP TABLE INFO  ***]" + (' ' * 34) + "[***  MAC ADDRESS-TABLE INFO  ***]"
        print("_" * 60) + '   ' + ("_" * 39)
        print(template.format("IP ADDRESS", "MAC ADDRESS", "INTERFACE", "PORT", "VLAN"))
        fmt_string = []
        for i in range(0, len(col_widths)):
            fmt_string.append('-' * (col_widths[i] - 2))
        print(template.format(*fmt_string))




def main():
    ip = getip()
    my_mac, my_intf = iparp(ip)
    port, found_vlan = macintf(my_mac)
    PrintVmInfo()
    print '{:<21}'.format(ip) + '{:<21}'.format(my_mac) + '{:<21}'.format(my_intf) + '{:<21}'.format(port) + '{:<21}'.format(found_vlan)
    print ""


if __name__ == '__main__':
  main()

