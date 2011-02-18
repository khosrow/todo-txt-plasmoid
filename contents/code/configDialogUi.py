# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configDialog.ui'
#
# Created: Fri Feb 18 15:16:05 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        ConfigDialog.setObjectName("ConfigDialog")
        ConfigDialog.resize(369, 253)
        self.FileLabel = QtGui.QLabel(ConfigDialog)
        self.FileLabel.setGeometry(QtCore.QRect(11, 11, 25, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.FileLabel.setFont(font)
        self.FileLabel.setObjectName("FileLabel")
        self.ColourLabel = QtGui.QLabel(ConfigDialog)
        self.ColourLabel.setGeometry(QtCore.QRect(10, 100, 111, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.ColourLabel.setFont(font)
        self.ColourLabel.setObjectName("ColourLabel")
        self.widget = QtGui.QWidget(ConfigDialog)
        self.widget.setGeometry(QtCore.QRect(20, 120, 181, 129))
        self.widget.setObjectName("widget")
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.priorityALabel = QtGui.QLabel(self.widget)
        self.priorityALabel.setObjectName("priorityALabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.priorityALabel)
        self.priorityBLabel = QtGui.QLabel(self.widget)
        self.priorityBLabel.setObjectName("priorityBLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.priorityBLabel)
        self.priorityBColour = KColorButton(self.widget)
        self.priorityBColour.setObjectName("priorityBColour")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.priorityBColour)
        self.priorityCLabel = QtGui.QLabel(self.widget)
        self.priorityCLabel.setObjectName("priorityCLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.priorityCLabel)
        self.priorityCColour = KColorButton(self.widget)
        self.priorityCColour.setObjectName("priorityCColour")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.priorityCColour)
        self.priorityDLabel = QtGui.QLabel(self.widget)
        self.priorityDLabel.setObjectName("priorityDLabel")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.priorityDLabel)
        self.priorityDColour = KColorButton(self.widget)
        self.priorityDColour.setObjectName("priorityDColour")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.priorityDColour)
        self.priorityAColour = KColorButton(self.widget)
        self.priorityAColour.setObjectName("priorityAColour")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.priorityAColour)
        self.widget1 = QtGui.QWidget(ConfigDialog)
        self.widget1.setGeometry(QtCore.QRect(19, 31, 341, 51))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.todoFileLabel = QtGui.QLabel(self.widget1)
        self.todoFileLabel.setObjectName("todoFileLabel")
        self.verticalLayout.addWidget(self.todoFileLabel)
        self.todoURL = KUrlComboRequester(self.widget1)
        self.todoURL.setObjectName("todoURL")
        self.verticalLayout.addWidget(self.todoURL)

        self.retranslateUi(ConfigDialog)
        QtCore.QObject.connect(self.todoURL, QtCore.SIGNAL("openFileDialog(KUrlRequester*)"), ConfigDialog.update)
        QtCore.QObject.connect(self.priorityAColour, QtCore.SIGNAL("changed(QColor)"), ConfigDialog.update)
        QtCore.QObject.connect(self.priorityBColour, QtCore.SIGNAL("changed(QColor)"), ConfigDialog.update)
        QtCore.QObject.connect(self.priorityCColour, QtCore.SIGNAL("changed(QColor)"), ConfigDialog.update)
        QtCore.QObject.connect(self.priorityDColour, QtCore.SIGNAL("changed(QColor)"), ConfigDialog.update)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)
        ConfigDialog.setTabOrder(self.todoURL, self.priorityAColour)
        ConfigDialog.setTabOrder(self.priorityAColour, self.priorityBColour)
        ConfigDialog.setTabOrder(self.priorityBColour, self.priorityCColour)
        ConfigDialog.setTabOrder(self.priorityCColour, self.priorityDColour)

    def retranslateUi(self, ConfigDialog):
        ConfigDialog.setWindowTitle(QtGui.QApplication.translate("ConfigDialog", "todo.txt Plasmoid Config Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.FileLabel.setText(QtGui.QApplication.translate("ConfigDialog", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.ColourLabel.setText(QtGui.QApplication.translate("ConfigDialog", "Priority Colours", None, QtGui.QApplication.UnicodeUTF8))
        self.priorityALabel.setText(QtGui.QApplication.translate("ConfigDialog", "Priority A", None, QtGui.QApplication.UnicodeUTF8))
        self.priorityBLabel.setText(QtGui.QApplication.translate("ConfigDialog", "Priority B", None, QtGui.QApplication.UnicodeUTF8))
        self.priorityCLabel.setText(QtGui.QApplication.translate("ConfigDialog", "Priority C", None, QtGui.QApplication.UnicodeUTF8))
        self.priorityDLabel.setText(QtGui.QApplication.translate("ConfigDialog", "Priority D", None, QtGui.QApplication.UnicodeUTF8))
        self.todoFileLabel.setText(QtGui.QApplication.translate("ConfigDialog", "todo.txt location", None, QtGui.QApplication.UnicodeUTF8))

from PyKDE4.kio import KUrlComboRequester
from PyKDE4.kdeui import KColorButton
