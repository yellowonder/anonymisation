#by Aju Shrestha and Guido van den Heuvel
#replace a several labels with a new label
import sys
import glob


filepath = sys.argv[1]
oldlabels = sys.argv[2] #string of labels
newlabel = sys.argv[3] #new label


oldlabels_list = oldlabels.split() #transform string in to list of labels


filenames = glob.glob(f"{filepath}")
for filename in filenames:
    with open(filename, "r") as f:
        for line in f:
            for oldlabel in oldlabels_list:
                if oldlabel in line:
                    line = line.replace(oldlabel, newlabel)
            print(line, end="")