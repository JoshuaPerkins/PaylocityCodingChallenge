# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QIcon
import pcc_main
import sys


# GUI Main class
class Ui_main_window_pcc(object):
    # GUI window works off of generic employee and benefits objects to start
    def __init__(self, employee, benefits):
        self.employee = employee
        self.benefits = benefits

    # Sets Gui window layout
    def setupUi(self, main_window_pcc):
        main_window_pcc.setObjectName("main_window_pcc")
        main_window_pcc.resize(640, 380)
        main_window_pcc.setAnimated(True)
        self.central_widget_pcc = QtWidgets.QWidget(main_window_pcc)
        self.central_widget_pcc.setObjectName("central_widget_pcc")
        self.group_employee = QtWidgets.QGroupBox(self.central_widget_pcc)
        self.group_employee.setGeometry(QtCore.QRect(10, 10, 621, 181))
        self.group_employee.setObjectName("group_employee")
        self.text_employee_name = QtWidgets.QPlainTextEdit(self.group_employee)
        self.text_employee_name.setGeometry(QtCore.QRect(10, 40, 140, 25))
        self.text_employee_name.setObjectName("text_employee_name")
        self.label_employee_name = QtWidgets.QLabel(self.group_employee)
        self.label_employee_name.setGeometry(QtCore.QRect(10, 20, 120, 20))
        self.label_employee_name.setObjectName("label_employee_name")
        self.label_employee_dependents = QtWidgets.QLabel(self.group_employee)
        self.label_employee_dependents.setGeometry(QtCore.QRect(310, 20, 141, 20))
        self.label_employee_dependents.setObjectName("label_employee_dependents")
        self.button_employee_calculate = QtWidgets.QPushButton(self.group_employee)
        self.button_employee_calculate.setGeometry(QtCore.QRect(470, 110, 141, 25))
        self.button_employee_calculate.setObjectName("button_employee_calculate")
        self.button_employee_clear = QtWidgets.QPushButton(self.group_employee)
        self.button_employee_clear.setGeometry(QtCore.QRect(470, 60, 141, 25))
        self.button_employee_clear.setObjectName("button_employee_clear")
        self.listwidget_dependents = QtWidgets.QListWidget(self.group_employee)
        self.listwidget_dependents.setGeometry(QtCore.QRect(310, 40, 140, 101))
        self.listwidget_dependents.setObjectName("listwidget_dependents")
        self.text_employee_dependent_add = QtWidgets.QPlainTextEdit(self.group_employee)
        self.text_employee_dependent_add.setGeometry(QtCore.QRect(160, 40, 140, 25))
        self.text_employee_dependent_add.setObjectName("text_employee_dependent_add")
        self.label_employee_dependent_add = QtWidgets.QLabel(self.group_employee)
        self.label_employee_dependent_add.setGeometry(QtCore.QRect(160, 20, 141, 20))
        self.label_employee_dependent_add.setObjectName("label_employee_dependent_add")
        self.button_employee_dependent_add = QtWidgets.QPushButton(self.group_employee)
        self.button_employee_dependent_add.setGeometry(QtCore.QRect(160, 70, 141, 25))
        self.button_employee_dependent_add.setObjectName("button_employee_dependent_add")
        self.button_employee_dependent_delete = QtWidgets.QPushButton(self.group_employee)
        self.button_employee_dependent_delete.setGeometry(QtCore.QRect(310, 150, 141, 25))
        self.button_employee_dependent_delete.setObjectName("button_employee_dependent_delete")
        self.group_preview = QtWidgets.QGroupBox(self.central_widget_pcc)
        self.group_preview.setGeometry(QtCore.QRect(10, 190, 621, 150))
        self.group_preview.setObjectName("group_preview")
        self.table_preview = QtWidgets.QTableWidget(self.group_preview)
        self.table_preview.setGeometry(QtCore.QRect(5, 21, 611, 120))
        self.table_preview.setAlternatingRowColors(True)
        self.table_preview.setColumnCount(6)
        self.table_preview.setObjectName("table_preview")
        self.table_preview.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.table_preview.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_preview.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_preview.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_preview.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_preview.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_preview.setHorizontalHeaderItem(5, item)
        self.table_preview.horizontalHeader().setDefaultSectionSize(99)
        self.table_preview.verticalHeader().setVisible(True)
        main_window_pcc.setCentralWidget(self.central_widget_pcc)
        self.menubar = QtWidgets.QMenuBar(main_window_pcc)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        main_window_pcc.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window_pcc)
        self.statusbar.setObjectName("statusbar")
        main_window_pcc.setStatusBar(self.statusbar)

        self.button_employee_calculate.clicked.connect(self.button_employee_calculate_click)
        self.button_employee_clear.clicked.connect(self.button_employee_clear_click)
        self.button_employee_dependent_add.clicked.connect(self.button_employee_dependent_add_click)
        self.button_employee_dependent_delete.clicked.connect(self.button_employee_dependent_delete_click)

        self.retranslateUi(main_window_pcc)
        QtCore.QMetaObject.connectSlotsByName(main_window_pcc)

    # Sets other gui elements and labels
    def retranslateUi(self, main_window_pcc):
        _translate = QtCore.QCoreApplication.translate
        main_window_pcc.setWindowTitle(_translate("main_window_pcc", "Paylocity Coding Challenge"))
        self.group_employee.setTitle(_translate("main_window_pcc", "Employee Data"))
        self.label_employee_name.setText(_translate("main_window_pcc", "Name (Ex. \'Bob\'):"))
        self.label_employee_dependents.setText(_translate("main_window_pcc", "Dependents List:"))
        self.button_employee_calculate.setText(_translate("main_window_pcc", "Calculate Cost Preview"))
        self.button_employee_clear.setText(_translate("main_window_pcc", "Clear All Data"))
        self.label_employee_dependent_add.setText(_translate("main_window_pcc", "Dependent (Ex. \'Jane\')"))
        self.button_employee_dependent_add.setText(_translate("main_window_pcc", "Add Dependent To List"))
        self.button_employee_dependent_delete.setText(_translate("main_window_pcc", "Delete Dependent From List"))
        self.group_preview.setTitle(_translate("main_window_pcc", "Cost Preview"))
        item = self.table_preview.horizontalHeaderItem(0)
        item.setText(_translate("main_window_pcc", "Name"))
        item = self.table_preview.horizontalHeaderItem(1)
        item.setText(_translate("main_window_pcc", "# Dependents"))
        item = self.table_preview.horizontalHeaderItem(2)
        item.setText(_translate("main_window_pcc", "Type"))
        item = self.table_preview.horizontalHeaderItem(3)
        item.setText(_translate("main_window_pcc", "Gross Pay $"))
        item = self.table_preview.horizontalHeaderItem(4)
        item.setText(_translate("main_window_pcc", "Deduction $"))
        item = self.table_preview.horizontalHeaderItem(5)
        item.setText(_translate("main_window_pcc", "Net Pay $"))

    # Formats cost preview for table
    def cost_view_format(self, employee, type, report):
        formatted = [employee.employee_name,
                     len(employee.dependents),
                     type, report[0],
                     report[1],
                     report[2]]
        return formatted

    # Updates cost preview table with calculated data
    def update_cost_preview(self, employee, report_year, report_month, report_paycheck):
        cost_view = [self.cost_view_format(employee, 'Yearly', report_year),
                     self.cost_view_format(employee, 'Monthly', report_month),
                     self.cost_view_format(employee, 'Paycheck', report_paycheck)]

        row_index = 0
        for report in cost_view:
            col_index = 0
            for item in report:
                if col_index > 2:
                    item_str = '{:.2f}'.format(item)
                    data = QTableWidgetItem(item_str)
                    data.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                else:
                    item_str = str(item)
                    data = QTableWidgetItem(item_str)
                    data.setTextAlignment(QtCore.Qt.AlignVCenter)
                self.table_preview.setItem(row_index, col_index, data)
                col_index += 1
            row_index += 1

    # Process all input data for employee benefits report
    def button_employee_calculate_click(self):
        try:
            name = self.text_employee_name.toPlainText().split()[0]
            if name.isalpha():
                self.employee.set_employee(name)
                report_year = pcc_main.report_benefit_costs(self.employee, self.benefits)
                report_month = pcc_main.report_conv_month(report_year)
                report_paycheck = pcc_main.report_conv_paycheck(report_year, self.employee)
                self.update_cost_preview(self.employee, report_year, report_month, report_paycheck)
        except:
            self.show_popup('Error: Calculate Data', 'Make sure the employee name and all dependents are correctly entered.')

    # Clears all data from gui
    def button_employee_clear_click(self):
        try:
            self.employee.reset_employee()
            self.employee.clr_dependents()
            self.text_employee_name.setPlainText('')
            self.text_employee_dependent_add.setPlainText('')
            self.listwidget_dependents.clear()
            self.table_preview.clearContents()
        except:
            self.show_popup('Error: Clear All', 'Critical Error - Please restart the program.')

    # Adds dependent to employee
    def button_employee_dependent_add_click(self):
        try:
            dependent = self.text_employee_dependent_add.toPlainText().split()[0]
            if dependent.isalpha():
                self.employee.add_dependent(dependent)
                self.listwidget_dependents.addItem(dependent)
                self.text_employee_dependent_add.clear()
        except:
            self.show_popup('Error: Add Dependent', 'Make sure the name is entered correctly to add a dependent.')

    # Deletes dependent from employee
    def button_employee_dependent_delete_click(self):
        try:
            selected_row = self.listwidget_dependents.currentRow()
            dependent_obj = self.listwidget_dependents.takeItem(selected_row)
            self.employee.del_dependent(dependent_obj.text())
            del dependent_obj
        except:
            self.show_popup('Error: Delete Dependent', 'Make sure a dependent is selected from the list.')

    # Generic popup used to display error messages or warnings
    def show_popup(self, title='Error', message='Error with program; please ensure all data is entered.'):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        popup = msg.exec_()

# Main program to run gui for employee benefits reporting
if __name__ == "__main__":
    my_employee = pcc_main.Employee()
    my_benefits = pcc_main.Benefits()

    app = QtWidgets.QApplication(sys.argv)
    main_window_pcc = QtWidgets.QMainWindow()
    ui = Ui_main_window_pcc(employee=my_employee, benefits=my_benefits)
    ui.setupUi(main_window_pcc)
    main_window_pcc.show()
    sys.exit(app.exec_())
