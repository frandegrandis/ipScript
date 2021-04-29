from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView,QApplication


class IPTable(QWidget):
    def __init__(self, data):
        super().__init__()
        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.data = data
        self.headers = ['IP', 'Location', 'TorNode']
        self.creatingTables()

        self.setLayout(self.layout)

    def creatingTables(self):
        data = self.data
        table = self.table
        self.setupTable(table)
        self.fillTableWith()

    def fillTableWith(self):
        data = self.data
        table = self.table
        for row in range(len(data)):
            ip_info = data[row]  # ip_info is a list containing [ip,location,TorNode]
            for column in range(len(data[row])):
                table.setItem(row, column, QTableWidgetItem(str(ip_info[column])))
        self.repaint()

    def setupTable(self, table):  # make configurations on the table.
        table.setRowCount(len(self.data))
        table.setColumnCount(len(self.headers))
        table.setHorizontalHeaderLabels(self.headers)
        header = table.horizontalHeader()
        table.setSortingEnabled(True)
        for i in range(len(self.headers)):
            header.setSectionResizeMode(i, QHeaderView.Stretch)