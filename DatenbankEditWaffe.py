# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatenbankEditWaffe.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_talentDialog(object):
    def setupUi(self, talentDialog):
        talentDialog.setObjectName("talentDialog")
        talentDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        talentDialog.resize(440, 550)
        self.gridLayout_2 = QtWidgets.QGridLayout(talentDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.spinHaerte = QtWidgets.QSpinBox(talentDialog)
        self.spinHaerte.setMinimumSize(QtCore.QSize(50, 0))
        self.spinHaerte.setAlignment(QtCore.Qt.AlignCenter)
        self.spinHaerte.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinHaerte.setMinimum(0)
        self.spinHaerte.setMaximum(99)
        self.spinHaerte.setProperty("value", 7)
        self.spinHaerte.setObjectName("spinHaerte")
        self.horizontalLayout_6.addWidget(self.spinHaerte)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(talentDialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(talentDialog)
        self.label_4.setMinimumSize(QtCore.QSize(110, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboTyp = QtWidgets.QComboBox(talentDialog)
        self.comboTyp.setObjectName("comboTyp")
        self.comboTyp.addItem("")
        self.comboTyp.addItem("")
        self.horizontalLayout_2.addWidget(self.comboTyp)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.spinRW1 = QtWidgets.QSpinBox(talentDialog)
        self.spinRW1.setMinimumSize(QtCore.QSize(50, 0))
        self.spinRW1.setAlignment(QtCore.Qt.AlignCenter)
        self.spinRW1.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinRW1.setMaximum(999)
        self.spinRW1.setProperty("value", 1)
        self.spinRW1.setObjectName("spinRW1")
        self.horizontalLayout_4.addWidget(self.spinRW1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(talentDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(talentDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(talentDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 10, 0, 1, 1)
        self.labelWMLZ = QtWidgets.QLabel(talentDialog)
        self.labelWMLZ.setObjectName("labelWMLZ")
        self.gridLayout.addWidget(self.labelWMLZ, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(talentDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(talentDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.spinWMLZ = QtWidgets.QSpinBox(talentDialog)
        self.spinWMLZ.setMinimumSize(QtCore.QSize(50, 0))
        self.spinWMLZ.setAlignment(QtCore.Qt.AlignCenter)
        self.spinWMLZ.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinWMLZ.setMinimum(-9)
        self.spinWMLZ.setMaximum(9)
        self.spinWMLZ.setObjectName("spinWMLZ")
        self.horizontalLayout_5.addWidget(self.spinWMLZ)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)
        self.textEigenschaften = QtWidgets.QPlainTextEdit(talentDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEigenschaften.sizePolicy().hasHeightForWidth())
        self.textEigenschaften.setSizePolicy(sizePolicy)
        self.textEigenschaften.setObjectName("textEigenschaften")
        self.gridLayout.addWidget(self.textEigenschaften, 10, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(talentDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.spinW6 = QtWidgets.QSpinBox(talentDialog)
        self.spinW6.setAlignment(QtCore.Qt.AlignCenter)
        self.spinW6.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinW6.setMinimum(0)
        self.spinW6.setMaximum(19)
        self.spinW6.setProperty("value", 2)
        self.spinW6.setObjectName("spinW6")
        self.horizontalLayout.addWidget(self.spinW6)
        self.label_7 = QtWidgets.QLabel(talentDialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.spinPlus = QtWidgets.QSpinBox(talentDialog)
        self.spinPlus.setMinimumSize(QtCore.QSize(50, 0))
        self.spinPlus.setAlignment(QtCore.Qt.AlignCenter)
        self.spinPlus.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinPlus.setMinimum(-9)
        self.spinPlus.setProperty("value", 2)
        self.spinPlus.setObjectName("spinPlus")
        self.horizontalLayout.addWidget(self.spinPlus)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(talentDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.comboTalent = QtWidgets.QComboBox(talentDialog)
        self.comboTalent.setObjectName("comboTalent")
        self.gridLayout.addWidget(self.comboTalent, 8, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(talentDialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.comboFert = QtWidgets.QComboBox(talentDialog)
        self.comboFert.setObjectName("comboFert")
        self.gridLayout.addWidget(self.comboFert, 7, 1, 1, 1)
        self.layoutKampfstile = QtWidgets.QGridLayout()
        self.layoutKampfstile.setObjectName("layoutKampfstile")
        self.gridLayout.addLayout(self.layoutKampfstile, 9, 1, 1, 1)
        self.warning = QtWidgets.QLabel(talentDialog)
        self.warning.setVisible(False)
        self.warning.setStyleSheet("background-color: rgb(255, 255, 0); color: black;")
        self.warning.setWordWrap(True)
        self.warning.setObjectName("warning")
        self.gridLayout.addWidget(self.warning, 0, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(talentDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(talentDialog)
        self.buttonBox.accepted.connect(talentDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(talentDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(talentDialog)
        talentDialog.setTabOrder(self.nameEdit, self.comboTyp)
        talentDialog.setTabOrder(self.comboTyp, self.spinW6)
        talentDialog.setTabOrder(self.spinW6, self.spinPlus)
        talentDialog.setTabOrder(self.spinPlus, self.spinRW1)
        talentDialog.setTabOrder(self.spinRW1, self.spinWMLZ)
        talentDialog.setTabOrder(self.spinWMLZ, self.spinHaerte)
        talentDialog.setTabOrder(self.spinHaerte, self.comboFert)
        talentDialog.setTabOrder(self.comboFert, self.comboTalent)
        talentDialog.setTabOrder(self.comboTalent, self.textEigenschaften)

    def retranslateUi(self, talentDialog):
        _translate = QtCore.QCoreApplication.translate
        talentDialog.setWindowTitle(_translate("talentDialog", "Sephrasto - Waffe bearbeiten..."))
        self.label_9.setText(_translate("talentDialog", "Härte"))
        self.label_4.setText(_translate("talentDialog", "Reichweite"))
        self.comboTyp.setItemText(0, _translate("talentDialog", "Nahkampfwaffe"))
        self.comboTyp.setItemText(1, _translate("talentDialog", "Fernkampfwaffe"))
        self.label.setText(_translate("talentDialog", "Waffenname"))
        self.label_5.setText(_translate("talentDialog", "Eigenschaften"))
        self.labelWMLZ.setText(_translate("talentDialog", "WM/LZ"))
        self.label_2.setText(_translate("talentDialog", "Typ"))
        self.label_3.setText(_translate("talentDialog", "Trefferpunkte"))
        self.label_6.setText(_translate("talentDialog", "Fertigkeit"))
        self.spinW6.setSuffix(_translate("talentDialog", " W6"))
        self.label_7.setText(_translate("talentDialog", "+"))
        self.label_8.setText(_translate("talentDialog", "Talent"))
        self.label_10.setText(_translate("talentDialog", "Kampfstil"))
        self.warning.setText(_translate("talentDialog", "<html><head/><body><p>Dies ist eine Ilaris-Standardwaffe. Sobald du hier etwas veränderst, bekommst du eine persönliche Kopie und das Original wird in den Hausregeln gelöscht. Damit erhältst du für diese Waffe keine automatischen Updates mehr mit neuen Sephrasto-Versionen.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    talentDialog = QtWidgets.QDialog()
    ui = Ui_talentDialog()
    ui.setupUi(talentDialog)
    talentDialog.show()
    sys.exit(app.exec_())
