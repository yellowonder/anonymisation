#by Aju Shrestha
#selects a indicated percentage of lines in of dataset contain in one file
import sys
import glob
 
filepath = sys.argv[1]
x = sys.argv[2] #indicate percentage
 
filenames = glob.glob(f"{filepath}")
 
x=int(x) for filename in filenames:
    with open(filename, "r") as f:
        for i,line in enumerate(f):
            n_lines=i+1
        n_lines=int(n_lines)#total number of lines
        p=n_lines*(x/100) #x % of the total number of lines
 
for filename in filenames:
    with open(filename, "r") as f:
        for i,line in enumerate(f):
            y=i+1 #keep count of the number of lines
            if y <= p: #if number is smaller than the x% of the total amount of lines
               print(line, end="") #keep it
            else: #else break for loop
                break