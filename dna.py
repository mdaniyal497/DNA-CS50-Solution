from csv import reader, DictReader
from sys import argv, exit
import re


if len(argv) != 3:
    print("Invalid arguments")
    exit(1)

# open the csv file to extract name of strs as a list
with open(argv[1]) as strfile:
    strf = reader(strfile)
    for row in strf:
        strs = row
        strs.pop(0)
        break

# open txt file to extract dna code
with open(argv[2]) as dnafile:
    dnar = reader(dnafile)
    for row in dnar:
        dnalist = row

# string of dna code from txt file
dna = dnalist[0]

# dict to store the str sequences
sequences = {}

# copy the str names from strs (taken from strfile)
for seq in strs:
    sequences[seq] = 1

# check for the longest continuously repeated str
for key in strs:
    maxvalue = 0
    # making a regex
    k = fr"(?:{key})+"
    look = re.findall(k, dna)
    # check if list is empty 
    i = len(look)
    # dividing the length of the longest repeated sequence by strlen
    if i != 0:
        maxvalue = len(max(look, key=len)) / len(key)
    # copying the seq length to dict sequences
        sequences[key] = int(maxvalue)

# comparing sequences dict with the csv file for matches
with open(argv[1]) as peoplefile:
    people = DictReader(peoplefile)
    for person in people:
        match = 0
        for seq in strs:
            if sequences[seq] == int(person[seq]):
                match += 1
            if match == len(sequences):
                print(person['name'])
                exit(0)

    print("No match")