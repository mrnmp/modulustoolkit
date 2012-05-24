#!/usr/bin/env python
"""
        begin                : 2012-04-03
        copyright            : (C) 2012 by nimal mariampillai

"""
import pickle
import sys 

def read_dict(filename):
	"""
	reads seismic catalog object extracted by isccut.py
	generates space seperated fileds
	"""
	pkl_file = open(filename,'rb')
	event_dict = pickle.load(pkl_file)
	pkl_file.close()
	rec_count = 1
	magTypes = []

	#for agency_dict in event_dict.values():
	for events_key in event_dict.keys():
		agency_dict = event_dict[events_key]
		for agency in agency_dict.keys():
			(date,time,hypo,mags) = agency_dict[agency]
			if len(hypo) > 2:
				[lat,lon,dep] = hypo[0:3]
			else:
				[lat,lon] = hypo[0:2]
			print   "{0:<10} {1:10} {2:11} {3:<6} {4:<10} {5:<10} {6:<6} {7:8} ".format(rec_count, date, time, agency,lat, lon, dep, events_key),
			if mags > 0:
				mag = []
				v1 = "";v2 = "";v3 = "";v4 = "";v5 = "";v6 = "";v7 = "";v8 = "";v9 = "";v10 = "";v11 = "";v12 = "";v13 = "";v14 = "";v15 = "";v16 = "";v17 = "";v18 = "";v19 = "";v20 = ""
				for key, value in mags.items():
					#print key,":", value
					if key not in magTypes:
						magTypes.append(key)
					#print " {0:10}".format(mags[mag]),
					if key == 'Mw' :
						v1 = value
					elif key == 'M' :
						v2 = value
					elif key == 'MB' :
						v3 = value
					elif key == 'ME' :
						v4 = value
					elif key == 'ML' :
						v5 = value
					elif key == 'MLv' :
						v6 = value
					elif key == 'MS' :
						v7 = value
					elif key == 'Mb' :
						v8 = value
					elif key == 'Mjma' :
						v9 = value
					elif key == 'Ms' :
						v10 = value
					elif key == 'Ms1' :
						v11 = value
					elif key == 'Ms7' :
						v12 = value
					elif key == 'Msz' :
						v13 = value
					elif key == 'Mwp' :
						v14 = value
					elif key == 'mB' :
						v15 = value
					elif key == 'mb' :
						v16 = value
					elif key == 'mb1' :
						v17 = value
					elif key == 'mb1mx' :
						v18 = value
					elif key == 'mbtmp' :
						v19 = value
					elif key == 'mslmx' :
						v20 = value
					else :
						#print " not matched value",
						pass
				print "{0:<5} {1:<5} {2:<5} {3:<5} {4:<5} {5:<5} {6:<5} {7:<5} {8:<5} {9:<5} {10:<5} {11:<5} {12:<5} {13:<5} {14:<5} {15:<5} {16:<5} {17:<5} {18:<5} {19:<5}".format(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20),
			print 
			rec_count = rec_count + 1



def main():
	read_dict(sys.argv[1])

if __name__ == '__main__':
	main()
