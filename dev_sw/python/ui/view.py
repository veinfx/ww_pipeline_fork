import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class MyView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SG CO CO')
        self.move(550, 300)
        self.resize(300, 250)
        # view instance
        project_combo_view = QComboBox()
        seq_combo_view = QComboBox()
        shot_combo_view = QComboBox()

        # self.dir_path_view = QLineEdit(self)

        # set layout
        layout = QVBoxLayout()
        project_label = QLabel('SG Projects')
        qvbox_layout = QVBoxLayout()
        layout.addLayout(qvbox_layout)
        qvbox_layout.addWidget(project_label)
        qvbox_layout.addWidget(project_combo_view)

        seq_label = QLabel('SG seq')
        qhbox_layout = QHBoxLayout()
        layout.addLayout(qhbox_layout)
        qhbox_layout.addWidget(seq_label)
        qhbox_layout.addWidget(seq_combo_view)
        shot_label = QLabel('SG shot')
        qhbox_layout.addWidget(shot_label)
        qhbox_layout.addWidget(shot_combo_view)
        self.setLayout(layout)



        def pressed_save_as(self):
            print("save excel path seleted")

        def pressed_excel_create(self):
            print("excel created")

        def pressed_close(self):
            print("window close")

        def excel_create_btn_messagebox(self):
            """excel create 버튼 성공시 QMessageBox 를 사용하여 확인창을 보여주는 함수이다.
            """
            QMessageBox.information(self, "QMessageBox", "Excel Creat Success")


def main():
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    view = MyView()
    view.show()
    app.exec_()


if __name__ == "__main__":
    main()
