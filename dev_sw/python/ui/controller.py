#!/usr/bin/env python
# :coding: utf-8

import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

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

        # self._seq_combo_model = MyModel()
        # self._seq_combo_view = self.view.seq_combo_view
        # self._seq_combo_view.setModel(self._seq_combo_model)

        self._shot_model = MyModel()
        # self._shot_model.setHorizontalHeaderItem(['Name', 'Height', 'Weight'])

        self._shot_view = self.view.shot_view
        self._shot_view.setModel(self._shot_model)
        # self.importData(data)
        # self._shot_view.expandAll()

        # self._org_path_model = MyModel()
        # self._org_path_view = self.view.copy_path_view
        # completer = QCompleter(self._org_path_model)
        # self._org_path_view.setCompleter(completer)

        self.set_project_combobox()
        # self.set_seq_combobox()

        self._project_combo_view.currentIndexChanged.connect(self.selected_project)
        self._shot_view.clicked.connect(self.sel_shot_get_copy_path)

        self.view.copy_btn.clicked.connect(self.set_org_copy)
        self.view.convert_btn.clicked.connect(self.set_convert)
        self.view.close_btn.clicked.connect(self.ui_close)

        # self._dir_path_model = model
        # self._dir_path_view = view.excel_path_view
        # set model
        # completer = QCompleter(self._dir_path_model)
        # self._dir_path_view.setCompleter(completer)

        # self.view.convert_btn.clicked.connect(self.set_excel_save)
        # self._shot_view.setAlternatingRowColors(True)
        # self._shot_view.header().setVisible(False)

    def set_project_combobox(self):
        """
        sg_mp(mapping api)를 통하여 project들을 combobox 에 넣어주는 함수이다.
        """
        projects = self.sg.get_active_project()
        for project in projects:
            self._project_combo_model._data_list.append(project)
        # self.set_seq_combobox()

    # def set_seq_combobox(self):
    #     """
    #     seq 콤보박스에 set 하는 함수이다.
    #     """
    #     # self._seq_combo_view.model().clear()
    #     user_project = self._project_combo_view.currentText()
    #     seqs = self.sg.get_seq_list(user_project)
    #     for seq in seqs:
    #         self._seq_combo_view.addItem(seq)
    #     self.set_shot_combobox()

    def set_shot_combobox(self):
        """
        shot 콤보박스에 set 하는 함수이다.
        """
        # self.shot_combboview.model().clear()
        user_project = self._project_combo_view.currentText()
        user_seq = self._seq_combo_view.currentText()
        shots = self.sg.get_shot_list(user_project, user_seq)
        for shot in shots:
            self._shot_view.addItem(shot)

    def selected_project(self, event):
        self.project_selection_dict = ""
        # self.set_seq_combobox()
        project_name = self._project_combo_view.currentText()
        self.project_selection = self.sg.select_get_project(project_name)

        self.set_shots()

    def set_shots(self):
        # project = self._project_combo_model
        # print(project)
        seqs, shots, _ = self.model.scan_org_copy(self._project_combo_view.currentText())
        # for shot in shots:
        #     shot_name = shot['code']
        #     print(shot_name)
        #
        #     for i in shot_name:
        #         asset_item = QTreeWidgetItem(self._shot_view)
        #         asset_item.setText(0, i)
        # model = QStringListModel()
        # model.setStringList(items)
        # print(seqs)
        print(shots)
        # for i in seqs:
        #     seq_item = QTreeView(self._shot_view)
        #     seq_item.setText(0, i)
        self._shot_model._data_list.clear()
        for shot in shots:
            self._shot_model._data_list.append(shot)
            self._shot_model.layoutChanged.emit()

    def sel_shot_get_copy_path(self):
        # self._org_path_view.clear()
        _, _, copy_path = self.model.scan_org_copy(self._project_combo_view.currentText())
        print(copy_path)
        # self._org_path_view.setText(copy_path)

    def set_org_copy(self):
        self.model.scan_org_copy()
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
