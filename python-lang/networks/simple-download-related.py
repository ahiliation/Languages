import urllib2

toolbar_width = 40

download_url = "http://www.beautifulwork.org/plan/beautifulwork-algorithms.pdf"

print "Retrieving...\n"
response = urllib2.urlopen(download_url)
tbw = response.read()
file = open("document.pdf", 'w')
file.write(tbw)
file.close()
print("Completed")


