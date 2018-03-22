import sys, os

oslist = list()
lensys = len(dir(sys))
print "Length of dir(sys) \n", lensys
lenos = len(dir(os))
print "Length of dir(os) \n", lenos
print "Printing dir(os) \n"
oslist = dir(os)
for word in oslist:
    print word
print "Length of dir(os.path)) \n", len(dir(os.path))
