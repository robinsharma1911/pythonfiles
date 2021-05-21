import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,QMessageBox,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont,QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        #self.setToolTip('my <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QIcon('pic.png'))
        self.show()
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.Cancel)

        if reply == QMessageBox.Yes:

            event.accept()
        else:

            event.ignore()


        

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()