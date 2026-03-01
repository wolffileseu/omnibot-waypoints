#######################################################################
# Trim trailing whitespace, set line end format to Win, optionally set
# Debug to 0 and save. Committing to SVN does not work atm.
#######################################################################
pattern = r"(^\s{1,4}Debug = )(true|1|2)(,.*$)"
match0 = ""
msgBoxResult = MESSAGEBOXFLAGS.RESULTNO

def regExFunc( match ):
    global match0
    match0 = match.group(0)
    # console.write( str( match0 ) )

def replaceDebugValue( match ):
    oldValue = match.group( 2 )
    newValue = "false" if oldValue == "true" else "0"
    return match.group( 1 ) + newValue + match.group( 3 )

editor.beginUndoAction()
notepad.menuCommand( MENUCOMMAND.EDIT_TRIMTRAILING )
editor.endUndoAction()

editor.beginUndoAction()
notepad.menuCommand( MENUCOMMAND.FORMAT_TODOS )
editor.endUndoAction()

editor.research( pattern, regExFunc )
if match0 != "":
    msgBoxResult = notepad.messageBox("Do you want to set Debug to 0?", "Confirmation", MESSAGEBOXFLAGS.YESNO )

if msgBoxResult == MESSAGEBOXFLAGS.RESULTYES:
    editor.beginUndoAction()
    editor.rereplace( pattern, replaceDebugValue )
    editor.endUndoAction()

notepad.save()
editor.setSavePoint()

# Committing to SVN does not work atm
# result = notepad.runPluginCommand( 'Subversion', 'Commit File', True )
# console.write( str(result) )
