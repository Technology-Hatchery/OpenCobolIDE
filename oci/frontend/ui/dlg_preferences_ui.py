# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/dev/OpenCobolIDE/forms/dlg_preferences.ui'
#
# Created: Tue Jul  1 10:43:18 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from pyqode.core.qt import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 393)
        icon = QtGui.QIcon.fromTheme("preferences-system")
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QGridLayout(self.widget)
        self.widget_2.setSpacing(0)
        self.widget_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2.setObjectName("widget_2")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabView = QtWidgets.QWidget()
        self.tabView.setObjectName("tabView")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabView)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxViewLineNumber = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxViewLineNumber.setChecked(True)
        self.checkBoxViewLineNumber.setObjectName("checkBoxViewLineNumber")
        self.verticalLayout_2.addWidget(self.checkBoxViewLineNumber)
        self.checkBoxViewMargins = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxViewMargins.setChecked(True)
        self.checkBoxViewMargins.setObjectName("checkBoxViewMargins")
        self.verticalLayout_2.addWidget(self.checkBoxViewMargins)
        self.checkBoxViewMenuBar = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxViewMenuBar.setObjectName("checkBoxViewMenuBar")
        self.verticalLayout_2.addWidget(self.checkBoxViewMenuBar)
        self.checkBoxViewStatus = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxViewStatus.setChecked(True)
        self.checkBoxViewStatus.setObjectName("checkBoxViewStatus")
        self.verticalLayout_2.addWidget(self.checkBoxViewStatus)
        self.checkBoxViewToolBar = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxViewToolBar.setObjectName("checkBoxViewToolBar")
        self.verticalLayout_2.addWidget(self.checkBoxViewToolBar)
        self.checkBoxViewControlPanel = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxViewControlPanel.setObjectName("checkBoxViewControlPanel")
        self.verticalLayout_2.addWidget(self.checkBoxViewControlPanel)
        self.groupBox = QtWidgets.QGroupBox(self.tabView)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.checkBoxHighlightCurrentLine = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxHighlightCurrentLine.setChecked(True)
        self.checkBoxHighlightCurrentLine.setObjectName("checkBoxHighlightCurrentLine")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBoxHighlightCurrentLine)
        self.checkBoxHighlightBraces = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxHighlightBraces.setChecked(True)
        self.checkBoxHighlightBraces.setObjectName("checkBoxHighlightBraces")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBoxHighlightBraces)
        self.checkBoxHighlightWhitespaces = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxHighlightWhitespaces.setChecked(True)
        self.checkBoxHighlightWhitespaces.setObjectName("checkBoxHighlightWhitespaces")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBoxHighlightWhitespaces)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tabView, "")
        self.tabEditor = QtWidgets.QWidget()
        self.tabEditor.setObjectName("tabEditor")
        self.gridLayout = QtWidgets.QGridLayout(self.tabEditor)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabEditor)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBoxEditorTabLen = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxEditorTabLen.setMaximum(99)
        self.spinBoxEditorTabLen.setProperty("value", 4)
        self.spinBoxEditorTabLen.setObjectName("spinBoxEditorTabLen")
        self.horizontalLayout.addWidget(self.spinBoxEditorTabLen)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.checkBoxEditorAutoIndent = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxEditorAutoIndent.setChecked(True)
        self.checkBoxEditorAutoIndent.setObjectName("checkBoxEditorAutoIndent")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBoxEditorAutoIndent)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabEditor)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_4.setObjectName("formLayout_4")
        self.checkBoxEditorSaveOnFocusOut = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxEditorSaveOnFocusOut.setChecked(True)
        self.checkBoxEditorSaveOnFocusOut.setObjectName("checkBoxEditorSaveOnFocusOut")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBoxEditorSaveOnFocusOut)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tabEditor)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_5.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBoxEditorCCTriggerLen = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBoxEditorCCTriggerLen.setProperty("value", 1)
        self.spinBoxEditorCCTriggerLen.setObjectName("spinBoxEditorCCTriggerLen")
        self.horizontalLayout_2.addWidget(self.spinBoxEditorCCTriggerLen)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout_5.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tabEditor, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.radioButtonColorWhite = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButtonColorWhite.setChecked(True)
        self.radioButtonColorWhite.setObjectName("radioButtonColorWhite")
        self.horizontalLayout_3.addWidget(self.radioButtonColorWhite)
        self.radioButtonColorDark = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButtonColorDark.setObjectName("radioButtonColorDark")
        self.horizontalLayout_3.addWidget(self.radioButtonColorDark)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fontComboBox = QtWidgets.QFontComboBox(self.groupBox_6)
        self.fontComboBox.setFontFilters(QtWidgets.QFontComboBox.MonospacedFonts)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.fontComboBox.setCurrentFont(font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_4.addWidget(self.fontComboBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.spinBoxFontSize = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBoxFontSize.setProperty("value", 10)
        self.spinBoxFontSize.setObjectName("spinBoxFontSize")
        self.horizontalLayout_5.addWidget(self.spinBoxFontSize)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidgetColorSchemes = QtWidgets.QListWidget(self.groupBox_7)
        self.listWidgetColorSchemes.setObjectName("listWidgetColorSchemes")
        self.gridLayout_4.addWidget(self.listWidgetColorSchemes, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_7)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout_6 = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout_6.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName("formLayout_6")
        self.checkBoxRunExtTerm = QtWidgets.QCheckBox(self.tab_2)
        self.checkBoxRunExtTerm.setObjectName("checkBoxRunExtTerm")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBoxRunExtTerm)
        self.lineEditRunTerm = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditRunTerm.setObjectName("lineEditRunTerm")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditRunTerm)
        self.checkBoxCompileBeforeRun = QtWidgets.QCheckBox(self.tab_2)
        self.checkBoxCompileBeforeRun.setChecked(True)
        self.checkBoxCompileBeforeRun.setObjectName("checkBoxCompileBeforeRun")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBoxCompileBeforeRun)
        self.checkBoxAutoDetectDeps = QtWidgets.QCheckBox(self.tab_2)
        self.checkBoxAutoDetectDeps.setChecked(True)
        self.checkBoxAutoDetectDeps.setObjectName("checkBoxAutoDetectDeps")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkBoxAutoDetectDeps)
        self.checkBoxCustomPath = QtWidgets.QCheckBox(self.tab_2)
        self.checkBoxCustomPath.setObjectName("checkBoxCustomPath")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.checkBoxCustomPath)
        self.lineEditCompilerPath = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditCompilerPath.setObjectName("lineEditCompilerPath")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditCompilerPath)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_Cobol = QtWidgets.QWidget()
        self.tab_Cobol.setObjectName("tab_Cobol")
        self.formLayout_7 = QtWidgets.QFormLayout(self.tab_Cobol)
        self.formLayout_7.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_7.setObjectName("formLayout_7")
        self.checkBoxFreeFormat = QtWidgets.QCheckBox(self.tab_Cobol)
        self.checkBoxFreeFormat.setObjectName("checkBoxFreeFormat")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBoxFreeFormat)
        self.label_5 = QtWidgets.QLabel(self.tab_Cobol)
        self.label_5.setObjectName("label_5")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.spinBoxLeftMargin = QtWidgets.QSpinBox(self.tab_Cobol)
        self.spinBoxLeftMargin.setMaximum(256)
        self.spinBoxLeftMargin.setObjectName("spinBoxLeftMargin")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxLeftMargin)
        self.label_6 = QtWidgets.QLabel(self.tab_Cobol)
        self.label_6.setObjectName("label_6")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinBoxRightMargin = QtWidgets.QSpinBox(self.tab_Cobol)
        self.spinBoxRightMargin.setMaximum(256)
        self.spinBoxRightMargin.setObjectName("spinBoxRightMargin")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBoxRightMargin)
        self.label_7 = QtWidgets.QLabel(self.tab_Cobol)
        self.label_7.setObjectName("label_7")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEditCommentIndicator = QtWidgets.QLineEdit(self.tab_Cobol)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.lineEditCommentIndicator.setFont(font)
        self.lineEditCommentIndicator.setObjectName("lineEditCommentIndicator")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditCommentIndicator)
        self.label_8 = QtWidgets.QLabel(self.tab_Cobol)
        self.label_8.setObjectName("label_8")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBoxStandard = QtWidgets.QComboBox(self.tab_Cobol)
        self.comboBoxStandard.setObjectName("comboBoxStandard")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxStandard)
        self.tabWidget.addTab(self.tab_Cobol, "")
        self.widget_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(4)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Preferences"))
        self.widget.setAccessibleName(_translate("Dialog", "widget", "widget"))
        self.checkBoxViewLineNumber.setText(_translate("Dialog", "Display line numbers"))
        self.checkBoxViewMargins.setText(_translate("Dialog", "Display margins"))
        self.checkBoxViewMenuBar.setText(_translate("Dialog", "Display Menu bar"))
        self.checkBoxViewStatus.setText(_translate("Dialog", "Display Status bar"))
        self.checkBoxViewToolBar.setText(_translate("Dialog", "Display Tool bar "))
        self.checkBoxViewControlPanel.setText(_translate("Dialog", "Display control panel (compile and run button inside editor)"))
        self.groupBox.setTitle(_translate("Dialog", "Highlighting"))
        self.checkBoxHighlightCurrentLine.setText(_translate("Dialog", "Highlight current line"))
        self.checkBoxHighlightBraces.setText(_translate("Dialog", "Highlight matching braces"))
        self.checkBoxHighlightWhitespaces.setText(_translate("Dialog", "Highlight whitespaces"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabView), _translate("Dialog", "View"))
        self.groupBox_2.setTitle(_translate("Dialog", "Indentation"))
        self.label.setText(_translate("Dialog", "Tab width (number of spaces):"))
        self.checkBoxEditorAutoIndent.setText(_translate("Dialog", "Enable automatic indentation"))
        self.groupBox_3.setTitle(_translate("Dialog", "File saving"))
        self.checkBoxEditorSaveOnFocusOut.setText(_translate("Dialog", "Save on editor focus out"))
        self.groupBox_4.setTitle(_translate("Dialog", "Code completion"))
        self.label_2.setText(_translate("Dialog", "Trigger length:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEditor), _translate("Dialog", "Editor"))
        self.groupBox_5.setTitle(_translate("Dialog", "Global style"))
        self.radioButtonColorWhite.setText(_translate("Dialog", "White"))
        self.radioButtonColorDark.setText(_translate("Dialog", "Dark"))
        self.groupBox_6.setTitle(_translate("Dialog", "Font"))
        self.label_3.setText(_translate("Dialog", "Editor font"))
        self.label_4.setText(_translate("Dialog", "Font size:"))
        self.groupBox_7.setTitle(_translate("Dialog", "Color scheme"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Font && Colors"))
        self.checkBoxRunExtTerm.setText(_translate("Dialog", "Run in external terminal"))
        self.checkBoxCompileBeforeRun.setText(_translate("Dialog", "Recompile before run"))
        self.checkBoxAutoDetectDeps.setText(_translate("Dialog", "Autodetect dependencies"))
        self.checkBoxCustomPath.setText(_translate("Dialog", "Custom compiler path"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Build && Run"))
        self.checkBoxFreeFormat.setToolTip(_translate("Dialog", "Code and compile with free format support"))
        self.checkBoxFreeFormat.setText(_translate("Dialog", "Free Format support"))
        self.label_5.setText(_translate("Dialog", "Left margin position:"))
        self.spinBoxLeftMargin.setToolTip(_translate("Dialog", "Position of the left margin (starting from 0)"))
        self.label_6.setText(_translate("Dialog", "Right margin position"))
        self.spinBoxRightMargin.setToolTip(_translate("Dialog", "Position of the right margin (starting from 0)"))
        self.label_7.setText(_translate("Dialog", "Comment indicator:"))
        self.lineEditCommentIndicator.setText(_translate("Dialog", "*>"))
        self.label_8.setText(_translate("Dialog", "Standard"))
        self.comboBoxStandard.setItemText(0, _translate("Dialog", "default"))
        self.comboBoxStandard.setItemText(1, _translate("Dialog", "cobol2002"))
        self.comboBoxStandard.setItemText(2, _translate("Dialog", "cobol85"))
        self.comboBoxStandard.setItemText(3, _translate("Dialog", "ibm"))
        self.comboBoxStandard.setItemText(4, _translate("Dialog", "mvs"))
        self.comboBoxStandard.setItemText(5, _translate("Dialog", "bs2000"))
        self.comboBoxStandard.setItemText(6, _translate("Dialog", "mf"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Cobol), _translate("Dialog", "Cobol"))

from . import ide_rc
