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
batchSwitch = '-dNOPAUSE -dBATCH'
inputFile = raw_input("Input File Name: ")
outputFile = raw_input("Output File Name: ")
startPage = input("Starting Page: ")
lastPage = input("Ending Page: ")
dpi = input("What resolution do you want (76 --- 300): ")

#gs command
command = 'gswin64c' + ' -sDEVICE=' + device + ' -q ' + batchSwitch + ' -sOutputFile=' + outputFile + ' -dFirstPage=' + str(startPage) + ' -dLastPage=' + str(lastPage) + ' ' + '-density=' + str(dpi) + ' ' + '"' + inputFile + '"'


print command

os.system(command)

print "Your Job Done!"
