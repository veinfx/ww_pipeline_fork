import os
import re

from openpyxl import *


class ExcelCreated:

    def __init__(self):

        self._input_path = None

        self.files_list = []

        self.file_name = []

    @property
    def input_path(self):
        return self._input_path

    @input_path.setter
    def input_path(self, value):
        if value is None or value == "":
            raise ValueError("Input path is missing.")
        self._input_path = value

    def selected_files(self):
        self.files_list = []
        for file in os.listdir(self.input_path):
            if os.path.isfile(os.path.join(self.input_path, file)):
                self.files_list.append(file)
                self.files_list.sort(key=lambda x: int(re.search(r"\d+", x).group(0)))
        if len(self.files_list) == 0:
            raise Exception("No files found in the directory.")
        return self.files_list

    # def excel_data(self):

    def excel_create(self):

        # 새로운 엑셀 파일 생성
        workbook = Workbook()
        sheet = workbook.active

        # 파일 이름 시트에 넣기
        for index, file_name in enumerate(self.files_list, start=1):
            sheet.cell(row=index, column=1, value=file_name)

        # 엑셀 파일 저장
        workbook.save("파일명2.xlsx")



def main():
    ec = ExcelCreated()

    # setter test info
    ec.input_path = r"/home/west/HJ_root/ihj/production/scan/20221018_plate_scan/001_C140C022_220304_WOFX"
    # ec.old_text = ["IHJ", "JOKER"]
    # ec.new_text = ["HJ", "JOK"]

    print(f"하마{ec.selected_files()}")

    print(f"mack{ec.excel_create()}")


if __name__ == '__main__':
    main()