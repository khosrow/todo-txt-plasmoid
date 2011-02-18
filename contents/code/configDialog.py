# -*- coding: iso-8859-1 -*-
from PyQt4 import QtCore, QtGui
from configDialogUi import Ui_ConfigDialog

class ConfigDialog(QtGui.QWidget, Ui_ConfigDialog):
    def __init__(self, parent, settings):
	QtGui.QWidget.__init__(self)
	self.setupUi(self)
	self.parent = parent
	self.todoURL.setText(str(settings["todoURL"]))	
	self.priorityAColour.setValue(settings["priorityAColour"])
	self.priorityBColour.setValue(settings["priorityBColour"])
	self.priorityCColour.setValue(settings["priorityCColour"])
	self.priorityDColour.setValue(settings["priorityDColour"])

    def getSettings(self):
	settings = {}
	settings["todoURL"] = self.todoURL.text()
	settings["priorityAColour"] = self.priorityAColour.value()
	settings["priorityBColour"] = self.priorityBColour.value()
	settings["priorityCColour"] = self.priorityCColour.value()
	settings["priorityDColour"] = self.priorityDColour.value()