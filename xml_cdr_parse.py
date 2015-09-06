#! /ws/xbalaji-sjc/python/bin/python

import glob
import time
from optparse import OptionParser
from xml.dom.minidom import parseString

def read_file(filename):
    fd = open(filename, "r")
    data = fd.read()
    fd.close()
    return data

def parse_args(args):
    parser = OptionParser()
    parser.add_option("-f", "--file", action="store", dest="fname", 
        default="cdr_log.xml", help="CDR log file in xml format")
    return parser.parse_args(args)

def get_start_details(s_node):
    guid = s_node.getElementsByTagName('conference_guid')[0].toxml()
    name = s_node.getElementsByTagName('name')[0].toxml()
    date = s_node.getElementsByTagName('scheduled_date')[0].toxml()
    time = s_node.getElementsByTagName('scheduled_time')[0].toxml()

    guid = guid.replace('<conference_guid>',  '')
    guid = guid.replace('</conference_guid>', '')

    name = name.replace('<name>',  '')
    name = name.replace('</name>', '')

    date = date.replace('<scheduled_date>',  '')
    date = date.replace('</scheduled_date>', '')

    time = time.replace('<scheduled_time>',  '')
    time = time.replace('</scheduled_time>', '')

    return (guid, [name, date, time])

def get_finish_details(e_node):
    guid  = e_node.getElementsByTagName('conference_guid')[0].toxml()
    video = e_node.getElementsByTagName \
                    ('total_audio_video_participants')[0].toxml()
    audio = e_node.getElementsByTagName \
                    ('total_audio_only_participants')[0].toxml()
    dur   = e_node.getElementsByTagName('duration')[0].toxml()


    guid = guid.replace('<conference_guid>',  '')
    guid = guid.replace('</conference_guid>', '')

    video = video.replace('<total_audio_video_participants>',  '')
    video = video.replace('</total_audio_video_participants>', '')

    audio = audio.replace('<total_audio_only_participants>',  '')
    audio = audio.replace('</total_audio_only_participants>', '')

    dur   = dur.replace('<duration>',  '')
    dur   = dur.replace('</duration>', '')
    return (guid, [ video, audio, dur ])


def main(args = None):
    (options, args) = parse_args(args)

    origdata = read_file(options.fname)

    xmlDom = parseString(origdata)

    # xmlTag  = xmlDom.getElementsByTagName('duration')[0].toxml()
    # xmlData = xmlTag.replace('<duration>', '').replace('</duration>', '') 

    # print "xmlTag:  ", xmlTag
    # print "xmlData: ", xmlData

    # create a dict, we'll use 'conference_guid' as the key
    conf = dict()

    # process the start node
    for start in xmlDom.getElementsByTagName('conference_started'):
        (guid, details) = get_start_details(start)
        if not conf.has_key(guid):
            conf[guid] = list()
        conf[guid] += details

    # now process the end node
    for finish in xmlDom.getElementsByTagName('conference_finished'):
        (guid, details) = get_finish_details(finish)
        if conf.has_key(guid):
            conf[guid] += details


    # now display the results
    print "Description, Seconds, Num Video, Num Audio, Start time"
    for guid, data in conf.items():
        if len(data) != 6:
            continue
        start = time.asctime        \
                (time.strptime(data[1] + " " +data[2], '%d %B %Y %H:%M:%S'))
        print "%s, %s, %s, %s, %s" %      \
                (data[0], data[5], data[3], data[4], start)

    # print conf

    return 
    
if __name__ == "__main__" :
    main()
 
