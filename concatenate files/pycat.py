#by Guido van den Heuvel
#script to concatenate several files in one directory into one file
import sys
import glob

filepath = sys.argv[1]

filenames = glob.glob(filepath)

for filename in filenames:
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
        print()