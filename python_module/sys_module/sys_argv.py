#!/usr/bin/python
#filename:cat.py

import sys

print "the first argv :" sys.argv[0]
print "the second argv:" sys.argv[1]
print "the third argv :" sys.argv[2]
print "the other argv :" sys.argv[3:]

def readfile(filename):
    '''Print a file to the standard output'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line #notice comma
    f.close()

#script starts from here
if len(sys.argv) < 2:
    print 'No action specified'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    #fetch sys.argv[1] but without the first two characters
    if option == 'version':
        print 'Version 1.2'
    elif option == 'help':
        print '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
    --version:Prints the version number
    --help:Dispaly this help'''
    else:
        print 'Unknown option'
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)