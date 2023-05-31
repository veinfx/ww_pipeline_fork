import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication

from excel_creater import ExcelCreater
from ui import CreateExcelView


class CreateExcelController(CreateExcelView):
    def __init__(self):
        super().__init__()

        self.model = ExcelCreater()

        # button clicked event
        self.btn_browse.clicked.connect(self.btn_browse_clicked)
        self.btn_create.clicked.connect(self.btn_create_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)

    def btn_browse_clicked(self):
        self.dir_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.line_path.setText(self.dir_path)

    def btn_create_clicked(self):
        self.model
        self.message_box()

    def btn_cancel_clicked(self):
        self.close()


if __name__ == "__main__":
    app = QApplication()
    cc = CreateExcelController()
    sys.exit(app.exec_())