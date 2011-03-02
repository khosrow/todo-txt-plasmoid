# -*- coding: utf-8 -*-
# <Copyright and license information goes here.>
#from PyQt4.QtCore import Qt, QPoint
from PyQt4.QtCore import *
#from PyQt4.QtGui import QPen
from PyQt4.QtGui import *
from PyQt4 import uic
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
	_configForm = ""
	def __init__(self,parent,args=None):
		plasmascript.Applet.__init__(self,parent)
	
	def init(self):
		self.setHasConfigurationInterface(True)
		#self.resize(350, 350)
		#self.setAspectRatioMode(Plasma.Square)
		self.setAspectRatioMode(Plasma.IgnoreAspectRatio)
		self._settings["todoURL"] = "/home/khosrow/Documents/todo.txt"
		self._settings["showLineNumbers"] = False
		self._settings["showPriority"] = False
		self._settings["showProjects"] = False
		self._settings["showContexts"] = False
		#self._settings["priorityAColor"] = Qt.yellow
		self._settings["priorityAColor"] = "#ffff00"
		#self._settings["priorityBColor"] = Qt.darkGreen
		self._settings["priorityBColor"] = "#008000"
		#self._settings["priorityCColor"] = Qt.darkCyan
		self._settings["priorityCColor"] = "#008080"
		#self._settings["priorityDColor"] = Qt.blue        
		self._settings["priorityDColor"] = "#0000ff"        
		self._todolist = TodoList(self._settings["todoURL"])
		print "filepath:"
		print str(self.package().filePath('ui', 'config.ui'))
		print "----"
		print "priority a color:"
		print str(self._settings["priorityAColor"])
	
	def createConfigurationInterface(self, parent):
		#self._configForm = ConfigForm(parent, self._settings)
		self.generalWidget = QWidget(parent)
		self._generalConfigForm = uic.loadUi(str(self.package().filePath('ui', 'config.ui')), self.generalWidget)
		
		# set the defaults
		self._generalConfigForm.todourl.setText(str(self._settings["todoURL"]))
		if self._settings["showLineNumbers"] == True:
			self._generalConfigForm.linenumbers.setChecked(True)
		if self._settings["showPriority"] == True:
			self._generalConfigForm.priorities.setChecked(True)
		if self._settings["showProjects"] == True:
			self._generalConfigForm.projects.setChecked(True)
		if self._settings["showContexts"] == True:
			self._generalConfigForm.contexts.setChecked(True)
		page1 = parent.addPage(self._generalConfigForm, "General")
		page1.setIcon(KIcon("preferences-other"))
		
		self.colorWidget = QWidget(parent)
		self._colorConfigForm = uic.loadUi(str(self.package().filePath('ui','config_2.ui')), self.colorWidget)
		
		# set color defaults
		self._colorConfigForm.colorA.setColor(QColor(self._settings["priorityAColor"]))
		self._colorConfigForm.colorB.setColor(QColor(self._settings["priorityBColor"]))
		self._colorConfigForm.colorC.setColor(QColor(self._settings["priorityCColor"]))
		self._colorConfigForm.colorD.setColor(QColor(self._settings["priorityDColor"]))
		
		page2 = parent.addPage(self._colorConfigForm, "Colors")
		page2.setIcon(KIcon("preferences-desktop-color"))
		self.connect(parent, SIGNAL("okClicked()"), self.configAccepted)
	
	def showConfigurationInterface(self):
		dialog = KPageDialog()
		dialog.setFaceType(KPageDialog.List)
		dialog.setButtons(KDialog.ButtonCode(KDialog.Ok | KDialog.Cancel))
		self.createConfigurationInterface(dialog)
		dialog.exec_()
	
	def configAccepted(self):
		self._settings["todoURL"] = self._generalConfigForm.todourl.text()
		self._settings["showLineNumbers"] = self._generalConfigForm.linenumbers.isChecked()
		self._settings["showPriority"] = self._generalConfigForm.priorities.isChecked()
		self._settings["showProjects"] = self._generalConfigForm.projects.isChecked()
		self._settings["showContexts"] = self._generalConfigForm.contexts.isChecked()
		self._settings["priorityAColor"] = self._colorConfigForm.colorA.color().name()
		self._settings["priorityBColor"] = self._colorConfigForm.colorB.color().name()
		self._settings["priorityCColor"] = self._colorConfigForm.colorC.color().name()
		self._settings["priorityDColor"] = self._colorConfigForm.colorD.color().name()
		self._todolist.setDataPath(self._settings["todoURL"])
	
	def paintInterface(self, painter, option, rect):
		painter.save()
		#pen = QPen()                       
		painter.setPen(Qt.gray)
		#painter.setPen(Qt.black)
		painter.drawText(rect, Qt.AlignTop | Qt.AlignHCenter, "Todo List")
		#todos = self._todolist.getList()
		self._todolist.refreshList()
		todos = self._todolist.sortList()
		##painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, "Hello Python!")
		#painter.drawText(rect, Qt.AlignTop | Qt.AlignJustify, output)
		point = QPoint(15,50)
		y = 50
		for item in todos:
			# find the color to use for each priority
			if item.getPriority() == "A":
				#painter.setPen(Qt.yellow)
				painter.setPen(QColor(self._settings["priorityAColor"]))
			elif item.getPriority() == "B":
				painter.setPen(Qt.darkGreen)
			elif item.getPriority() == "C":
				painter.setPen(Qt.darkCyan)
			elif item.getPriority() == "D":
				painter.setPen(Qt.blue)
			else:
				painter.setPen(Qt.white)
			# now draw the text in the widget
			print len(item.getContexts())
			painter.drawText(point,item.getText(self._settings["showLineNumbers"],
							    self._settings["showPriority"],
							    self._settings["showProjects"],
							    self._settings["showContexts"],
							    ))
			y = y +15
			point.setY(y)
		painter.restore()
	

def CreateApplet(parent):
	return TodoApplet(parent)
