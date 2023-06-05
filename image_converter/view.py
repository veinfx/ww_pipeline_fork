from PySide2.QtWidgets import *
from PySide2.QtGui import *


class ConvertView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('EXR Converter')

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.combo_box = QComboBox()
        layout.addWidget(self.combo_box)

        self.label = QLabel('Converting Project: ')
        layout.addWidget(self.label)

        button_layout = QHBoxLayout()

        self.ok_button = QPushButton('OK')
        self.ok_button.clicked.connect(self.ok_clicked)
        button_layout.addWidget(self.ok_button)

        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.clicked.connect(self.cancel_clicked)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

        self.setCentralWidget(widget)

        self.center_on_screen()

    def center_on_screen(self):
        screen_geometry = QGuiApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2

        self.move(x, y)

    def ok_clicked(self):
        print('convert start')

    def cancel_clicked(self):
        print('work cancel')
        self.close()

    @staticmethod
    def message_box(message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText(f"{message}")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()


if __name__ == '__main__':
    app = QApplication()
    window = ConvertView()
    window.show()
    app.exec_()
