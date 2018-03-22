#! /usr/bin/python

import re
import socket
import urllib
from termcolor import colored

sumy = list()
y = list()
complete = []
unique = list()
uniq =  []
uniq1 = []
uniq2 = []
check = list()
commands = list()
commands = ['grep','ls','pstree','quote','setterm','dig','true','false',
            'cat','groups','hexdump','head','getopt','ypdomainname','vmstat',
            'sudo','stat','dnsdomainname','tee','free','pidof','man','factor',
             'dict','mountpoint','echo','split','rm']



files = {'/var/log/syslog' : "[File for system logging]" }
function = {'memset' : "[Fill memory with a constant byte]"}
dmd = ['^\(gdb\)\sbt','FIXME']
language = ['^#include\s<string\.h>']


try :
    fhand = urllib.urlopen('http://www.beautifulwork.org/split')
    for line in fhand:
        if re.search("</pre>",line):
            break
        line = line.strip()
        if re.search("<pre>",line):
            while True:
                if re.search("</pre>",line):
                    break
                for line in fhand:
                    line = line.strip()
                    if re.search("</pre>",line):
                        break
                    print colored(line,'red')
                    for string in commands:
                        y = re.findall('\$%s' % string,line)
                        sumy = sumy + y
                        if re.search("</pre>",line):
                            break
    unique = list(set(sumy))
    for cmd in unique:
            print cmd,": <Command> :"
    print "Number of commands found is : ", len(unique)
    fhand.close()
except :
    print "Issue Found"


#handle = open("sample1.txt")
#for line in handle:
#    for library in language:
#        if  re.search(library,line):
#            print colored(": C Language detected :",'blue')

#handle.close()
