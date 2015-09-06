#! /usr/bin/env python

import os.path
import csv
import json
from optparse import OptionParser

supported_extensions = [ ".csv", ".json", ".xml" ]

def read_file(filename):
    try:
        extension = os.path.splitext(filename)[1]
        if extension not in supported_extensions:
            raise Exception("Not a supported extension")

        f = open(filename, 'r')
        if extension == ".csv" :
            csv_r = csv.DictReader(f)
            header = csv_r.fieldnames
            g = lambda d: { d.keys()[0].strip(): d.values()[0].strip(),
                            d.keys()[1].strip(): d.values()[1].strip() }
            data = map(g, csv_r)
            # data = [ ix for ix in csv_r]
        elif extension == ".json":
            pass
        else: # extension == ".xml":
            raise Exception("XML not supported at this time")
            pass
    except Exception, e:
        raise Exception(str(e))
    else:       # this is else for exception (if there is no exception)
        f.close()
    finally:    # this will always execute
        pass

    return header, data

def parse_args(args):
    parser = OptionParser()
    parser.add_option("-i", "--ifile", type="string", action="store", 
        dest="iname", help="report file in csv/xml/json format")
    parser.add_option("-o", "--ofile", action="store", dest="oname", 
        help="output file name")
    parser.add_option("-t", "--type", action="store", dest="type", 
        default="png", help="export type svg, png, jpg, cdata")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
        help="print verbose debugging")
    parser.add_option("-q", "--quiet",  action="store_false", dest="verbose",
        default=False, help="no output be quiet")
    return parser.parse_args(args)

def main(args = None):
    (options, args) = parse_args(args)

    if options.verbose:
        print "iname: %s" % options.iname
        print "oname: %s" % options.oname
        print "type : %s" % options.type
        print "args: %s" % args
        print "options: %s" % options

    if options.iname is None:
        parse_args(['-h'])
        exit(2)

    # origdata = read_file(options.iname)
    # header = origdata[0]
    # data   = origdata[1:]
    try:
        header, data = read_file(options.iname)
        # print header
        data = json.dumps(data)
        print data
        data = json.loads(data)
        print "keys: " 
        x_axis = map(lambda d: d.values()[0], data)
        y_axis = map(lambda d: d.values()[1], data)
        print x_axis
        print y_axis
        
        # print json.dumps(data)
    except Exception, e:
        print str(e)

    # return 
    
if __name__ == "__main__" :
    main()
 

