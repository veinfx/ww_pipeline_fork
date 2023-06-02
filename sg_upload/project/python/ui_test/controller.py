import sys
import os
from PySide2.QtWidgets import QApplication, QFileDialog
from view import MyView
from model import xlsx

class Converter_controller(MyView):
    def __init__(self):
        super().__init__()

        self.xx = xlsx()
        self.path = None

        self.openButton.clicked.connect(self.open)
        self.update_project_combo()


        self.uploadButton.clicked.connect(self.upload_data)

    def open(self):
        file_dialog = QFileDialog()
        self.path, _ = file_dialog.getOpenFileName(self, "Select File")
        self.label_path.setText(self.path)
        self.xx.set_file_path(self.path) # 선택한 파일 경로 설정

    def update_project_combo(self):
        self.project.clear()
        self.xx.project_info()

        project_names, sorted_project_names = self.xx.project_info()

        self.project.addItems(sorted_project_names)  # ABC 순서로 정렬된 프로젝트 추가
        self.project.setCurrentIndex(0)  # 첫 번째 프로젝트 선택

    # def update_project_combo(self):
    #     self.project.clear()
    #     self.xx.project_info()
    #
    #     for self.xx.project in self.xx.projects:
    #         self.project.addItem(self.xx.project['name'])

    def upload_data(self):
        project_name = self.project.currentText()
        self.xx.set_file_path(self.path)
        self.xx.data_info()
        self.xx.sequence_upload(project_name)
        self.xx.shot_upload(project_name)

        print("Cinnamoroll")




def main():
    app = QApplication(sys.argv)
    controller = Converter_controller()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()