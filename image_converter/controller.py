from PySide2.QtWidgets import *
from view import ConvertView
from model import ConvertModel


class ConvertController:
    def __init__(self):
        self.view = ConvertView()
        self.model = ConvertModel()

        self.model.set_project()

        for project in self.model.all_project:
            self.view.combo_box.addItem(project)

        self.selected_project = ''

        self.view.combo_box.currentIndexChanged.connect(self.combo_box_changed)
        self.view.ok_button.clicked.connect(self.ok_clicked)
        self.view.cancel_button.clicked.connect(self.cancel_clicked)

    def combo_box_changed(self):
        self.selected_project = self.view.combo_box.currentText()
        self.view.label.setText(f'Converting Project: {self.selected_project}')
        print(f'selected project: {self.selected_project}')

    def ok_clicked(self):
        if self.selected_project:
            self.model.get_project(self.selected_project)
            self.model.get_sequence()
            self.model.get_shot()
            self.model.video_uploader()
            self.view.combo_box.setCurrentIndex(-1)
            self.view.label.setText('Converting Project: ')
            if self.model.is_video_uploaded:
                self.view.message_box('Convert Done')
            else:
                self.view.message_box('Convert Skipped (Video already uploaded)')
        else:
            self.view.combo_box.setCurrentIndex(-1)
            self.view.label.setText('Converting Project: ')
            self.view.message_box('Please select a project')

    def cancel_clicked(self):
        self.view.close()


if __name__ == '__main__':
    app = QApplication()
    controller = ConvertController()
    controller.view.show()
    app.exec_()
