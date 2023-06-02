import sys

from PySide2.QtWidgets import *
from PySide2 import QtGui


class CreateExcelView(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Create Excel File")
        self.resize(400, 100)
        self.center()

        # create widgets
        vb = QVBoxLayout()

        hbtop = QHBoxLayout()
        vb.addLayout(hbtop)
        self.line_dir_path = QLineEdit()
        self.btn_browse = QPushButton("Browse")
        self.btn_clear = QPushButton("Clear")
        self.btn_clear.setMaximumSize(60, 23)
        hbtop.addWidget(self.line_dir_path)
        hbtop.addWidget(self.btn_browse)
        hbtop.addWidget(self.btn_clear)

        hbmid = QHBoxLayout()
        vb.addLayout(hbmid)
        self.label_save_path = QLabel("Save Directory")
        hbmid.addWidget(self.label_save_path)

        hbbot = QHBoxLayout()
        vb.addLayout(hbbot)
        self.btn_create = QPushButton("Create")
        self.btn_create.setMaximumSize(200, 30)
        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.setMaximumSize(200, 30)
        hbbot.addWidget(self.btn_create)
        hbbot.addWidget(self.btn_cancel)

        self.setLayout(vb)

        # print(self.btn_create.sizeHint())
        # print(self.btn_create.sizePolicy())

        # button clicked event example
        self.btn_browse.clicked.connect(self.browse_test)
        self.btn_clear.clicked.connect(self.clear_test)
        self.btn_create.clicked.connect(self.create_test)
        self.btn_cancel.clicked.connect(self.cancel_test)

        self.show()

    def center(self):
        fg = self.frameGeometry()
        dw = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        fg.moveCenter(dw)
        self.move(fg.topLeft())

    def message_box(self):
        msgbox = QMessageBox(self)
        msgbox.about(self, "Successful", "Save Complete!")

    def browse_test(self):
        print("Select a directory")

    def clear_test(self):
        print("Clear the directory")

    def create_test(self):
        # self.message_box()
        print("Save Excel File")

    def cancel_test(self):
        print("Close widget")


if __name__ == '__main__':
    app = QApplication()
    cv = CreateExcelView()
    sys.exit(app.exec_())
