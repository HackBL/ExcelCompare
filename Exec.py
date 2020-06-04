import os
import sys

itemId = []

# Read excel files
with open( "file.txt", "r" ) as ins:

	for line in ins:
		itemId.append( line.replace( '\n', '' ) ) # Store item id into array
ins.close()


itemId = list( filter( None, itemId ) ) 

newFile = sys.argv[1]

for i in range( len( itemId ) ): # Execute all id
	os.system( "Python3 filedChecker.py " + itemId[i] + ' ' + newFile )