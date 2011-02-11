# -*- coding: utf-8 -*-
# <Copyright and license information goes here.>
from PyQt4.QtCore import Qt, QPoint
from PyQt4.QtGui import QPen
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
import commands
import string
import todo
 
class HelloPython(plasmascript.Applet):
    _todolist = ""
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
        self._todolist = todo.TodoList("/home/kandn/Documents/todo/todo.txt")
 
    def init(self):
        self.setHasConfigurationInterface(False)
        self.resize(350, 350)
        #self.setAspectRatioMode(Plasma.Square)
        self.setAspectRatioMode(Plasma.IgnoreAspectRatio)
 
    def paintInterface(self, painter, option, rect):
	painter.save()
        #pen = QPen()                       
	painter.setPen(Qt.gray)
	#painter.setPen(Qt.black)
	painter.drawText(rect, Qt.AlignTop | Qt.AlignHCenter, "Todo List")
	# get the todo list
	#(status, output) = commands.getstatusoutput("~/bin/todo.sh -p list")
	#lines = output.split("\n")
	
        todos = self._todolist.getList()
        
        ##painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, "Hello Python!")
        #painter.drawText(rect, Qt.AlignTop | Qt.AlignJustify, output)
	
	point = QPoint(15,50)
	y = 50
	
	for item in todos:
	    if item.getPriority() == "A":
		painter.setPen(Qt.yellow)
	    elif item.getPriority() == "B":
		painter.setPen(Qt.darkGreen)
	    elif item.getPriority() == "C":
		painter.setPen(Qt.darkCyan)
	    else:
		painter.setPen(Qt.white)
	    painter.drawText(point,item.getText())
	    y = y +15
	    point.setY(y)
	    
	#for line in lines:
		#words = line.split(" ")
		#if (len(words) > 1) and (words[1] == "(A)"):
		  #painter.setPen(Qt.yellow)
		#elif (len(words) > 1) and (words[1] == "(B)"):
		  #painter.setPen(Qt.darkGreen)
		#elif (len(words) > 1) and (words[1] == "(C)"):
		  #painter.setPen(Qt.darkCyan)
		#else:
		  #painter.setPen(Qt.white)
		#painter.drawText(point, line)
		#y = y + 15
		#point.setY(y)
        painter.restore()

    def createConfigurationInterface(self,parent):
	print "Hello world"
	
 
def CreateApplet(parent):
    return HelloPython(parent)
