import sys
from qtpy import QtWidgets

from Programm.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(str('Wichtige Levels & Fibonacci'))

        self.ui.berechnen.clicked.connect(self.rechner)

    def rechner(self):
        o = self.ui.open.value()
        l = self.ui.low.value()
        h = self.ui.high.value()
        c = self.ui.close.value()

        # Fibonacci Rechner

        d = h - l

        gf0 = round(d * 0 + l, 2)
        gf23 = round(d * 0.236 + l, 2)
        gf38 = round(d * 0.382 + l, 2)
        gf50 = round(d * 0.50 + l, 2)
        gf61 = round(d * 0.618 + l, 2)
        gf100 = round(d * 1 + l, 2)
        gf138 = round(d * 1.382 + l, 2)
        gf161 = round(d * 1.618 + l, 2)
        gf200 = round(d * 2 + l, 2)
        gf261 = round(d * 2.618 + l, 2)

        self.ui.gf0.setText(str(gf0))
        self.ui.gf23.setText(str(gf23))
        self.ui.gf38.setText(str(gf38))
        self.ui.gf50.setText(str(gf50))
        self.ui.gf61.setText(str(gf61))
        self.ui.gf100.setText(str(gf100))
        self.ui.gf138.setText(str(gf138))
        self.ui.gf161.setText(str(gf161))
        self.ui.gf200.setText(str(gf200))
        self.ui.gf261.setText(str(gf261))

        # Wiederstand & Unterstützung

        kp = (h + l + c) / 3

        # Widerstand

        kr1 = ((2 * kp) - l)
        kr2 = kp + h - l
        kr3 = h + 2 * (kp - l)

        # Unterstützung

        ks1 = (2 * kp) - h
        ks2 = kp - h + l
        ks3 = l - 2 * (h - kp)

        # Woody Methode
        # Pivot Point

        wp = (h + l + 2 * c) / 4

        # Widerstand

        wr1 = 2 * wp - l
        wr2 = wp + h - l

        # Unterstützung

        ws1 = 2 * wp - h
        ws2 = wp - h + l

        # Camarilla Methode
        # Unterstützung

        cr1 = (h - l) * 1.1 / 12 + c
        cr2 = (h - l) * 1.1 / 6 + c
        cr3 = (h - l) * 1.1 / 4 + c
        cr4 = (h - l) * 1.1 / 2 + c

        # Widerstand

        cs1 = c - (h - l) * 1.1 / 12
        cs2 = c - (h - l) * 1.1 / 6
        cs3 = c - (h - l) * 1.1 / 4
        cs4 = c - (h - l) * 1.1 / 2

        # DeMark Methode

        if c < o:
            x = h + 2 * l + c
        elif c > o:
            x = 2 * h + l + c
        elif c == o:
            x = h + l + 2 * c

        nh = x / 2 - l
        nl = x / 2 - h

        # Durchschnittliche Werte

        p = round((kp + wp) / 2, 2)

        r1 = round((kr1 + wr1 + cr1) / 3, 2)
        r2 = round((kr2 + wr2 + cr2) / 3, 2)
        r3 = round((kr3 + cr3) / 2, 2)
        r4 = cr4

        s1 = round((ks1 + ws1 + cs1) / 3, 2)
        s2 = round((ks2 + ws2 + cs2) / 3, 2)
        s3 = round((ks3 + cs3) / 2,2)
        s4 = cs4

        self.ui.pivot_result.setText(str(p))
        self.ui.new_high.setText(str(nh))
        self.ui.new_low.setText(str(nl))
        self.ui.r1.setText(str(r1))
        self.ui.r2.setText(str(r2))
        self.ui.r3.setText(str(r3))
        self.ui.r4.setText(str(r4))
        self.ui.s1.setText(str(s1))
        self.ui.s2.setText(str(s2))
        self.ui.s3.setText(str(s3))
        self.ui.s4.setText(str(s4))

window = MainWindow()

window.show()

sys.exit(app.exec_())
