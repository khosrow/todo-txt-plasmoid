# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created: Mon Feb 21 22:09:17 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(306, 313)
        self.fileGroupBox = QtGui.QGroupBox(Form)
        self.fileGroupBox.setGeometry(QtCore.QRect(10, 10, 281, 81))
        self.fileGroupBox.setObjectName("fileGroupBox")
        self.todourl = KUrlComboRequester(self.fileGroupBox)
        self.todourl.setGeometry(QtCore.QRect(20, 30, 241, 25))
        self.todourl.setObjectName("todourl")
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 281, 161))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 231, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.prioritybcolour = KColorButton(self.layoutWidget)
        self.prioritybcolour.setObjectName("prioritybcolour")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.prioritybcolour)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.priorityccolour = KColorButton(self.layoutWidget)
        self.priorityccolour.setObjectName("priorityccolour")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.priorityccolour)
        self.priorityacolour = KColorButton(self.layoutWidget)
        self.priorityacolour.setObjectName("priorityacolour")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.priorityacolour)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.fileGroupBox.setTitle(QtGui.QApplication.translate("Form", "todo File", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Colours", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Priority A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Priority B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Prority C", None, QtGui.QApplication.UnicodeUTF8))

from PyKDE4.kio import KUrlComboRequester
from PyKDE4.kdeui import KColorButton
