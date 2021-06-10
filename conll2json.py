#by Sophie Arnoult
# converts a conll2002 file to json, where each sentence appears as a dictionary
# with a list of words and a list of ner labels

import sys
import json

def read_sentences(conll):
    """returns list of sentences in conll format"""
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

def map2entry(sentence):
    """converts a list of conll lines to a dictionary with a list of tokens and a list of ner labels"""
    words = []
    ner = []
    for line in sentence:
        wl = line.split()
        words.append(wl[0])
        ner.append(wl[1])
    return {'words': words, 'ner': ner}
  
def to_json(sentences, as_list=False):
    json_sentences = [map2entry(s) for s in sentences]
    if as_list:
        obj = json.dumps(json_sentences, ensure_ascii=False)
        print(obj)
    else:
        for s in json_sentences:
            print(json.dumps(s, ensure_ascii=False))
  
def main():
    sentences = read_sentences(sys.argv[1])
    to_json(sentences)
  
if __name__ == "__main__":
    main()