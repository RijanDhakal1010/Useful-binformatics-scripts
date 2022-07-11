#!/usr/bin/env python3

import sys
import pandas as pd
import re

def main():

    #creat a dictionary to store the taxonomy
    taxonomy = {}

    # take in system arguments (to be used if the input file is supplied as the first sys argument)
    args = sys.argv
    # the first argument is the name of the file that we want to convert
    taxtree_filename = args[1]
    # read in the first file using with
    with open(taxtree_filename, 'r') as taxtree_file:
        taxtree_lines = taxtree_file.readlines()

    # loop through the lines of the file
    for line in taxtree_lines:
        # use regex to see if the line starts with a number
        if re.match(r'^\d+', line):
            # assign everything after the first period to the name
            name = line[line.find('.')+1:]
            name = name.strip()
            #make an end marker for the name with the format "End of name"
            end_marker = "End of " + name
            # make a nested dictionary with the name inside the taxonomy dictionary
            taxonomy[name] = {}
        # else if the line has the end marker break the loop
        elif line.replace(" ","") == end_marker.replace(" ","") or line.replace(" ","") == end_marker.replace(" ","") + "\n":
            continue
        # els if the line is blank skip break the loop
        elif line == "\n":
            continue
        #else the first word is the key and anything
        else:
            line = line.strip()# remove newline character
            words = line.split("\t",1) # split the line at the first tab
            if words[0] in taxonomy[name]: # add value if key already exists
                taxonomy[name][words[0]].append(words[1])
            else: # add key and value if key does not exist
                taxonomy[name][words[0]] = [words[1]]
    
    dict_to_table(taxonomy)

def dict_to_table(taxonomy):
    df = pd.DataFrame.from_dict(taxonomy, orient='index')
    df.fillna('0', inplace=True)
    out = pd.DataFrame(df).stack().map(', '.join).unstack()
    out.to_csv('taxonomy_7.csv', index=True, header=True)

main()