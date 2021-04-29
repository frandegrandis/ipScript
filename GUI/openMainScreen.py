import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

import mainScreen


class IpAnalyzeApp(QtWidgets.QMainWindow, mainScreen.UiMainWindow):
    def __init__(self, parent=None):
        super(IpAnalyzeApp, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form = mainScreen.UiMainWindow()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
