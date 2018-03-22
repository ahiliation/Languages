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
             'dict','mountpoint','echo']



files = {'/var/log/syslog' : "[File for system logging]" }
function = {'memset' : "[Fill memory with a constant byte]"}
dmd = ['^\(gdb\)\sbt','FIXME']
language = ['^#include\s<string\.h>']

leng = len(commands)
count = 0
handle = open("setterm.txt")
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        for string in commands:
            if string in word:
                check.append(word)


unique = list(set(check))
# print unique
count = len(unique)
# print "Number of commands found is : ",count
handle.close()

handle = open("setterm.txt")
for line in handle:
    line = line.rstrip()
    y = re.findall('\squote\s',line)
    sumy = sumy + y
# print sumy
unique = list(set(sumy))
# print "Number of commands found is : ", len(unique)
handle.close()


handle = open("sample1.txt")
for line in handle:
    line = line.rstrip()
    for string in commands:
        y = re.findall('\$%s' % string,line)
        sumy = sumy + y
# print sumy
unique = list(set(sumy))
for cmd in unique:
    print cmd,": <Command> :"
print "Number of commands found is : ", len(unique)
handle.close()


handle = open("sample1.txt")
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        for key in files:
            if key in word:
                uniq.append(key)
uniq = list(set(uniq))
for content in uniq:
    print content,colored(": <File> :",'green'),files[content]
handle.close()

handle = open("sample1.txt")
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
	for key in function:
            if key in word:
		uniq1.append(key)
uniq1 = list(set(uniq1))
for content in uniq1:
    print content,colored(": <Function> :",'red'),function[content]
handle.close()

handle = open("sample1.txt")
for line in handle:
    if  re.search(dmd[0],line):
        print colored(": Backtrace detected :",'blue')

#print complete
#uniq2 = list(set(complete))
#for content in uniq2:
#    print colored(": Backtrace detected :",'blue')
handle.close()


#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('www.beautifulwork.org', 80))
#mysock.send('GET http://www.beautifulwork.org  HTTP/1.0\n\n')
#while True:
 #   data = mysock.recv(512)
  #  if ( len(data) < 1 ) :
   #     break
  #  print data
#mysock.close()


try :
    fhand = urllib.urlopen('http://www.beautifulwork.org/pidof')
    for line in fhand:
        if  re.search(dmd[1],line):
            print colored(": FIXME detected :",'yellow')
except :
    print "Issue Found"

test = 0
try :
    fhand = urllib.urlopen('http://www.beautifulwork.org/code-library-libsrcinst')
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
    fhand.close()
except :
    print "Issue Found"


handle = open("sample1.txt")
for line in handle:
    for library in language:
        if  re.search(library,line):
            print colored(": C Language detected :",'blue')

handle.close()
