# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mineconfig_ui.ui'
#
# Created: Fri Feb 28 14:45:09 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        ConfigDialog.setObjectName(_fromUtf8("ConfigDialog"))
        ConfigDialog.setWindowModality(QtCore.Qt.WindowModal)
        ConfigDialog.resize(470, 362)
        ConfigDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(ConfigDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(ConfigDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinMapWidth = QtGui.QSpinBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinMapWidth.setFont(font)
        self.spinMapWidth.setProperty("value", 10)
        self.spinMapWidth.setObjectName(_fromUtf8("spinMapWidth"))
        self.gridLayout.addWidget(self.spinMapWidth, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinMapHeight = QtGui.QSpinBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinMapHeight.setFont(font)
        self.spinMapHeight.setProperty("value", 10)
        self.spinMapHeight.setObjectName(_fromUtf8("spinMapHeight"))
        self.gridLayout.addWidget(self.spinMapHeight, 1, 1, 1, 1)
        self.horizontalLayout_9.addLayout(self.gridLayout)
        spacerItem2 = QtGui.QSpacerItem(32, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.tab_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.radioButtonRandomMines = QtGui.QRadioButton(self.tab_2)
        self.radioButtonRandomMines.setText(_fromUtf8(""))
        self.radioButtonRandomMines.setChecked(True)
        self.radioButtonRandomMines.setObjectName(_fromUtf8("radioButtonRandomMines"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.radioButtonRandomMines)
        self.groupBoxRandomMines = QtGui.QGroupBox(self.tab_2)
        self.groupBoxRandomMines.setObjectName(_fromUtf8("groupBoxRandomMines"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBoxRandomMines)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_8 = QtGui.QLabel(self.groupBoxRandomMines)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.spinMineNumber = QtGui.QSpinBox(self.groupBoxRandomMines)
        self.spinMineNumber.setMinimum(1)
        self.spinMineNumber.setMaximum(50)
        self.spinMineNumber.setProperty("value", 5)
        self.spinMineNumber.setObjectName(_fromUtf8("spinMineNumber"))
        self.horizontalLayout_4.addWidget(self.spinMineNumber)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.mineNumberSlider = QtGui.QSlider(self.groupBoxRandomMines)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineNumberSlider.setFont(font)
        self.mineNumberSlider.setMinimum(1)
        self.mineNumberSlider.setMaximum(50)
        self.mineNumberSlider.setProperty("value", 5)
        self.mineNumberSlider.setSliderPosition(5)
        self.mineNumberSlider.setOrientation(QtCore.Qt.Horizontal)
        self.mineNumberSlider.setTickInterval(0)
        self.mineNumberSlider.setObjectName(_fromUtf8("mineNumberSlider"))
        self.verticalLayout_3.addWidget(self.mineNumberSlider)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.groupBoxRandomMines)
        self.radioButtonFixedMines = QtGui.QRadioButton(self.tab_2)
        self.radioButtonFixedMines.setText(_fromUtf8(""))
        self.radioButtonFixedMines.setObjectName(_fromUtf8("radioButtonFixedMines"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.radioButtonFixedMines)
        self.groupBoxInfoMines = QtGui.QGroupBox(self.tab_2)
        self.groupBoxInfoMines.setEnabled(False)
        self.groupBoxInfoMines.setObjectName(_fromUtf8("groupBoxInfoMines"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBoxInfoMines)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.TWMinesPos = QtGui.QTableWidget(self.groupBoxInfoMines)
        self.TWMinesPos.setMaximumSize(QtCore.QSize(244, 16777215))
        self.TWMinesPos.setLineWidth(0)
        self.TWMinesPos.setObjectName(_fromUtf8("TWMinesPos"))
        self.TWMinesPos.setColumnCount(2)
        self.TWMinesPos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.TWMinesPos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.TWMinesPos.setHorizontalHeaderItem(1, item)
        self.verticalLayout_7.addWidget(self.TWMinesPos)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.addBtn = QtGui.QToolButton(self.groupBoxInfoMines)
        self.addBtn.setMinimumSize(QtCore.QSize(30, 0))
        self.addBtn.setObjectName(_fromUtf8("addBtn"))
        self.horizontalLayout_5.addWidget(self.addBtn)
        self.minusBtn = QtGui.QToolButton(self.groupBoxInfoMines)
        self.minusBtn.setMinimumSize(QtCore.QSize(30, 0))
        self.minusBtn.setObjectName(_fromUtf8("minusBtn"))
        self.horizontalLayout_5.addWidget(self.minusBtn)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.groupBoxInfoMines)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_6.addWidget(self.label_9)
        self.spinBoxMinDistDetection = QtGui.QSpinBox(self.tab_3)
        self.spinBoxMinDistDetection.setMaximum(100)
        self.spinBoxMinDistDetection.setProperty("value", 5)
        self.spinBoxMinDistDetection.setObjectName(_fromUtf8("spinBoxMinDistDetection"))
        self.horizontalLayout_6.addWidget(self.spinBoxMinDistDetection)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalSliderMinDistDetection = QtGui.QSlider(self.tab_3)
        self.horizontalSliderMinDistDetection.setMaximum(100)
        self.horizontalSliderMinDistDetection.setProperty("value", 5)
        self.horizontalSliderMinDistDetection.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderMinDistDetection.setObjectName(_fromUtf8("horizontalSliderMinDistDetection"))
        self.verticalLayout_6.addWidget(self.horizontalSliderMinDistDetection)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_8.addWidget(self.label_10)
        self.spinBoxMaxDistExplosion = QtGui.QSpinBox(self.tab_3)
        self.spinBoxMaxDistExplosion.setMaximum(100)
        self.spinBoxMaxDistExplosion.setProperty("value", 5)
        self.spinBoxMaxDistExplosion.setObjectName(_fromUtf8("spinBoxMaxDistExplosion"))
        self.horizontalLayout_8.addWidget(self.spinBoxMaxDistExplosion)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalSliderMaxDistExplosion = QtGui.QSlider(self.tab_3)
        self.horizontalSliderMaxDistExplosion.setMaximum(100)
        self.horizontalSliderMaxDistExplosion.setProperty("value", 5)
        self.horizontalSliderMaxDistExplosion.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderMaxDistExplosion.setObjectName(_fromUtf8("horizontalSliderMaxDistExplosion"))
        self.verticalLayout_6.addWidget(self.horizontalSliderMaxDistExplosion)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem10)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.cancelBtn = QtGui.QPushButton(ConfigDialog)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.resetBtn = QtGui.QPushButton(ConfigDialog)
        self.resetBtn.setObjectName(_fromUtf8("resetBtn"))
        self.horizontalLayout_2.addWidget(self.resetBtn)
        self.okBtn = QtGui.QPushButton(ConfigDialog)
        self.okBtn.setDefault(True)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.horizontalLayout_2.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ConfigDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.mineNumberSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinMineNumber.setValue)
        QtCore.QObject.connect(self.spinMineNumber, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.mineNumberSlider.setValue)
        QtCore.QObject.connect(self.radioButtonRandomMines, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBoxRandomMines.setEnabled)
        QtCore.QObject.connect(self.radioButtonFixedMines, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBoxInfoMines.setEnabled)
        QtCore.QObject.connect(self.spinBoxMaxDistExplosion, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSliderMaxDistExplosion.setValue)
        QtCore.QObject.connect(self.horizontalSliderMaxDistExplosion, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxMaxDistExplosion.setValue)
        QtCore.QObject.connect(self.horizontalSliderMinDistDetection, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxMinDistDetection.setValue)
        QtCore.QObject.connect(self.spinBoxMinDistDetection, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSliderMinDistDetection.setValue)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)

    def retranslateUi(self, ConfigDialog):
        ConfigDialog.setWindowTitle(QtGui.QApplication.translate("ConfigDialog", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConfigDialog", "Width (meters):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ConfigDialog", "Height (meters):", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("ConfigDialog", "Mine Field Dimensions", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxRandomMines.setTitle(QtGui.QApplication.translate("ConfigDialog", "Random postions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ConfigDialog", "Number of mines:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxInfoMines.setTitle(QtGui.QApplication.translate("ConfigDialog", "Fixed positions", None, QtGui.QApplication.UnicodeUTF8))
        item = self.TWMinesPos.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("ConfigDialog", "X", None, QtGui.QApplication.UnicodeUTF8))
        item = self.TWMinesPos.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("ConfigDialog", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.addBtn.setText(QtGui.QApplication.translate("ConfigDialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.minusBtn.setText(QtGui.QApplication.translate("ConfigDialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("ConfigDialog", "Mine Field Generation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ConfigDialog", "Minimum distance for detection(cm):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ConfigDialog", "Maximum distance to explosion(cm):", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("ConfigDialog", "Mine Detection", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("ConfigDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setShortcut(QtGui.QApplication.translate("ConfigDialog", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.resetBtn.setText(QtGui.QApplication.translate("ConfigDialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.resetBtn.setShortcut(QtGui.QApplication.translate("ConfigDialog", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.okBtn.setText(QtGui.QApplication.translate("ConfigDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.okBtn.setShortcut(QtGui.QApplication.translate("ConfigDialog", "O, Return", None, QtGui.QApplication.UnicodeUTF8))

