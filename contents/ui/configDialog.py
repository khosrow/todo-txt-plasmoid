# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configDialog.ui'
#
# Created: Sun Feb 13 22:29:18 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.kcolorbutton = KColorButton(Dialog)
        self.kcolorbutton.setGeometry(QtCore.QRect(101, 150, 72, 24))
        self.kcolorbutton.setObjectName("kcolorbutton")
        self.kcolorbutton_2 = KColorButton(Dialog)
        self.kcolorbutton_2.setGeometry(QtCore.QRect(101, 178, 72, 24))
        self.kcolorbutton_2.setObjectName("kcolorbutton_2")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(31, 31, 141, 16))
        self.label.setObjectName("label")
        self.kurlcomborequester = KUrlComboRequester(Dialog)
        self.kurlcomborequester.setGeometry(QtCore.QRect(170, 30, 99, 25))
        self.kurlcomborequester.setObjectName("kurlcomborequester")
        self.kcolorbutton_3 = KColorButton(Dialog)
        self.kcolorbutton_3.setGeometry(QtCore.QRect(101, 206, 72, 24))
        self.kcolorbutton_3.setObjectName("kcolorbutton_3")
        self.kcolorbutton_4 = KColorButton(Dialog)
        self.kcolorbutton_4.setGeometry(QtCore.QRect(101, 234, 72, 24))
        self.kcolorbutton_4.setObjectName("kcolorbutton_4")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 251, 171))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 191, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 241, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 206, 57, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 234, 57, 16))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 178, 57, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 57, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "todo.txt file location:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Priority Colours", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "A", None, QtGui.QApplication.UnicodeUTF8))

from PyKDE4.kio import KUrlComboRequester
from PyKDE4.kdeui import KColorButton

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

