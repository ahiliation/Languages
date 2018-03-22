import time
import sys
import urllib2

toolbar_width = 40

download_url = "http://www.linuxvoice.com/issues/003/Linux-Voice-Issue-003.pdf"
chunk_size = 1000

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
file = open("Linux-Voice-Issue-003.pdf", 'w')

for i in xrange(toolbar_width):
    time.sleep(0.1) # do real work here
    response = urllib2.urlopen(download_url).read(1000)
    file.write(response)
    sys.stdout.write("-")
    sys.stdout.flush()
    
file.close()
print("Completed")

# update the bar
#sys.stdout.write("-")
#sys.stdout.flush()

sys.stdout.write("\n")
