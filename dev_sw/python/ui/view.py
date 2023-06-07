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
        # self.resize(300, 250)

        # set layout
        layout = QVBoxLayout()
        project_label = QLabel('Projects')
        layout.addWidget(project_label)
        self.project_combo_view = QComboBox()
        layout.addWidget(self.project_combo_view)

        # seq_label = QLabel('seq')
        # layout.addWidget(seq_label)
        # self.seq_combo_view = QComboBox()
        # layout.addWidget(self.seq_combo_view)

        shot_label = QLabel('shots')
        layout.addWidget(shot_label)
        self.shot_view = QTreeView()

        layout.addWidget(self.shot_view)

        copy_path_label = QLabel('scan-org copy path')
        layout.addWidget(copy_path_label)
        self.copy_path_view = QLineEdit()
        layout.addWidget(self.copy_path_view)

        btn_layout = QHBoxLayout()
        self.copy_btn = QPushButton('scan-org Copy')
        btn_layout.addWidget(self.copy_btn)
        self.copy_btn.clicked.connect(self.pressed_copy)

        self.convert_btn = QPushButton('Convert')
        btn_layout.addWidget( self.convert_btn)
        self.convert_btn.clicked.connect(self.pressed_convert)

        self.close_btn = QPushButton('close')
        btn_layout.addWidget(self.close_btn)
        self.close_btn.clicked.connect(self.pressed_close)

        layout.addLayout(btn_layout)


        # seq_combo_view = QComboBox()
        # shot_combo_view = QComboBox()
        # self.dir_path_view = QLineEdit(self)
        # qvbox_layout = QVBoxLayout()
        # layout.addLayout(qvbox_layout)
        # qvbox_layout.addWidget(project_label)
        # qvbox_layout.addWidget(project_combo_view)

        # seq_label = QLabel('SG seq')
        # qhbox_layout = QHBoxLayout()
        # layout.addLayout(qhbox_layout)
        # qhbox_layout.addWidget(seq_label)
        # qhbox_layout.addWidget(seq_combo_view)
        # shot_label = QLabel('SG shot')
        # qhbox_layout.addWidget(shot_label)
        # qhbox_layout.addWidget(shot_combo_view)

        self.setLayout(layout)

    def pressed_copy(self):
        print("project scan-org copy")

    def pressed_convert(self):
        print("org - jpg and mp4 covert")

    def pressed_close(self):
        print("ui close")

    def success_messagebox(self):
        """excel create 버튼 성공시 QMessageBox 를 사용하여 확인창을 보여주는 함수이다.
        """
        QMessageBox.information(self, "QMessageBox", "Success")


def main():
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    view = MyView()
    view.show()
    app.exec_()


if __name__ == "__main__":
    main()
