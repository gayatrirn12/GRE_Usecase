#!/usr/bin/python

import os, sys
import json
mp=sys.argv[1]
dir_count = 0
file_count = 0

print "{",'\n','"files in each Dir":','\n',"  ["
for (path,dirs,files) in os.walk(mp):
    print('"Directory": "%s",'%(path)),'\n    ['
    dir_count += 1
    for file in files:
        pairs= []
        fstat = os.stat(os.path.join(path,file))
        pairs.append((file, fstat.st_size))
        j_string = dict(pairs)
        file_count += 1
        print '\t',(json.dumps(j_string, sort_keys=True))

    print '    ],'
print '  ',']',"\n","}"