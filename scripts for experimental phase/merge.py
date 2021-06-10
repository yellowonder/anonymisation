#by Aju Shrestha
# replaces indicated label(s) with the another indicated label

import sys
import glob

filepath = sys.argv[1]
x = sys.argv[2]
y = sys.argv[3]
#z = sys.argv[4]
#q = sys.argv[5]
#v = sys.argv[6]

filenames = glob.glob(f"{filepath}")
for filename in filenames:
    with open(filename, "r") as f:
        for line in f:
            if x in line:
                line=line.replace(x,y) 
            #if z in line:
                #line=line.replace(z,y)
            #if q in line:
                #line=line.replace(q,y)
            #if q in line:
                #line=line.replace(v,y)
            print(line, end="")