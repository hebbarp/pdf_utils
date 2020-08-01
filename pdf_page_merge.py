#!/usr/bin/python
import os

'''
gs -sDEVICE=pdfwrite \
   -q -dNOPAUSE -dBATCH 
\   
   -sOutputFile=sample-1.pdf \
   -dFirstPage=1 \
   -dLastPage=1 \
   sample.pdf
'''

device = 'pdfwrite'
qSwitch = '-dNOPAUSE -dQUIET'
inputFile1 = raw_input("First file to merge: ")
inputFile2 = raw_input("Second file to merge: ")
outputFile = raw_input("Output File Name: ")

command = 'gswin64' + ' -sDEVICE=' + device + ' -q' + qSwitch + ' -sOutputFile=' + outputFile + ' ' + inputFile1 + ' ' + inputFile2

print command

os.system(command)

print "Your Job Done!"
