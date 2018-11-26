#!/usr/bin/python3.6
#MoulesFrites
#26/11/2018
#Active/desactive le forward sur centos

import subprocess
import sys

def exeBash(bash_Command):
	output = subprocess.check_output(['bash','-c', bash_Command])


if len(sys.argv) < 2:
	print('Use -a for activate or -d to disable')
elif sys.argv[1] == "-a":
	bashCommand = "echo '1' > /proc/sys/net/ipv4/ip_forward"
	exeBash(bashCommand)
	bashCommand = "iptables -F | iptables -X | iptables -t filter -A FORWARD -i enp0s9 -o enp0s3 -j ACCEPT | iptables -t filter -A FORWARD -i enp0s3 -o enp0s9 -j ACCEPT | iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE"
	exeBash(bashCommand)
elif sys.argv[1] == "-d":
	bashCommand = "echo '0' > /proc/sys/net/ipv4/ip_forward"
	exeBash(bashCommand)
	bashCommand = "iptables -F | iptables -X"
	exeBash(bashCommand)

