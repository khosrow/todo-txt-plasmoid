README
======

todotxt_plasmoid is a Plasma widget for KDE, that displays your todo items from a todo.txt file. Currently only reading is supported and in order to add to the file you still need the todo.txt shell script.

Requirements
------------
This widget works in conjunction with todotxt CLI script, available at [todotxt.com](http://todotxt.com). A full KDE installation with kde-plasma is needed as well. 

Building from source
--------------------
Use the following commands to build the plasmoid on KDE 4.x:

        git clone git://github.com/khosrow/todo-txt-plasmoid.git todotxt_plasmoid
	cd todotxt_plasmoid 
	zip -x ".git/*" -x ".gitignore" -x "*/*.pyc" -x "build.sh" -x "*~" -r ../todotxt_plasmoid.plasmoid .
	cd ..
	plasmapkg -i todotxt_plasmoid.plasmoid
	plasmoidviewer todotxt_plasmoid

Alternatively, you can use *build.sh* to build and update after code changes.
