#!/usr/bin/python
import os, sys, json

mp=sys.argv[1]
list = os.listdir(mp)

# Loop and add files to list.
pairs = []
for file in list:

    # Use join to get full file path.
    location = os.path.join(mp, file)

    # Get size and add to list of tuples.
    size = os.path.getsize(location)
    pairs.append((file, size))
    j_string = dict(pairs)
print(json.dumps(j_string, indent=4))