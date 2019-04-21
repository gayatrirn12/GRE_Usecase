#!/usr/bin/python

import os, sys

mp=sys.argv[1]
dir_count = 0
file_count = 0

print "{",'\n','  ','"files in each Dir":','\n','  ',"["
for (path,dirs,files) in os.walk(mp):
    print'\t',('"Directory": "%s",'%(path)),'\n\t ['
    dir_count += 1
    for file in files:
        fstat = os.stat(os.path.join(path,file))
        print '\t\t',('{"%s",%d},'%(file,fstat.st_size))
        file_count += 1
    print '\t ],'
print '  ','],',"\n","}"