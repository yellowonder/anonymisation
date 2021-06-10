import sys
import glob

filepath = sys.argv[1]

filenames = glob.glob(filepath)

for filename in filenames:
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
        print()