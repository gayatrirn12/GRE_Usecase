#!/usr/bin/python

import os, sys

mp=sys.argv[1]
dir_count = 0
file_count = 0

print "{",'\n "files":','\n ['
for (path,dirs,files) in os.walk(mp):
    dir_count += 1
    for file in files:
        fstat = os.stat(os.path.join(path,file))
        print '\t',('{"%s/%s",%d},'%(path,file,fstat.st_size))
        file_count += 1
print ' ],','\n}'
