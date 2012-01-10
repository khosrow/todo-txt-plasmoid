README
======

todotxt_plasmoid is a Plasma widget for KDE, that displays your todo items from a todo.txt file.  
Currently only reading is supported and in order to add to the file you still need the todo.txt shell script.

Requirements
------------
This widget works in conjunction with todotxt CLI script, available at http://todotxt.com

Building from source
--------------------
Use the following commands to build the plasmoid on KDE 4.x:

	cd todotxt_plasmoid
	zip -x ".git/*" -x ".gitignore" -x "*/*.pyc" -r ../todotxt_plasmoid.zip .
	cd ..
	plasmapkg -i todotxt_plasmoid.zip
	plasmoidviewer todotxt_plasmoid
