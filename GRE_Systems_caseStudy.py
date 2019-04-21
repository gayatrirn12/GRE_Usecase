#!/usr/bin/python

import os, sys

mp=sys.argv[1]
dir_count = 0
file_count = 0

print "{",'\n','  ','"files in each Dir":','\n','  ',"["
#Traverse directory tree
for (path,dirs,files) in os.walk(mp):
    print'\t',('"Directory": {:s},'.format(path))
    dir_count += 1
    #Repeat for each file in directory
    for file in files:
        fstat = os.stat(os.path.join(path,file))

# Print file attributes
        print '\t\t','{"',file,'",',fstat.st_size,'},'
        file_count += 1

print '  ','],',"\n","}"
