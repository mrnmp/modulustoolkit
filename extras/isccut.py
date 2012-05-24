#!/usr/bin/env python

import os
import sys
import math
import pickle
import re
import getopt
import numpy as np
import pylab as pl
from scipy.odr import RealData, ODR
from scipy.odr.models import unilinear
#

def usage():
    print 'bleh'

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:l:u:", ["help", "input=", "output=","lowerleft","upperright"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    input  = None
    ll_lon = 0.
    ll_lat = -90.
    ur_lon = 360.
    ur_lat = 90.
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            return(0)
        elif o in ("-i", "--input"):
            print o,a
            infile = a
        elif o in ("-o", "--output"):
            outfile = a
        elif o in ("-l", "--lowerleft"):
            tmp = a.split(',')
            try:
                ll_lon = float(tmp[0])
                ll_lat = float(tmp[1])
            except (IndexError,TypeError):
                usage()
        elif o in ("-u", "--upperright"):
            tmp = a.split(',')
            try:
                ur_lon = float(tmp[0])
                ur_lat = float(tmp[1])
            except (IndexError,TypeError):
                usage()
        else:
            assert False, "unhandled option"
    if len(args) != 0:
        usage()
        return(-1)
    # Finished processing commabd line options, now for the real work
    events = readisc_text(infile)
    #
    auths = {}
    authnos = {}
    events_out = {}
    for event in events.keys():
        for auth in events[event].keys():
            (date,time,hypo,mags) = events[event][auth]
            [lon,lat] = hypo[0:2]
            if lon < ll_lon or lon > ur_lon or lat < ll_lat or lat > ur_lat:
                continue
            events_out[event] = events[event]
            if auths.has_key(auth):
                magnos = auths[auth]
                authnos[auth] += 1
            else:
                magnos = {}
                authnos[auth] = 1
            for magtype in mags.keys():
                if magnos.has_key(magtype):
                    magnos[magtype] += 1
                else:
                    magnos[magtype] = 1
            auths[auth] = magnos
    for auth in auths.keys():
        if len(auths[auth]) > 0: 
            print '%d events measured by %s' % (authnos[auth],auth)
        for magtype in auths[auth].keys():
            print '\t%s   %d' % (magtype,auths[auth][magtype])
    output = open(outfile,'wb')
    ##pickle.dump(events_out,output)
    print >>output, events_out
    output.close()
    print 'Total %d events after cut' % len(events_out)
    print 'Events dictionary saved in %s' % outfile


def readisc_text(file):
    lines = open(file,'r').readlines()
    events = {}
    auths  = {}
    iscid  = ''
    for line in lines:
        flds = line.split()
        if line.startswith('Event'): 
            if len(iscid) == 0: 
                iscid = flds[1]
            else:
                if events.has_key(iscid):
                    print 'Duplicate event %s' % iscid
                else: 
                    events[iscid] = auths
                auths = {}
                iscid = flds[1]
            continue
# New hypocenter
        if re.match('\d\d\d\d/\d\d/\d\d',line) != None:
            date = flds[0]
            time = flds[1]
            lon  = float(line[45:54])
            lat  = float(line[36:44])
            if line[71:76] != '     ':
                dep = float(line[71:76])
                hypo = [lon,lat,dep]
            else:
                hypo = [lon,lat]
            auth = line[118:124].strip()
            auths[auth] = (date,time,hypo,{})
        elif line[78:82] == 'HRVD' or line[78:82] == 'GCMT':
            iexp = int(flds[1])
            m0   = float(flds[2])
            mag  = 2.*math.log10(m0*math.pow(10.,7+iexp))/3. - 10.7
            (date,time,hypo,mags) = auths[auth]
            mags['Mw'] = mag
            auths[auth] =  (date,time,hypo,mags)
        elif (line.startswith('M') or line.startswith('m')) and not line.startswith('Magnitude'):
            magauth = line[20:26].strip()
            magtype = flds[0]
            if magtype == 'MW': magtype = 'Mw'
            mag = float(flds[1])
            for auth in auths.keys():
                if auth == magauth or auth == 'GUTE' and magauth == 'PAS':
                    (date,time,hypo,mags) = auths[auth]
                    mags[magtype] = mag
                    auths[auth] =  (date,time,hypo,mags)

    print '%d events found' % len(events)
    return events
#
###
if __name__ == "__main__":
    sys.exit(main())
