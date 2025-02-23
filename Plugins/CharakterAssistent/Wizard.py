# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wizard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formMain(object):
    def setupUi(self, formMain):
        formMain.setObjectName("formMain")
        formMain.setWindowModality(QtCore.Qt.ApplicationModal)
        formMain.resize(447, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(formMain.sizePolicy().hasHeightForWidth())
        formMain.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(formMain)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        self.cbProfession = QtWidgets.QComboBox(formMain)
        self.cbProfession.setObjectName("cbProfession")
        self.gridLayout.addWidget(self.cbProfession, 7, 1, 1, 1)
        self.cbKultur = QtWidgets.QComboBox(formMain)
        self.cbKultur.setObjectName("cbKultur")
        self.gridLayout.addWidget(self.cbKultur, 5, 1, 1, 1)
        self.lblProfession = QtWidgets.QLabel(formMain)
        self.lblProfession.setObjectName("lblProfession")
        self.gridLayout.addWidget(self.lblProfession, 7, 0, 1, 1)
        self.cbProfessionKategorie = QtWidgets.QComboBox(formMain)
        self.cbProfessionKategorie.setObjectName("cbProfessionKategorie")
        self.gridLayout.addWidget(self.cbProfessionKategorie, 6, 1, 1, 1)
        self.lblSpezies = QtWidgets.QLabel(formMain)
        self.lblSpezies.setObjectName("lblSpezies")
        self.gridLayout.addWidget(self.lblSpezies, 4, 0, 1, 1)
        self.lblGeschlecht = QtWidgets.QLabel(formMain)
        self.lblGeschlecht.setObjectName("lblGeschlecht")
        self.gridLayout.addWidget(self.lblGeschlecht, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnAccept = QtWidgets.QPushButton(formMain)
        self.btnAccept.setEnabled(True)
        self.btnAccept.setMinimumSize(QtCore.QSize(100, 0))
        self.btnAccept.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.btnAccept.setObjectName("btnAccept")
        self.horizontalLayout_3.addWidget(self.btnAccept)
        self.gridLayout.addLayout(self.horizontalLayout_3, 14, 0, 1, 2)
        self.lblRegeln = QtWidgets.QLabel(formMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblRegeln.sizePolicy().hasHeightForWidth())
        self.lblRegeln.setSizePolicy(sizePolicy)
        self.lblRegeln.setObjectName("lblRegeln")
        self.gridLayout.addWidget(self.lblRegeln, 2, 0, 1, 1)
        self.lblProfessionKategorie = QtWidgets.QLabel(formMain)
        self.lblProfessionKategorie.setObjectName("lblProfessionKategorie")
        self.gridLayout.addWidget(self.lblProfessionKategorie, 6, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnWeiblich = QtWidgets.QRadioButton(formMain)
        self.btnWeiblich.setChecked(True)
        self.btnWeiblich.setObjectName("btnWeiblich")
        self.horizontalLayout.addWidget(self.btnWeiblich)
        self.btnMaennlich = QtWidgets.QRadioButton(formMain)
        self.btnMaennlich.setObjectName("btnMaennlich")
        self.horizontalLayout.addWidget(self.btnMaennlich)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.cbRegeln = QtWidgets.QComboBox(formMain)
        self.cbRegeln.setMinimumSize(QtCore.QSize(300, 0))
        self.cbRegeln.setObjectName("cbRegeln")
        self.gridLayout.addWidget(self.cbRegeln, 2, 1, 1, 1)
        self.cbSpezies = QtWidgets.QComboBox(formMain)
        self.cbSpezies.setMinimumSize(QtCore.QSize(300, 0))
        self.cbSpezies.setObjectName("cbSpezies")
        self.gridLayout.addWidget(self.cbSpezies, 4, 1, 1, 1)
        self.lblKultur = QtWidgets.QLabel(formMain)
        self.lblKultur.setObjectName("lblKultur")
        self.gridLayout.addWidget(self.lblKultur, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(formMain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 15, 0, 1, 2)
        self.label = QtWidgets.QLabel(formMain)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 16, 0, 1, 2)

        self.retranslateUi(formMain)
        QtCore.QMetaObject.connectSlotsByName(formMain)

    def retranslateUi(self, formMain):
        _translate = QtCore.QCoreApplication.translate
        formMain.setWindowTitle(_translate("formMain", "Charakterassistent"))
        self.lblProfession.setText(_translate("formMain", "Profession"))
        self.lblSpezies.setText(_translate("formMain", "Spezies"))
        self.lblGeschlecht.setText(_translate("formMain", "Geschlecht"))
        self.btnAccept.setText(_translate("formMain", "Übernehmen"))
        self.lblRegeln.setText(_translate("formMain", "Baukasten"))
        self.lblProfessionKategorie.setText(_translate("formMain", "Professionskategorie"))
        self.btnWeiblich.setText(_translate("formMain", "Weiblich"))
        self.btnMaennlich.setText(_translate("formMain", "Männlich"))
        self.lblKultur.setText(_translate("formMain", "Kultur"))
        self.label.setToolTip(_translate("formMain", "Der Charakterassistent lebt von Communitybeiträgen. Eigene Spezies/Kulturen/Professionen/Archetypen lassen sich spielend leicht erstellen.\n"
"Finde hier heraus wie: Charakterassistent auf dsaforum.de\n"
"Lege eigene Vorlagen in den Plugins-Ordner den du in den Einstellungen festgelegt hast um diese bei neuen Sephrastoversionen nicht zu verlieren. Sie gehören in den \"Plugins/Charakterassistent/Data\" Ordner"))
        self.label.setText(_translate("formMain", "<html><head/><body><p><span style=\" font-size:6pt;\">Der Charakterassistent lebt von Communitybeiträgen. Eigene Spezies/Kulturen/Professionen/Archetypen lassen sich spielend leicht erstellen. Finde hier heraus wie und teile deine Kreationen: </span><a href=\"https://dsaforum.de/viewtopic.php?f=180&amp;t=56703\"><span style=\" font-size:6pt; text-decoration: underline; color:#0000ff;\">Charakterassistent auf dsaforum.de</span></a></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formMain = QtWidgets.QWidget()
    ui = Ui_formMain()
    ui.setupUi(formMain)
    formMain.show()
    sys.exit(app.exec_())
