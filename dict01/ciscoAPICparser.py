#!/usr/bin/env python3
"""parsing json"""
import json # working with json data

def main():
	with open("ciscoAPIC.json", "r") as jsono file:
	fog = jsono.load(jsonofile)
	print("The number of instances: ", len(fog['imdata']))
	for instances in fog['imdata']:
		print("Firmware version running - ", instances.get('firmwareCtrlrRunning').get('attributes'))

main()