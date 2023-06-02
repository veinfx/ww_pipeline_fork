import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLabel

class MyView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Sanrio_OUT')

        # first_hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        #label
        self.label_path = QLabel()
        vbox.addWidget(self.label_path)
        self.label_path.setText('경로에요')

        #"Open" Button
        self.openButton = QPushButton("Open")
        self.openButton.setMaximumWidth(60)  # 버튼 크기 조정
        vbox.addWidget(self.openButton)

        #Project Combo box
        # second_hbox = QHBoxLayout()
        self.project = QComboBox()
        vbox.addWidget(self.project)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()
        vbox.addLayout(button_layout)

        # "Cancel" 버튼
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)  # 창 닫기
        button_layout.addWidget(cancel_button)

        # "Upload" Button
        self.uploadButton = QPushButton("Upload")
        button_layout.addWidget(self.uploadButton)

        self.setLayout(vbox)
        self.show()

    def update_project_combo(self):
        project_names, sorted_project_names = self.xx.project_info()

        self.project.clear()  # 기존 항목 제거

        self.project.addItems(sorted_project_names)  # ABC 순서로 정렬된 프로젝트 추가
        self.project.setCurrentIndex(0)  # 첫 번째 프로젝트 선택


def main():
    app = QApplication(sys.argv)
    view = MyView()
    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()