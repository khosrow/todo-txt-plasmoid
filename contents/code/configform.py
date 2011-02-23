# -*- coding: iso-8859-1 -*-
from PyQt4 import QtCore, QtGui
from configformui import Ui_Form

class ConfigForm(QtGui.QWidget, Ui_Form):
    def __init__(self, parent, settings):
	QtGui.QWidget.__init__(self)
	self.parent = parent
	self.setupUi(self)
	self.todourl.setText(str(settings["todoURL"]))	
	#self.priorityAColour.setValue(settings["priorityAColour"])
	#self.priorityBColour.setValue(settings["priorityBColour"])
	#self.priorityCColour.setValue(settings["priorityCColour"])
	#self.priorityDColour.setValue(settings["priorityDColour"])

    def getSettings(self):
	settings = {}
	settings["todoURL"] = self.todourl.text()
	#settings["priorityAColour"] = self.priorityAColour.value()
	#settings["priorityBColour"] = self.priorityBColour.value()
	#settings["priorityCColour"] = self.priorityCColour.value()
	#settings["priorityDColour"] = self.priorityDColour.value()