#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

def find_word(srivi,chrs_in_guess):
    spit = len(srivi)
    srivialkup = srivi
    for kirjain in chrs_in_guess:
        if srivi.find(kirjain) != -1:
            srivi = srivi.replace(kirjain ,'', 1)
            if len(srivi) == 0:
                print(srivialkup)
                break
                
def main(argv):
    if (len(argv) != 4):
        print("Usage: python ratkaisu.py filename.txt letters lenght")
        exit(1)
        
    program_name,filename,chrs_in_guess,word_length=argv
    f = open(filename)
    for row in f:
        clean_row = row.strip() #.decode('UTF-8')
        if len(clean_row) == int(word_length):
            find_word(clean_row,chrs_in_guess)

if __name__ == "__main__":
    main(sys.argv)
