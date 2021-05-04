from ExportIPWindow import ExportIPWindow
from LoadIPWindow import LoadIPWindow
from MainWindow import MainWindow

if __name__ == '__main__':
    window = LoadIPWindow()
    window.setMainWindow()
    window.root.mainloop()