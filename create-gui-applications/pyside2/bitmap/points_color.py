import sys
from random import choice, randint

from PySide2.QtCore import Qt
from PySide2.QtGui import QColor, QPainter, QPen, QPixmap
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    # tag::draw_something[]
    def draw_something(self):
        colors = [
            "#FFD141",
            "#376F9F",
            "#0D1F2D",
            "#E9EBEF",
            "#EB5160",
        ]

        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for n in range(10000):
            # pen = painter.pen() you could get the active pen here
            pen.setColor(QColor(choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(
                200 + randint(-100, 100),
                150 + randint(-100, 100),  # x  # y
            )
        painter.end()

    # end::draw_something[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
