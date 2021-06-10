# Anonymisation of police reports at CBS—as a pre-step for cybercrime-categorisation
this respository contains scripts and jupyter notebooks for a BERTje-based NERC tool for the anonymisation of dutch police reports 

The jupyter notebooks contain python code for:

(1) preprocessing, sample design, and transforming selected string of data pandas cells to conll files—ready to be annotated in Inception. Python packages required are pandas, numpy, glob, re, spacy, TextToCoNLL, and os.

(2) counting annotations in the annotated files with conll 2002 format. Python packages required are pandas, numpy, glob, re, os, and csv.

Addionally, bash scripts are made available for:
(1) concatanation of files after annotation
(2) preprocessing of files: covert conll to json, indicate max token lenght, and shuffling sentences.
(3) experimental phase: merges and systematically testing with training data size.

