# -*- coding: utf-8 -*-
# <Copyright and license information goes here.>
#from PyQt4.QtCore import Qt, QPoint
from PyQt4.QtCore import *
#from PyQt4.QtGui import QPen
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript, kdeui, kdecore
from PyKDE4.kdeui import *
import string

from todo import TodoList
#from configDialog import ConfigDialog
from configform import ConfigForm
 
class TodoApplet(plasmascript.Applet):
	_todolist = ""
	_settings = {}
	#_configDialog = ""
	_configForm = ""
	def __init__(self,parent,args=None):
		plasmascript.Applet.__init__(self,parent)
	
	def init(self):
		self.setHasConfigurationInterface(True)
		#self.resize(350, 350)
		#self.setAspectRatioMode(Plasma.Square)
		self.setAspectRatioMode(Plasma.IgnoreAspectRatio)
		self._settings["todoURL"] = "/home/kandn/Documents/todo/todo.txt"
		self._settings["priorityAColour"] = ""
		self._settings["priorityBColour"] = ""
		self._settings["priorityCColour"] = ""
		self._settings["priorityDColour"] = ""        
		self._todolist = TodoList(self._settings["todoURL"])
	
	def createConfigurationInterface(self, parent):
		#self._configDialog = ConfigDialog(parent, self._settings)
		self._configForm = ConfigForm(parent, self._settings)
		##parent.setMainWidget(self._configDialog)
		#page = parent.addPage( self._configDialog, "My Config Page")
		page = parent.addPage(self._configForm, "todo.txt Config Page")
		page.setIcon(KIcon("preferences-desktop-color"))
		self.connect(parent, SIGNAL("okClicked()"), self.configAccepted)
	
	def showConfigurationInterface(self):
		dialog = KPageDialog()
		dialog.setFaceType(KPageDialog.List)
		dialog.setButtons(KDialog.ButtonCode(KDialog.Ok | KDialog.Cancel))
		self.createConfigurationInterface(dialog)
		dialog.exec_()
	
	def configAccepted(self):
		#self._settings = self._configDialog.getSettings()
		self._settings = self._configForm.getSettings()
		self._todolist.refreshList()
	
	def paintInterface(self, painter, option, rect):
		painter.save()
		#pen = QPen()                       
		painter.setPen(Qt.gray)
		#painter.setPen(Qt.black)
		painter.drawText(rect, Qt.AlignTop | Qt.AlignHCenter, "Todo List")
		#todos = self._todolist.getList()
		todos = self._todolist.sortList()
		##painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, "Hello Python!")
		#painter.drawText(rect, Qt.AlignTop | Qt.AlignJustify, output)
		point = QPoint(15,50)
		y = 50
		for item in todos:
			# find the color to use for each priority
			if item.getPriority() == "A":
				painter.setPen(Qt.yellow)
			elif item.getPriority() == "B":
				painter.setPen(Qt.darkGreen)
			elif item.getPriority() == "C":
				painter.setPen(Qt.darkCyan)
			else:
				painter.setPen(Qt.white)
			# now draw the text in the widget
			painter.drawText(point,item.getText())
			y = y +15
			point.setY(y)
		painter.restore()
	

def CreateApplet(parent):
	return TodoApplet(parent)
