#!/usr/bin/python

import requests
import json

# hard coded variables for dc build, replia of ansible dc build

"""
Modify these please
"""
url='http://10.91.86.244/ins'
switchuser='admin'
switchpassword='letmein'

# create vlans
print "Creating vlans..."
vlan_myheaders={'content-type':'application/json'}
vlan_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ; vlan 2-20,99 ; vlan 10 ;name test_segment ;vlan 20 ;name peer-keepalive ;vlan 99 ;name native",
    "output_format": "json"
  }
}
vlan_response = requests.post(url,data=json.dumps(vlan_payload), headers=vlan_myheaders,auth=(switchuser,switchpassword)).json()
print "vlan configuration done."



# Create Portchannels
print "Creating port-channels..."
po10_myheaders={'content-type':'application/json'}
po10_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ; interface port-channel 10 ; switchport mode trunk ;switchport trunk native vlan 99 ;switchport trunk allowed vlan 2-20",
    "output_format": "json"
  }
}
po10_response = requests.post(url,data=json.dumps(po10_payload), headers=po10_myheaders,auth=(switchuser,switchpassword)).json()

po11_myheaders={'content-type':'application/json'}
po11_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;interface port-channel 11 ;switchport mode trunk ;switchport trunk native vlan 99 ;switchport trunk allowed vlan 2-20",
    "output_format": "json"
  }
}
po11_response = requests.post(url,data=json.dumps(po11_payload), headers=po11_myheaders,auth=(switchuser,switchpassword)).json()
print "Port-channel configuration done"

# create L2 switchport configs
print "Creating L2 trunk switchports..."
trunks_myheaders={'content-type':'application/json'}
trunks_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ; interface Ethernet 1/2 ; switchport mode trunk ;switchport trunk native vlan 99 ;"
             "switchport trunk allowed vlan 2-20 ; channel-group 10 mode active ;no shut",
    "output_format": "json"
  }
}
trunk_response = requests.post(url,data=json.dumps(trunks_payload), headers=trunks_myheaders,auth=(switchuser,switchpassword)).json()


# create L2 for peer keepalive link
pka_myheaders={'content-type':'application/json'}
pka_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;interface Ethernet 2/12 ;switchport mode trunk ;switchport trunk native vlan 99 ;"
             "switchport trunk allowed vlan 20 ; channel-group 11 mode active ;no shut",
    "output_format": "json"
  }
}
pka_response = requests.post(url,data=json.dumps(pka_payload), headers=pka_myheaders,auth=(switchuser,switchpassword)).json()


# create logical interfaces
print "Creating logical interfaces..."
logicalint_myheaders={'content-type':'application/json'}
logicalint_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;interface vlan 10 ;interface vlan 20",
    "output_format": "json"
  }
}
logicalint_response = requests.post(url,data=json.dumps(logicalint_payload), headers=logicalint_myheaders,auth=(switchuser,switchpassword)).json()
print "Logical interfaces complete."


# create VRFs and assign to link interfaces
print "Creating vrfs..."
vrf_myheaders={'content-type':'application/json'}
vrf_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;vrf context keepalive ;interface vlan 20 ; vrf member keepalive",
    "output_format": "json"
  }
}
vrf_response = requests.post(url,data=json.dumps(vrf_payload), headers=vrf_myheaders,auth=(switchuser,switchpassword)).json()
print "VRFs completed..."

# assign ip addresses
print "Assigning IP addresses to logical interfaces..."

ip_myheaders={'content-type':'application/json'}
ip_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;interface vlan 10 ;ip address 10.10.1.2/24 ;interface vlan 20 ;ip add 10.20.1.2/24",
    "output_format": "json"
  }
}
ip_response = requests.post(url,data=json.dumps(ip_payload), headers=ip_myheaders,auth=(switchuser,switchpassword)).json()
print "Completed assigning of IP addresses."




# config HSRP
print "Configuring HSRP..."
hsrp10_myheaders={'content-type':'application/json'}
hsrp10_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;interface vlan 10 ;hsrp version 2 ;hsrp 10 ;  priority 120 ;  ip 10.10.1.1",
    "output_format": "json"
  }
}
hsrp10_response = requests.post(url,data=json.dumps(hsrp10_payload), headers=hsrp10_myheaders,auth=(switchuser,switchpassword)).json()

hsrp20_myheaders={'content-type':'application/json'}
hsrp20_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;interface vlan 20 ;hsrp version 2 ;hsrp 10 ;  priority 120 ;  ip 10.20.1.1",
    "output_format": "json"
  }
}
hsrp20_response = requests.post(url,data=json.dumps(hsrp20_payload), headers=hsrp20_myheaders,auth=(switchuser,switchpassword)).json()

print "Completed HSRP..."

######## STOP ################


# create vpc globals
print "Creating vpc global configuration..."
vpcg_myheaders={'content-type':'application/json'}
vpcg_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;vpc domain 100 ;role priority 1000 ;system-priority 2000 ;peer-keepalive destination 10.20.1.3 source 10.20.1.2 vrf keepalive",
    "output_format": "json"
  }
}
vpcg_response = requests.post(url,data=json.dumps(vpcg_payload), headers=vpcg_myheaders,auth=(switchuser,switchpassword)).json()
print "Completed vpc global configuration..."

# vpc portchannel configuration
print "Creating VPC Portchannel configuration..."
vpcpl_myheaders={'content-type':'application/json'}
vpcpl_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;interface port-channel 10 ;vpc peer-link",
    "output_format": "json"
  }
}
vpcpl_response = requests.post(url,data=json.dumps(vpcpl_payload), headers=vpcpl_myheaders,auth=(switchuser,switchpassword)).json()

vpc11_myheaders={'content-type':'application/json'}
vpc11_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;interface port-channel 11 ;vpc 11",
    "output_format": "json"
  }
}
vpc11_response = requests.post(url,data=json.dumps(vpc11_payload), headers=vpc11_myheaders,auth=(switchuser,switchpassword)).json()
print "Completed vpc configurations."

# save config
print "Saving configuration..."
save_myheaders={'content-type':'application/json'}
save_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "copy running-config startup-config",
    "output_format": "json"
  }
}
save_response = requests.post(url,data=json.dumps(save_payload), headers=save_myheaders,auth=(switchuser,switchpassword)).json()
