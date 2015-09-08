#! /usr/bin/env python

import os.path
import csv
import json
import pygal
from optparse import OptionParser
import code

input_extns = [ ".csv", ".json", ".xml" ]
output_extns = [ ".svg" ]

def read_file(filename):
    try:
        extension = os.path.splitext(filename)[1]
        if extension not in input_extns:
            raise Exception("Reading files of this type not supported yet")

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

def print_json_dict(cols):
    print "json converted to dict/row: "
    for ix in sorted(cols.keys()):
        print "cols['%s']: %s" % (ix, cols[ix])
    return

def print_cmdline_params(options):
    print "iname: %s" % options.iname
    print "oname: %s" % options.oname
    print "type : %s" % options.type
    print "output file : %s" % (options.oname + '.' + options.type)
    print "args: %s" % args
    print "options: %s" % options
    return

def create_output(chart, filename, extension):

    extension = "." + extension
    filename += extension
    try:
        output = None
        if extension not in output_extns:
            raise Exception("Output of this type not supported yet")

        if extension == ".png" :
            chart.render_to_png(filename)
        elif extension == ".svg" :
            chart.render_to_file(filename)
        else:
            output = chart.render()

    except Exception, e:
        raise Exception(str(e))
    else:       # this is else for exception (if there is no exception)
        pass
    finally:    # this will always execute
        pass
    return output

def json_to_dict(data):
    colh = sorted(data[0].keys())
    cols = dict()
    for ix in colh:
        cols[ix] = [ data[jx][ix] for jx in xrange(len(data))]
    return cols

# create chart from the c_data, which is a dictionary
def create_chart(c_data, c_type = "stbar", title = None):
    title = "xbalaji - pygal demo"
    if c_type == "line":
        line_chart = pygal.Line(title=title)
    elif c_type == "bar":
        line_chart = pygal.Bar(title=title)
    else:
        line_chart = pygal.StackedBar(title=title)

    it = iter(sorted(c_data.keys()))
    line_chart.x_labels = map(str, c_data[next(it)])
    for ix in it:
        line_chart.add(ix, map(int, c_data[ix]))
    return line_chart

def main(args = None):
    (options, args) = parse_args(args)

    if options.verbose:
        print_cmdline_params(options)

    if options.iname is None:
        parse_args(['-h'])
        exit(2)

    try:
        header, data = read_file(options.iname)

        data = json.dumps(data, sort_keys = True, indent=2)
        if options.verbose:
            print "stringfied: ", data

        data = json.loads(data)
        if options.verbose:
            print "jsonified data: ", data

        cols = json_to_dict(data)
        if options.verbose:
            print_json_dict(cols)

        # code.interact(local=locals())
        chart = create_chart(cols)
        create_output(chart, options.oname, options.type)
        
    except Exception, e:
        print str(e)

    # return 
    
if __name__ == "__main__" :
    main()
 

