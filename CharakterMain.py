# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formMain(object):
    def setupUi(self, formMain):
        formMain.setObjectName("formMain")
        formMain.setWindowModality(QtCore.Qt.ApplicationModal)
        formMain.resize(1093, 541)
        self.gridLayout = QtWidgets.QGridLayout(formMain)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkReq = QtWidgets.QCheckBox(formMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkReq.sizePolicy().hasHeightForWidth())
        self.checkReq.setSizePolicy(sizePolicy)
        self.checkReq.setMinimumSize(QtCore.QSize(125, 0))
        self.checkReq.setChecked(True)
        self.checkReq.setObjectName("checkReq")
        self.horizontalLayout_3.addWidget(self.checkReq)
        self.progressBar = QtWidgets.QProgressBar(formMain)
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximumSize(QtCore.QSize(305, 16777215))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.buttonQuicksave = QtWidgets.QPushButton(formMain)
        self.buttonQuicksave.setMinimumSize(QtCore.QSize(75, 0))
        self.buttonQuicksave.setObjectName("buttonQuicksave")
        self.horizontalLayout_3.addWidget(self.buttonQuicksave)
        self.buttonSave = QtWidgets.QPushButton(formMain)
        self.buttonSave.setMinimumSize(QtCore.QSize(75, 0))
        self.buttonSave.setObjectName("buttonSave")
        self.horizontalLayout_3.addWidget(self.buttonSave)
        self.buttonSavePDF = QtWidgets.QPushButton(formMain)
        self.buttonSavePDF.setMinimumSize(QtCore.QSize(100, 0))
        self.buttonSavePDF.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.buttonSavePDF.setObjectName("buttonSavePDF")
        self.horizontalLayout_3.addWidget(self.buttonSavePDF)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabs = QtWidgets.QTabWidget(formMain)
        self.tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabs.setElideMode(QtCore.Qt.ElideRight)
        self.tabs.setDocumentMode(False)
        self.tabs.setObjectName("tabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabs.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabs)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(formMain)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinEP = QtWidgets.QSpinBox(formMain)
        self.spinEP.setAlignment(QtCore.Qt.AlignCenter)
        self.spinEP.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinEP.setMaximum(100000)
        self.spinEP.setObjectName("spinEP")
        self.horizontalLayout_2.addWidget(self.spinEP)
        self.label_3 = QtWidgets.QLabel(formMain)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinSpent = QtWidgets.QSpinBox(formMain)
        self.spinSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinSpent.setReadOnly(True)
        self.spinSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinSpent.setMinimum(-100000)
        self.spinSpent.setMaximum(100000)
        self.spinSpent.setObjectName("spinSpent")
        self.horizontalLayout_2.addWidget(self.spinSpent)
        self.label_2 = QtWidgets.QLabel(formMain)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinRemaining = QtWidgets.QSpinBox(formMain)
        self.spinRemaining.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinRemaining.setAutoFillBackground(False)
        self.spinRemaining.setAlignment(QtCore.Qt.AlignCenter)
        self.spinRemaining.setReadOnly(True)
        self.spinRemaining.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinRemaining.setMinimum(-100000)
        self.spinRemaining.setMaximum(100000)
        self.spinRemaining.setObjectName("spinRemaining")
        self.horizontalLayout_2.addWidget(self.spinRemaining)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(formMain)
        self.tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(formMain)
        formMain.setTabOrder(self.tabs, self.spinEP)
        formMain.setTabOrder(self.spinEP, self.spinSpent)
        formMain.setTabOrder(self.spinSpent, self.spinRemaining)
        formMain.setTabOrder(self.spinRemaining, self.checkReq)
        formMain.setTabOrder(self.checkReq, self.buttonQuicksave)
        formMain.setTabOrder(self.buttonQuicksave, self.buttonSave)
        formMain.setTabOrder(self.buttonSave, self.buttonSavePDF)

    def retranslateUi(self, formMain):
        _translate = QtCore.QCoreApplication.translate
        formMain.setWindowTitle(_translate("formMain", "Sephrasto - Charakter erstellen"))
        self.checkReq.setText(_translate("formMain", "Voraussetzungen überprüfen"))
        self.buttonQuicksave.setText(_translate("formMain", "Speichern"))
        self.buttonSave.setText(_translate("formMain", "Speichern als..."))
        self.buttonSavePDF.setText(_translate("formMain", "PDF erstellen"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("formMain", "Tab 1"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("formMain", "Tab 2"))
        self.label.setText(_translate("formMain", "    Total:    "))
        self.spinEP.setSuffix(_translate("formMain", " EP"))
        self.label_3.setText(_translate("formMain", "    Ausgegeben:    "))
        self.spinSpent.setSuffix(_translate("formMain", " EP"))
        self.label_2.setText(_translate("formMain", "    Verbleibend:    "))
        self.spinRemaining.setSuffix(_translate("formMain", " EP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formMain = QtWidgets.QWidget()
    ui = Ui_formMain()
    ui.setupUi(formMain)
    formMain.show()
    sys.exit(app.exec_())
