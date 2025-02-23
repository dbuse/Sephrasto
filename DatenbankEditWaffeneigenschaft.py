# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatenbankEditWaffeneigenschaft.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_waffeneigenschaftDialog(object):
    def setupUi(self, waffeneigenschaftDialog):
        waffeneigenschaftDialog.setObjectName("waffeneigenschaftDialog")
        waffeneigenschaftDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        waffeneigenschaftDialog.resize(440, 334)
        self.gridLayout_2 = QtWidgets.QGridLayout(waffeneigenschaftDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(waffeneigenschaftDialog)
        self.label_3.setMinimumSize(QtCore.QSize(110, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(waffeneigenschaftDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 1, 1, 1, 1)
        self.textEdit = QtWidgets.QPlainTextEdit(waffeneigenschaftDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(waffeneigenschaftDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scriptEdit = QtWidgets.QLineEdit(waffeneigenschaftDialog)
        self.scriptEdit.setObjectName("scriptEdit")
        self.horizontalLayout.addWidget(self.scriptEdit)
        self.scriptPrioEdit = QtWidgets.QSpinBox(waffeneigenschaftDialog)
        self.scriptPrioEdit.setMinimum(-10)
        self.scriptPrioEdit.setMaximum(10)
        self.scriptPrioEdit.setSingleStep(1)
        self.scriptPrioEdit.setProperty("value", 0)
        self.scriptPrioEdit.setObjectName("scriptPrioEdit")
        self.horizontalLayout.addWidget(self.scriptPrioEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.warning = QtWidgets.QLabel(waffeneigenschaftDialog)
        self.warning.setVisible(False)
        self.warning.setStyleSheet("background-color: rgb(255, 255, 0); color: black;")
        self.warning.setWordWrap(True)
        self.warning.setObjectName("warning")
        self.gridLayout.addWidget(self.warning, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(waffeneigenschaftDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(waffeneigenschaftDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(waffeneigenschaftDialog)
        self.buttonBox.accepted.connect(waffeneigenschaftDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(waffeneigenschaftDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(waffeneigenschaftDialog)
        waffeneigenschaftDialog.setTabOrder(self.nameEdit, self.textEdit)

    def retranslateUi(self, waffeneigenschaftDialog):
        _translate = QtCore.QCoreApplication.translate
        waffeneigenschaftDialog.setWindowTitle(_translate("waffeneigenschaftDialog", "Sephrasto - Waffeneigenschaft bearbeiten..."))
        self.label_3.setText(_translate("waffeneigenschaftDialog", "Script / Priorität"))
        self.label_5.setText(_translate("waffeneigenschaftDialog", "Beschreibung"))
        self.warning.setText(_translate("waffeneigenschaftDialog", "<html><head/><body><p>Dies ist eine Ilaris-Standardwaffeneigenschaft. Sobald du hier etwas veränderst, bekommst du eine persönliche Kopie und das Original wird in den Hausregeln gelöscht. Damit erhältst du für diese Waffeneigenschaft keine automatischen Updates mehr mit neuen Sephrasto-Versionen.</p></body></html>"))
        self.label.setText(_translate("waffeneigenschaftDialog", "Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    waffeneigenschaftDialog = QtWidgets.QDialog()
    ui = Ui_waffeneigenschaftDialog()
    ui.setupUi(waffeneigenschaftDialog)
    waffeneigenschaftDialog.show()
    sys.exit(app.exec_())
