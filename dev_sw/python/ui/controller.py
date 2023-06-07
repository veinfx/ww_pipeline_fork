#!/usr/bin/env python
# :coding: utf-8

import os
import sys
from collections import deque

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

        self._shot_model = QStandardItemModel()
        # self._shot_model.setHorizontalHeaderItem(['Name', 'Height', 'Weight'])

        self._shot_view = self.view.shot_view
        self._shot_view.header().setDefaultSectionSize(180)
        self._shot_view.setModel(self._shot_model)
        self.importData(data)
        self._shot_view.expandAll()

        self.set_project_combobox()
        # self.set_seq_combobox()

        self._project_combo_view.currentIndexChanged.connect(self.selected_project)

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

    def importData(self, data, root=None):
        self._shot_model.setRowCount(0)
        if root is None:
            root = self._shot_model.invisibleRootItem()
        seen = {}   # List of  QStandardItem
        values = deque(data)
        while values:
            value = values.popleft()
            if value['unique_id'] == 1:
                parent = root
            else:
                pid = value['parent_id']
                if pid not in seen:
                    values.append(value)
                    continue
                parent = seen[pid]
            unique_id = value['unique_id']
            parent.appendRow([
                QStandardItem(value['short_name']),
                QStandardItem(value['height']),
                QStandardItem(value['weight'])
            ])
            seen[unique_id] = parent.child(parent.rowCount() - 1)

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
        seqs, shots = self.model.scan_org_copy(self._project_combo_view.currentText())
        # for shot in shots:
        #     shot_name = shot['code']
        #     print(shot_name)
        #
        #     for i in shot_name:
        #         asset_item = QTreeWidgetItem(self._shot_view)
        #         asset_item.setText(0, i)
        # model = QStringListModel()
        # model.setStringList(items)
        print(seqs)
        print(shots)
        # for i in seqs:
        #     seq_item = QTreeView(self._shot_view)
        #     seq_item.(0, i)

            # for shot in shots:
            #     print(shot)

            # self._shot_model = QStringListModel()
            # self._shot_model.setStringList(shot)
            # self._shot_model._data_list.append(shot)
            # self._shot_view.(shot)

            # self._shot_model.data.append(shot)

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

    data = [
        {'unique_id': 1, 'parent_id': 0, 'short_name': '', 'height': ' ', 'weight': ' '},
        {'unique_id': 2, 'parent_id': 1, 'short_name': 'Class 1', 'height': ' ', 'weight': ' '},
        {'unique_id': 3, 'parent_id': 2, 'short_name': 'Lucy', 'height': '162', 'weight': '50'},
        {'unique_id': 4, 'parent_id': 2, 'short_name': 'Joe', 'height': '175', 'weight': '65'},
        {'unique_id': 5, 'parent_id': 1, 'short_name': 'Class 2', 'height': ' ', 'weight': ' '},
        {'unique_id': 6, 'parent_id': 5, 'short_name': 'Lily', 'height': '170', 'weight': '55'},
        {'unique_id': 7, 'parent_id': 5, 'short_name': 'Tom', 'height': '180', 'weight': '75'},
        {'unique_id': 8, 'parent_id': 1, 'short_name': 'Class 3', 'height': ' ', 'weight': ' '},
        {'unique_id': 9, 'parent_id': 8, 'short_name': 'Jack', 'height': '178', 'weight': '80'},
        {'unique_id': 10, 'parent_id': 8, 'short_name': 'Tim', 'height': '172', 'weight': '60'}
    ]

    main()
