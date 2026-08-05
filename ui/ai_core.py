from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QBrush
)

import math


class AICore(QWidget):

    def __init__(self):

        super().__init__()

        self.setMinimumSize(320, 320)

        self.angle = 0

        self.pulse = 0

        self.direction = 1

        self.timer = QTimer()

        self.timer.timeout.connect(self.animate)

        self.timer.start(16)      # ~60 FPS

    ####################################################

    def animate(self):

        self.angle += 2

        if self.angle >= 360:
            self.angle = 0

        self.pulse += self.direction

        if self.pulse > 20:
            self.direction = -1

        if self.pulse < 0:
            self.direction = 1

        self.update()

    ####################################################

    def draw_ring(self, painter, radius, color, width):

        pen = QPen(color)

        pen.setWidth(width)

        painter.setPen(pen)

        painter.setBrush(Qt.NoBrush)

        painter.drawEllipse(
            -radius,
            -radius,
            radius * 2,
            radius * 2
        )

    ####################################################

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(
            self.width() / 2,
            self.height() / 2
        )

        painter.rotate(self.angle)

        ################################################
        # Outer Ring
        ################################################

        self.draw_ring(
            painter,
            120,
            QColor(0,255,255),
            4
        )

        ################################################
        # Middle Ring
        ################################################

        painter.rotate(-self.angle * 2)

        self.draw_ring(
            painter,
            90,
            QColor(0,170,255),
            3
        )

        ################################################
        # Inner Ring
        ################################################

        painter.rotate(self.angle * 3)

        self.draw_ring(
            painter,
            60,
            QColor(255,255,255),
            2
        )

        ################################################
        # Orbit Dots
        ################################################

        painter.setPen(Qt.NoPen)

        painter.setBrush(QBrush(QColor(0,255,255)))

        for i in range(8):

            a = math.radians(i * 45 + self.angle)

            x = math.cos(a) * 120

            y = math.sin(a) * 120

            painter.drawEllipse(x-5, y-5, 10, 10)

        ################################################
        # Core
        ################################################

        r = 35 + self.pulse

        painter.setBrush(QColor(0,255,255))

        painter.drawEllipse(-r//2,-r//2,r,r)

        ################################################
        # Glow

        painter.setBrush(QColor(0,255,255,70))

        painter.drawEllipse(-55,-55,110,110)
