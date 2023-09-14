import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from untitled4 import *

# 输入界面优化



class TestWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow_inter()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_write.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))  # 绑定槽
        self.ui.pushButton_result.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

    def show_txt(self):
        self.label_20.setText("method选择是{}".format(self.comboBox_2.currentText()))

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TestWidget()
    game.show()
    game.show_txt()
    sys.exit(app.exec_())
