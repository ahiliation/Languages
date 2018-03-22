import wget
import sys


global string1
global string2
string1 = "Retrieving...  "
string2 = ".pdf"

def lva():
    string3 = "http://www.linuxvoice.com/issues/00"
    string4 = "/Linux-Voice-Issue-00"
    string7 = "Linux-Voice-Issue-00"
    print string1 + string7 + str(i) + string2
    c = string3  + str(i)  + string4 
    d =  str(i) + string2
    try:       
        filename = wget.download(c+d)
        print "\nCompleted\n"
    except:
        print "volume is from 1 to 12"
    
def lvb():
    string5 = "/Linux-Voice-Issue-0"
    string6 = "http://www.linuxvoice.com/issues/0"
    string8 = "Linux-Voice-Issue-0"
    print string1 + string8  + str(i) + string2
    a = string6 + str(i)  + string5 
    b = str(i) + string2
    filename = wget.download(a+b)
    print "\nCompleted\n"

if len(sys.argv) > 1:
    i = int(sys.argv[1])
else:
    print "\n All LinuxVoice Download \n"
    for i in xrange(12):
        if i == 0:
            continue
        if i <= 9:
            lva()
        else:
            lvb()
if i <= 9:
#debug
    lva()
else:
#debug
    lvb()

