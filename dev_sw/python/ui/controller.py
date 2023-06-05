#!/usr/bin/env python
# :coding: utf-8

import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *

from model import MyModel
from view import MyView
from sg_mp import SgMapping


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

        self.view = MyView()

        self._project_combo_model = MyModel()
        self._project_combo_view = self.view.project_combo_view

        self._project_combo_view.setModel(self._project_combo_model)

        self.set_project_combobox()

        self.view.copy_btn.clicked.connect(self.set_copy)
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

    def set_copy(self):
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

    def get_asset_shot_info_to_url(self, url):
        """sys.argv 로 받은 샷그리드의 url 정보를 핸들러와 샷그리드 api 로 필요한 정보들을 가져오는 함수이다.
        """
        # sa = ShotgunAction(url)
        # sg = ShotgunApi()
        # self._project_name = sa.project['name']
        #
        # entity_type = sa.entity_type
        # if entity_type not in ["Asset", "Shot"]:
        #     raise ValueError("Invaild entity type {}".format(entity_type))
        #
        # elif entity_type == "Asset":
        #     asset_ids = sa.selected_ids
        #     # asset_ids_filter = sa.selected_ids_filter
        #     asset_info, _ = sg.get_user_data_info(entity_type, asset_ids)
        #     self._asset_info = asset_info
        #
        # elif entity_type == "Shot":
        #     shot_ids = sa.selected_ids
        #     # shot_ids_filter = sa.selected_ids_filter
        #     _, shot_info = sg.get_user_data_info(entity_type, shot_ids)
        #     self._shot_info = shot_info

    def set_excel_save(self):
        """
        xls save 버튼 클릭시 실행되는 함수이다.
        enumerate() 함수를 사용하여 행 인덱스를 1부터 시작
        """
        workbook = Workbook()
        sheet = workbook.active

        # sheet.title = self._project_name
        # sheet.title = "self._project_name"

        if self._asset_info:
            assets = self._asset_info

            sheet['A1'] = 'Asset Name'
            sheet['B1'] = 'Asset Status'
            sheet['C1'] = 'Asset Type'

            for i, asset in enumerate(assets):
                sheet.cell(row=i+2, column=1, value=asset['code'])
                sheet.cell(row=i+2, column=2, value=asset['sg_status_list'])
                sheet.cell(row=i+2, column=3, value=asset['sg_asset_type'])

        elif self._shot_info:
            shots = self._shot_info

            sheet['A1'] = 'Shot Name'
            sheet['B1'] = 'Shot Status'
            sheet['C1'] = 'Sequence Name'

            for i, shot in enumerate(shots):
                sheet.cell(row=i+2, column=1, value=shot['code'])
                sheet.cell(row=i+2, column=2, value=shot['sg_status_list'])
                sheet.cell(row=i+2, column=3, value=shot['sg_sequence']['name'])

        sheet.column_dimensions['A'].width = 20
        # workbook.save(self._dir_path)
        workbook.save(self._dir_path_view.displayText())
        workbook.close()
        self.view.excel_create_btn_messagebox()


def main():
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    controller = MyController()
    controller.view.show()
    app.exec_()


if __name__ == "__main__":
    main()
