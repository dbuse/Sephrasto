# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(286, 336)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.labelVersion = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        self.labelVersion.setFont(font)
        self.labelVersion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelVersion.setObjectName("labelVersion")
        self.gridLayout.addWidget(self.labelVersion, 18, 0, 1, 1)
        self.buttonRules = QtWidgets.QPushButton(Form)
        self.buttonRules.setMinimumSize(QtCore.QSize(0, 25))
        self.buttonRules.setObjectName("buttonRules")
        self.gridLayout.addWidget(self.buttonRules, 9, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.buttonNew = QtWidgets.QPushButton(Form)
        self.buttonNew.setMinimumSize(QtCore.QSize(0, 25))
        self.buttonNew.setObjectName("buttonNew")
        self.gridLayout.addWidget(self.buttonNew, 4, 0, 1, 1)
        self.buttonEdit = QtWidgets.QPushButton(Form)
        self.buttonEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.buttonEdit.setObjectName("buttonEdit")
        self.gridLayout.addWidget(self.buttonEdit, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 13, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.vlPluginButtons = QtWidgets.QVBoxLayout()
        self.vlPluginButtons.setObjectName("vlPluginButtons")
        self.gridLayout.addLayout(self.vlPluginButtons, 7, 0, 1, 1)
        self.buttonSettings = QtWidgets.QPushButton(Form)
        self.buttonSettings.setObjectName("buttonSettings")
        self.gridLayout.addWidget(self.buttonSettings, 10, 0, 1, 1)
        self.buttonHelp = QtWidgets.QPushButton(Form)
        self.buttonHelp.setObjectName("buttonHelp")
        self.gridLayout.addWidget(self.buttonHelp, 11, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.buttonNew, self.buttonEdit)
        Form.setTabOrder(self.buttonEdit, self.buttonRules)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sephrasto"))
        self.labelVersion.setText(_translate("Form", "PLACEHOLDER"))
        self.buttonRules.setText(_translate("Form", "Regelbasis bearbeiten"))
        self.buttonNew.setText(_translate("Form", "Neuen Charakter erstellen"))
        self.buttonEdit.setText(_translate("Form", "Vorhandenen Charakter bearbeiten"))
        self.label.setText(_translate("Form", "Sephrasto"))
        self.label_2.setText(_translate("Form", "Ein Charaktergenerator für Ilaris"))
        self.buttonSettings.setText(_translate("Form", "Einstellungen"))
        self.buttonHelp.setText(_translate("Form", "Hilfe"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
