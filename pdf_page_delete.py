#!/usr/bin/python
import os

'''
gs -sDEVICE=pdfwrite \
   -q -dNOPAUSE -dBATCH \
   -sOutputFile=sample-1.pdf \
   -dFirstPage=1 \
   -dLastPage=1 \
   sample.pdf
'''

device = 'pdfwrite'
qSwitch = '-dNOPAUSE -dQUIET'
inputFile = raw_input("Input File Name: ")
outputFile = raw_input("Output File Name: ")
startPage = input("Starting Page: ")
lastPage = input("Ending Page: ")


command = 'gswin32' + ' -sDEVICE=' + device + ' -q' + qSwitch + ' -sOutputFile=' + outputFile + ' -dFirstPage=' + str(startPage) + ' -dLastPage=' + str(lastPage) + ' ' + inputFile

print command

os.system(command)

print "Your Job Done!"
