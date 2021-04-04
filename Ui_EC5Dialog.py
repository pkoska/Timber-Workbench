# -*- coding: utf-8 -*-
#***************************************************************************
#*   (c) Jonathan Wiedemann (jonatan@wiedemann.fr) 2013                    *
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   FreeCAD is distributed in the hope that it will be useful,            *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#*   Jonathan Wiedemann 2013                                               *
#***************************************************************************/
#
# Created: Sun Dec 15 13:47:06 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import QT_TRANSLATE_NOOP

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(365, 504)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(350, 500))
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setMinimumSize(QtCore.QSize(350, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 332, 739))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboBox_2 = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_8.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBox_8.setMaximum(99999.0)
        self.doubleSpinBox_8.setSingleStep(10.0)
        self.doubleSpinBox_8.setProperty("value", 75.0)
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.horizontalLayout.addWidget(self.doubleSpinBox_8)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.doubleSpinBox_9 = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_9.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBox_9.setMaximum(99999.0)
        self.doubleSpinBox_9.setSingleStep(10.0)
        self.doubleSpinBox_9.setProperty("value", 220.0)
        self.doubleSpinBox_9.setObjectName(_fromUtf8("doubleSpinBox_9"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_9)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_16 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setMinimumSize(QtCore.QSize(0, 0))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_17.addWidget(self.label_16)
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_7.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBox_7.setMaximum(99999.0)
        self.doubleSpinBox_7.setSingleStep(100.0)
        self.doubleSpinBox_7.setProperty("value", 4500.0)
        self.doubleSpinBox_7.setObjectName(_fromUtf8("doubleSpinBox_7"))
        self.horizontalLayout_17.addWidget(self.doubleSpinBox_7)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_15.addWidget(self.label_7)
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_15.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBox.setPrefix(_fromUtf8(""))
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setProperty("value", 3.7)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.horizontalLayout_6.addWidget(self.doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_10 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_9.addWidget(self.label_10)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBox_3.setMaximum(2.0)
        self.doubleSpinBox_3.setProperty("value", 1.0)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_11 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_10.addWidget(self.label_11)
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBox_4.setProperty("value", 1.0)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.horizontalLayout_10.addWidget(self.doubleSpinBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_12 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_11.addWidget(self.label_12)
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_5.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBox_5.setMinimum(1.0)
        self.doubleSpinBox_5.setMaximum(1.1)
        self.doubleSpinBox_5.setSingleStep(0.1)
        self.doubleSpinBox_5.setProperty("value", 1.0)
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
        self.horizontalLayout_11.addWidget(self.doubleSpinBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.horizontalLayout_14.addWidget(self.textBrowser_2)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_13 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_16.addWidget(self.label_13)
        self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_16.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBox_2.setMaximum(99999.0)
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_2.setProperty("value", 3.5)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_14 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_12.addWidget(self.label_14)
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_6.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBox_6.setMaximum(2.0)
        self.doubleSpinBox_6.setProperty("value", 1.0)
        self.doubleSpinBox_6.setObjectName(_fromUtf8("doubleSpinBox_6"))
        self.horizontalLayout_12.addWidget(self.doubleSpinBox_6)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_13.addWidget(self.label_15)
        self.doubleSpinBox_10 = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_10.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBox_10.setMaximum(99999.0)
        self.doubleSpinBox_10.setSingleStep(10.0)
        self.doubleSpinBox_10.setProperty("value", 100.0)
        self.doubleSpinBox_10.setObjectName(_fromUtf8("doubleSpinBox_10"))
        self.horizontalLayout_13.addWidget(self.doubleSpinBox_10)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayout_8.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QT_TRANSLATE_NOOP("Dialog", "Dialog"))
        self.label_3.setText(QT_TRANSLATE_NOOP("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Poutre 2 appuis - </span>Flexion et Cisaillement </p><p>Eurocodes 5</p></body></html>"))
        self.label_6.setText(QT_TRANSLATE_NOOP("Dialog", "Récuperer données"))
        self.pushButton_3.setText(QT_TRANSLATE_NOOP("Dialog", "Element"))
        self.label_5.setText(QT_TRANSLATE_NOOP("Dialog", "Materiaux"))
        self.comboBox_2.setItemText(0, QT_TRANSLATE_NOOP("Dialog", "Bois Massif"))
        self.comboBox_2.setItemText(1, QT_TRANSLATE_NOOP("Dialog", "Lamellé Collé"))
        self.label_4.setText(QT_TRANSLATE_NOOP("Dialog", "Classe mécanique"))
        self.comboBox.setItemText(0, QT_TRANSLATE_NOOP("Dialog", "C18"))
        self.comboBox.setItemText(1, QT_TRANSLATE_NOOP("Dialog", "C24"))
        self.label.setText(QT_TRANSLATE_NOOP("Dialog", "Base"))
        self.doubleSpinBox_8.setSuffix(QT_TRANSLATE_NOOP("Dialog", " mm"))
        self.label_2.setText(QT_TRANSLATE_NOOP("Dialog", "Hauteur"))
        self.doubleSpinBox_9.setSuffix(QT_TRANSLATE_NOOP("Dialog", " mm"))
        self.label_16.setText(QT_TRANSLATE_NOOP("Dialog", "Longueur"))
        self.doubleSpinBox_7.setSuffix(QT_TRANSLATE_NOOP("Dialog", " mm"))
        self.label_7.setText(QT_TRANSLATE_NOOP("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Vérification de la flexion</span></p></body></html>"))
        self.pushButton.setText(QT_TRANSLATE_NOOP("Dialog", "Vérifier !"))
        self.label_8.setText(QT_TRANSLATE_NOOP("Dialog", "Moment fléchissant Max"))
        self.doubleSpinBox.setSuffix(QT_TRANSLATE_NOOP("Dialog", " MPa"))
        self.label_10.setText(QT_TRANSLATE_NOOP("Dialog", "Kmod associé"))
        self.label_11.setText(QT_TRANSLATE_NOOP("Dialog", "Kcrit associé"))
        self.label_12.setText(QT_TRANSLATE_NOOP("Dialog", "Ksys associé"))
        self.textBrowser_2.setHtml(QT_TRANSLATE_NOOP("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Contrainte de flexion induite : ---</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Resistance de calcul en flexion : ---</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Taux de travail : --- %</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">Ok</span>/<span style=\" color:#ff0000;\">NOK</span></p></body></html>"))
        self.label_13.setText(QT_TRANSLATE_NOOP("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Vérification du cisaillement</span></p></body></html>"))
        self.pushButton_2.setText(QT_TRANSLATE_NOOP("Dialog", "Vérifier !"))
        self.label_9.setText(QT_TRANSLATE_NOOP("Dialog", "Effort Tranchant Max"))
        self.doubleSpinBox_2.setSuffix(QT_TRANSLATE_NOOP("Dialog", " MPa"))
        self.label_14.setText(QT_TRANSLATE_NOOP("Dialog", "Kmod associé"))
        self.label_15.setText(QT_TRANSLATE_NOOP("Dialog", "Hauteur efficace"))
        self.doubleSpinBox_10.setSuffix(QT_TRANSLATE_NOOP("Dialog", " mm"))
        self.textBrowser.setHtml(QT_TRANSLATE_NOOP("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Contrainte de flexion induite : ---</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Resistance de calcul en flexion : ---</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Taux de travail : --- %</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">Ok</span>/<span style=\" color:#ff0000;\">NOK</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())