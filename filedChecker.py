# Instruction:

# This program is used for chekcing two excel files, 
# whether both of them have tags that don't match each other

import sys
import os
import xlrd
import xlsxwriter
import numpy as np


def checkDuplicate( arr ): 
	for i in range( len( arr ) - 1 ):
		for j in range( i+1, len( arr ) ):
			if arr[i] == arr[j]:
				print ( arr[i] )


def writeFile( arr, newFile ):	# Open and write arr into file
	workbook = xlsxwriter.Workbook( newFile+'.xlsx' )
	worksheet = workbook.add_worksheet()

	for col, data in enumerate( arr ):
		row = 0
		worksheet.write_column( row, col, data )

	workbook.close()


def doesFileExists( filePath ): # Check file exists
	return os.path.exists( filePath )


def readFile( file ):
	arr = []
	loc = ( file )

	wb = xlrd.open_workbook( loc )
	sheet = wb.sheet_by_index( 0 )
	sheet.cell_value( 0, 0 )	# For row 0 and column 0


	for i in range( sheet.ncols ):
		arr.append( sheet.cell_value( 0,i ) )

	return arr


def combination( arr1, arr2 ): # Combining two lists without duplicates
	return sorted( np.unique( arr1+arr2 ) )


def matchChecker( refArr, finalArr, dataArr, index ):

	for i in finalArr:
		if i in refArr:
			dataArr[index].append('')
		else:
			dataArr[index].append(1)

	
def addAttr( arr, index, data ):
	for i in range( len( arr[4] ) - 1 ):
		arr[index].append( data )


def getColData( file ):
	item = []

	loc = ( file )

	wb = xlrd.open_workbook( loc )
	sheet = wb.sheet_by_index(0)

	for i in readFile( file ):
		if i == 'category':
			item.append( sheet.cell_value( 1, readFile( file ).index( i ) ) )	# Get data of category

		if i == 'categoryId':
			item.append( sheet.cell_value( 1, readFile( file ).index( i ) ) ) # Get date of categoryId

	return item


def appending( oldArr, newArr ):
	final = oldArr
	for i in range( len( newArr ) ):
		for j in range( 1 , len( newArr[i] ) ):
			final[i].append( newArr[i][j] )

	return final


# --- Variables starts ---
data = [['category'], ['categoryId'], ['tableName'], ['filed'], ['new'], ['old_changed']]

fileName = sys.argv[1]
newFileName = sys.argv[2]

newTag = readFile( './category/'+ fileName + '.xlsx' )
baseTag = readFile( './categoryIT/'+ fileName+ '.xlsx' )
# --- Variables ends ---


# ---- Invoke starts ----
matchChecker( newTag , combination( baseTag,newTag ),data,4 ) # Append new
matchChecker( baseTag , combination( baseTag,newTag ), data, 5 )	# Append old_changed

addAttr( data, 2, fileName )	# Append tableName

for i in combination( baseTag, newTag ): # Append filed
	data[3].append( i )
	data[0].append( getColData( './category/' + fileName + '.xlsx' )[0] )
	data[1].append( getColData( './category/' + fileName + '.xlsx' )[1] )
# ---- Invoke ends ----


# ---- Exec Program starts ---
checkDuplicate( newTag ) # Check duplicate tags

if doesFileExists( './'+newFileName+'.xlsx' ):  # Update File
	loc = ( './'+newFileName+'.xlsx' )

	wb = xlrd.open_workbook( loc )
	sheet = wb.sheet_by_index(0)
	sheet.cell_value( 0, 0 )

	row = sheet.nrows # Update row
	col = sheet.ncols # Update col

	oldArray = [] # Exist data from excel

	for i in range( col ): # Data excel -> array
		pairs = [] # Existed attr in the file

		for j in range( row ):
			pairs.append( sheet.cell_value( j,i ) )

		oldArray.append( pairs )

	finalArr = appending( oldArray, data )
	writeFile( finalArr, newFileName )

else: # Open excel file
	writeFile( data, newFileName )
# ---- Exec Program ends ---




# --------Unit Test --------








