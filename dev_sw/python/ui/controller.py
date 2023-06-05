#!/usr/bin/env python
# :coding: utf-8

import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *

from model import MyModel
from view import MyView
from sg_mapping import SgMapping


class MyController:

    def __init__(self):
        # set real path
        # now_path = os.path.dirname(os.path.realpath(__file__))
        # self.file_path = now_path[:-2] + "/blend_dummy_files"
        # set real path
        # now_path = os.path.dirname(os.path.realpath(__file__))
        # self.file_path = now_path[:-6] + 'excel'

        # instance
        self.sg = SgMapping()
        self.model = MyModel()
        self.view = MyView()

        self._project_combo_model = MyModel()
        self._project_combo_view = self.view.project_combo_view

        self._project_combo_view.setModel(self._project_combo_model)

        self.set_project_combobox()

        self.view.copy_btn.clicked.connect(self.set_org_copy)
        self.view.convert_btn.clicked.connect(self.set_convert)
        self.view.close_btn.clicked.connect(self.ui_close)

        # self._dir_path_model = model
        # self._dir_path_view = view.excel_path_view
        # set model
        # completer = QCompleter(self._dir_path_model)
        # self._dir_path_view.setCompleter(completer)

        # self.view.convert_btn.clicked.connect(self.set_excel_save)

    def set_project_combobox(self):
        """
        sg_mp(mapping api)를 통하여 project들을 combobox 에 넣어주는 함수이다.
        """
        projects = self.sg.get_active_project()
        for project in projects:
            self._project_combo_model._data_list.append(project)

    def set_org_copy(self):
        self.model.org_copy()
        self.view.success_messagebox()
        pass

    def set_convert(self):
        self.view.success_messagebox()
        pass

    def ui_close(self):
        """
        close 버튼 클릭시 ui 창이 닫힌다.
        """
        self.view.close()


def main():
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    controller = MyController()
    controller.view.show()
    app.exec_()


if __name__ == "__main__":
    main()
