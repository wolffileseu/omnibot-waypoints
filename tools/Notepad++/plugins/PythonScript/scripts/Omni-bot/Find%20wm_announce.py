####################################################################
# Copies announce messages from a .script file to the clipboard and
# to a new file.
####################################################################
 
# set to True if you want to include voice announcements,
# otherwise to False:
addvoiceannouncements = False
stringlist = []

def regExFunc( match ):
	# appends matches to the list so we can optionally dump it
	# to a new file later on
	global stringlist
	if voice:
		stringlist.append( match.group(4) )
	else:
		stringlist.append( match.group(3) )

voice = False
editor.research( "^(\s)*wm_announce(\s)+\"(.*)\"", regExFunc )

# second pass for voice announcements
if addvoiceannouncements:
	voice = True
	editor.research( "^(\s)*wm_teamvoiceannounce(\s)+[01](\s)+\"(.*)\"", regExFunc )

if len(stringlist) > 0:
	notepad.new()
	notepad.menuCommand( MENUCOMMAND.VIEW_GOTO_ANOTHER_VIEW )
	for string in stringlist:
		string = string[0:71] # trim everything after the 71st character
		editor.copyText( string )
		editor.addText( string + "\r\n" )
	console.write( "\nCopied " + str(len(stringlist)) + " announcement messages." )