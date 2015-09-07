#! /usr/bin/env python

import os.path
import csv
import json
import pygal
from optparse import OptionParser
import code

input_extns = [ ".csv", ".json", ".xml" ]
output_extns = [ ".png", ".svg" ]

def read_file(filename):
    try:
        extension = os.path.splitext(filename)[1]
        if extension not in input_extns:
            raise Exception("Not a supported input extension")

        f = open(filename, 'r')
        if extension == ".csv" :
            csv_r = csv.reader(f)
            header = next(csv_r)
            data = map(lambda lst: dict(zip(header, lst)), csv_r)
        elif extension == ".json":
            data = json.load(f)
            header = sorted(data[0].keys())
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
        default="xb-py", help="output file name")
    parser.add_option("-t", "--type", action="store", dest="type", 
        default="svg", help="export type svg, png, jpg, cdata")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
        help="print verbose debugging")
    parser.add_option("-q", "--quiet",  action="store_false", dest="verbose",
        default=False, help="no output be quiet")
    return parser.parse_args(args)

def create_output(chart, filename):
    extension = os.path.splitext(filename)[1]
    try:
        if extension not in output_extns:
            raise Exception("Not a supported output extension")

        if extension == ".png" :
            chart.render_to_png(filename)

    except Exception, e:
        raise Exception(str(e))
    else:       # this is else for exception (if there is no exception)
        pass
    finally:    # this will always execute
        pass
    return

def main(args = None):
    (options, args) = parse_args(args)

    outfile = options.oname + '.' + options.type
    if options.verbose:
        print "iname: %s" % options.iname
        print "oname: %s" % options.oname
        print "type : %s" % options.type
        print "output file : %s" % outfile
        print "args: %s" % args
        print "options: %s" % options

    if options.iname is None:
        parse_args(['-h'])
        exit(2)

    try:
        header, data = read_file(options.iname)

        data = json.dumps(data)
        data = json.loads(data)

        colh = sorted(data[0].keys())
        cols = dict()
        for ix in colh:
            cols[ix] = [ data[jx][ix] for jx in xrange(len(data))]

        # for ix in colh:
        #    print "cols[%s]: %s" % (ix, cols[ix])


        it = iter(colh)
        line_chart = pygal.Bar()
        line_chart.x_labels = map(str, cols[next(it)])
        # tmp = next(it)
        # print "cols[%s]: %s" % (tmp, map(str, cols[tmp]))
        for ix in it:
            # print "cols[%s]: %s" % (ix, cols[ix])
            line_chart.add(ix, map(int, cols[ix]))

        # code.interact(local=locals())
        # line_chart.render()
        # line_chart.render_in_browser()
        line_chart.render_to_file(outfile)
        # line_chart.render_to_png(outfile)
        
    except Exception, e:
        print str(e)

    # return 
    
if __name__ == "__main__" :
    main()
 

