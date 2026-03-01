editor.beginUndoAction()

notepad.runMenuCommand( 'TextFX Edit', 'Reindent C++ code' )
notepad.menuCommand( MENUCOMMAND.EDIT_TRIMTRAILING )
editor.rereplace( "^\t\t\{ return; \}", "\t\t\t\{ return; \}" )

# join empty braces on a single line:
# editor.pymlreplace( r"(\s)+\=\r$\n(\t)+\{\r$\n(\t)+\},", " = {},", 0, Editor.INCLUDELINEENDINGS )

editor.endUndoAction()
