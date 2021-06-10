# shuffles the training data
# Sophie Arnoult
# Nov 4, 2020
# ------------------------------------
import random
import sys
import os
import glob
# -------- recipes ----------------------

def find_files_with_iglob():
    for filename in glob.iglob('some-folder/**', recursive=True):
        if os.path.isfile(filename): # filter dirs
            print(filename)

# -------- functions ----------------------

def write(sentences, outFile):
    with open(outFile, 'w') as f:
        for s in sentences:
            for token in s:
                f.write(token + "\n")
            f.write("\n")


def read(conll):
    sentences = []
    tokens = []
    with open(conll, 'r') as f:
        for line in f:
            line = line.rstrip()
            if not line:
                if tokens:
                    sentences.append(tokens)
                    tokens = []
            else:
                tokens.append(line)
    if tokens:
        sentences.append(tokens)
    return sentences

def shuffle_file(conll):
    sentences = read(conll)
    random.seed(1)
    random.shuffle(sentences)
    return sentences

 
def shuffle_dir(conlldir):
    files = [f for f in glob.iglob("{}/**".format(conlldir), recursive=False)]
    random.seed(1)
    random.shuffle(files)
    sentences = []
    for f in files:
        sentences.extend(read(f))
    random.shuffle(sentences)
    return sentences


# -------- main -------------------------------------
def main(conll, outFile):
    if os.path.isfile(conll):
        sentences = shuffle_file(conll)
    else:
        sentences = shuffle_dir(conll)
    write(sentences, outFile)
 
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python shuffle-conll.py conll outfile")
    else:
        main(sys.argv[1], sys.argv[2])