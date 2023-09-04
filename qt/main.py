import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtGui import QColor, QPainter

from logic import *

X, Y = 1280, 720


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.black = QColor(0, 0, 0)
        self.gray = QColor(128, 128, 128)
        self.setStyleSheet("background-color: gray;")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.blocks = get_block_locations(space_ship(), X // 2, Y // 2)
        self.old_blocks = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cycle)
        self.timer_interval = 100 

        self.timer.start(self.timer_interval)  # Start the timer immediately

    def paintEvent(self, event):
        self.painter = QPainter(self)
        self.painter.setPen(self.gray)
        self.painter.setBrush(self.gray)
        for block in self.old_blocks:
            self.painter.drawRect(block[0], block[1], 20, 20)
        self.painter.setPen(self.black)
        self.painter.setBrush(self.black)
        for block in self.blocks:
            self.painter.drawRect(block[0], block[1], 20, 20)
        self.painter.end()

    def cycle(self):
        self.old_blocks = self.blocks
        possible_blocks = get_possible(self.blocks)
        self.blocks = check_dead(possible_blocks, self.blocks) + check_alive(
            self.blocks, self.blocks
        )
        self.blocks = center_blocks(self.blocks, Y, X)
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()

    widget.resize(X, Y)
    widget.show()

    sys.exit(app.exec())
