import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from untitled4 import *
from CodeLibrary import Simulation

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

        self.ui.comboBox_2.currentIndexChanged.connect(self.show_txt)   # 联系按钮和槽

    def show_txt(self):  # 槽响应函数
        method = self.ui.comboBox_2.currentText()  # 定义combobox中的选中内容
        # self.ui.label_20.setText(method)    # 将combobox的内容显示到label_20中
        sim.GLB_Set_Method(method)    # 同步combobox的选中内容到aspen中

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
    sim = Simulation(AspenFileName="耦合工艺20230413.apw",
                     WorkingDirectoryPath=r"F:\AspenTest\耦合工艺20230413",
                     VISIBILITY=True)      # 初始化aspen文件
    app = QApplication(sys.argv)
    game = TestWidget()
    game.show()
    sys.exit(app.exec_())
