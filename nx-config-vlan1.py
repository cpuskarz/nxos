#!/usr/bin/python

import requests
import json

"""
Modify these please
"""
url='http://10.91.86.244/ins'
switchuser='admin'
switchpassword='letmein'

inp_vlan = raw_input("Enter a vlan to create, such as - 'vlan 4': ")

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": inp_vlan,
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()