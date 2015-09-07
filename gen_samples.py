#! /usr/bin/env python

# python -c 'import random; g = lambda x: random.sample(range(x*10, x*80), 20); print zip(g(4), g(9))'

from optparse import OptionParser
import random
import csv
import json

# global constants
# header="x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10"
# header="x"

# global variables
# max_rows = 5
# max_cols = 4
# offset = 1
# filename = 'sample'

y = lambda x,num_rows: random.sample(range(x*10, x*20), num_rows)
y = lambda x,num_rows: [ random.choice(xrange(11)) for ix in xrange(num_rows) ]

# csv_data is two dimensional array with header on top
def create_csv_file(fname, csv_data):
    csvfile = fname + '.csv'
    f = open(csvfile, 'wb')
    csv_w = csv.writer(f)
    csv_w.writerows(csv_data)
    f.close()

# json_data is two dimensional array with header on top
def create_json_file(fname, json_data):
    jsonfile = fname + '.json'
    f = open(jsonfile, 'wb')
    hdr = json_data[0]
    jdata = map(lambda lst: dict(zip(hdr, lst)), json_data[1:])
    json.dump(jdata, f, sort_keys=True, indent=2)
    f.close()
    return json.dumps(jdata, sort_keys=True, indent=2)

# creates a two dimensional array from header and lists
def create_raw_data(hdr, x, y1, y2, y3, y4):
    num_rows = len(x)
    raw = [list()]*(num_rows+1)
    raw[0] = hdr.split(',')
    for ix in xrange(num_rows):
        raw[ix+1] = [x[ix],y1[ix], y2[ix], y3[ix], y4[ix]]
    return raw

def create_raw_data2(hdr, *args):
    num_rows = len(args[0])
    num_cols = len(args)
    raw = [list()]*(num_rows+1)
    raw[0] = hdr.split(',')[:num_cols]
    for ix in xrange(num_rows):
        raw[ix+1] = [ args[jx][ix] for jx in xrange(num_cols) ]
    return raw

def create_raw_data3(hdr, offset = 1, num_rows = 10, num_cols = 4):
    # create y-lists from header, modify the locals to dynamically 
    # add list variable names
    # x, y1, y2, ... are created dynamically

    L = locals()
    for ix in xrange(num_cols):
        L['%s' % hdr.split(',')[ix]] = y(2*ix + 1, num_rows)

    # modify x to sane values instead of randoms
    # x = [ ix + offset for ix in xrange(num_rows) ]
    L['x'] = [ ix + offset for ix in xrange(num_rows) ]

    raw = [list()]*(num_rows+1)
    raw[0] = hdr.split(',')[:num_cols]
    for ix in xrange(num_rows):
        raw[ix+1] = [
                L['%s' % hdr.split(',')[jx]][ix] for jx in xrange(num_cols)]

    return raw

def parse_args(args):
    parser = OptionParser()
    parser.add_option("-r", "--rows", type="int", action="store", 
        default=10, dest="max_rows", help="number of rows")
    parser.add_option("-c", "--cols", type="int", action="store",
        default=4, dest="max_cols", help="number of columns")
    parser.add_option("-o", "--offset", type="int", action="store",
        default=1, dest="offset", help="x axis offset")
    parser.add_option("-f", "--file", type="string", action="store", 
        default="sample", dest='filename', help="file name before extension")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
        help="print verbose debugging")
    parser.add_option("-q", "--quiet",  action="store_false", dest="verbose",
        default=False, help="no output be quiet")
    return parser.parse_args(args)

def main(args = None):
    (options, args) = parse_args(args)

    if options.filename is None:
        parse_args(['-h'])
        exit(2)

    max_rows = options.max_rows
    max_cols = options.max_cols
    offset = options.offset
    filename = options.filename

    header = 'x'
    for ix in xrange(1,max_cols):
        header += ',y%s' % ix

    raw_data = create_raw_data3(header, offset, max_rows, max_cols)
    create_csv_file(filename, raw_data)
    jdata = create_json_file(filename, raw_data)
    # print jdata

# raw_data = create_raw_data(header, x, y1, y2, y3, y4)
# raw_data = create_raw_data2(header, x, y1, y2, y3, y4)


if __name__ == "__main__" :
    main()
 


