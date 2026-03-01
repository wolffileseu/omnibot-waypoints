# coding: iso-8859-1
leftquotes = ['\'', '\"', '„', '»']
rightquotes = ['\'', '\"', '“', '«']

caretpos = editor.getCurrentPos()
columnnumber = editor.getColumn( caretpos )
linetext = editor.getCurLine()
linestart = editor.getCurrentPos() - columnnumber

# console.write( "caretpos: " + str(caretpos) + "\r\n")
# console.write( "columnnumber: " + str(columnnumber) + "\r\n")
# console.write( "linestart: " + str(linestart) + "\r\n")

k = 0
padspaces = ""

# replace tabs with the appropriate number of spaces internally
for i in xrange( 0,editor.getTabWidth() ):
	padspaces += " "
linetext = linetext.replace( "\t", padspaces )

def findleft():
	# search backwards from current position until we find a left quote
	global k
	for i in xrange( columnnumber-1,0,-1 ):
		# console.write(str(i)+"\r\n")
		# console.write(linetext[i])
		for quote in leftquotes:
			if linetext[i] == quote:
				editor.setSelectionStart(linestart+i)
				# store the index of the quote we found
				k = leftquotes.index(quote)
				return True
	return False

def findright():
	# now find a matching quote on the right of the caret
	j = 0
	for i in xrange( columnnumber,len(linetext) ):
		j += 1
		# console.write(str(k))
		if linetext[i] == rightquotes[k]:
			editor.setSelectionEnd(caretpos+j)
			return True
	return False

if findleft() == True:
	if findright() == False:
		notepad.messageBox('No matching quote mark found!', 'Notepad++', 0)