


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(524, 309)

        self.input1 = QtWidgets.QLineEdit(Form)
        self.input1.setGeometry(QtCore.QRect(80, 50, 271, 41))
        self.input1.setObjectName("input1")
        self.input1.setPlaceholderText("0.00")
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(80, 210, 361, 61))
        self.btn.clicked.connect(self.logic)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(80, 140, 271, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setPlaceholderText("0.00")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(360, 50, 81, 41))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(360, 140, 81, 41))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        ### msg box ###########
        self.msg = QtWidgets.QMessageBox(Form)
        self.msg.setWindowTitle("Notification")
        self.msg.setText("Entrez une valeur")
        self.msg.setIcon(self.msg.Warning)
        self.msg.setStandardButtons(self.msg.Cancel|self.msg.Ok)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "Convert"))
        self.comboBox.setItemText(0, _translate("Form", "EURO"))
        self.comboBox.setItemText(1, _translate("Form", "DZD"))
        self.comboBox_2.setItemText(0, _translate("Form", "DZD"))
        self.comboBox_2.setItemText(1, _translate("Form", "EURO"))


    def logic(self):
        if self.input1.text() != "" :
            if self.comboBox.currentText() == "EURO":
                if self.comboBox_2.currentText() == "DZD":
                    result = float(self.input1.text()) * 20
                    print(result)
                    self.textBrowser.setText(str(result))
                else :
                    result = float(self.input1.text())
                    self.textBrowser.setText(str(result))

            elif self.comboBox.currentText() == "DZD":
                    if self.comboBox_2.currentText() == "EURO":
                        result = float(self.input1.text()) / 20
                        print(result)
                        self.textBrowser.setText(str(result))
                    else:
                        result = float(self.input1.text())
                        self.textBrowser.setText(str(result))

        else :
            print ("Entrez une valeur")

            self.msg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
