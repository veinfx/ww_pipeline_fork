import os
import re

from openpyxl import *

path = '/home/west/HJ_root/ihj/production/excel/230523_Ihj.xlsx'

excel = load_workbook(path)

excel_test = excel.active

cell_obj = excel_test.cell(row = 3, column = 2)

print(cell_obj.value)

class ReNamer:

    def __init__(self):

        self._input_path = None
        self._old_text = []
        self._new_text = []

        self.files_list = []
        self.search_text_list = []
        self.edit_text_list = []

    @property
    def input_path(self):
        return self._input_path

    @input_path.setter
    def input_path(self, value):
        if value is None or value == "":
            raise ValueError("Input path is missing.")
        self._input_path = value

    @property
    def old_text(self):
        return self._old_text

    @old_text.setter
    def old_text(self, value):
        if value is None or not isinstance(value, (list, tuple)):
            raise ValueError("Old name must be a list or a tuple.")
        self._old_text = value

    @property
    def new_text(self):
        return self._new_text

    @new_text.setter
    def new_text(self, value):
        if value is None or not isinstance(value, (list, tuple)):
            raise ValueError("New name must be a list or a tuple.")
        self._new_text = value

    def selected_files(self):
        self.files_list = []
        for file in os.listdir(self.input_path):
            if os.path.isfile(os.path.join(self.input_path, file)):
                self.files_list.append(file)
                self.files_list.sort(key=lambda x: int(re.search(r"\d+", x).group(0)))
        if len(self.files_list) == 0:
            raise Exception("No files found in the directory.")
        return self.files_list

    def search_text(self):
        self.search_text_list = []
        for old_file in self.files_list:
            for old_text in self.old_text:
                if re.search(old_text, old_file):
                    self.search_text_list.append(old_file)
                    self.search_text_list.sort(key=lambda x: int(re.search(r"\d+", x).group(0)))
                    print(f"거름망{old_file}")
                    break
        return self.search_text_list

    def edit_text(self):
        self.edit_text_list = []
        for new_file in range(len(self.search_text_list)):
            old_name = self.search_text_list[new_file]
            new_name = old_name
            for i in range(len(self.old_text)):
                new_name = new_name.replace(self.old_text[i], self.new_text[i])
                print(f"바꼇{new_name}")
            if old_name != new_name:
                self.edit_text_list.append(new_name)
                self.edit_text_list.sort(key=lambda x: int(re.search(r"\d+", x).group(0)))
        if len(self.edit_text_list) == 0:
            raise Exception("No files to be renamed.")
        return self.edit_text_list

    def rename_files(self):
        for old_names, new_names in zip(self.search_text_list, self.edit_text_list):
            print(f"막올{old_names}, 막뉴{new_names}")
            print("123", self.input_path)
            os.rename(os.path.join(self.input_path, old_names), os.path.join(self.input_path, new_names))


def main():
    rn = ReNamer()

    # setter test info
    # rn.input_path = r"/home/west/github/file_renamer/IHJ_JOKER_0020"
    # rn.old_text = ["IHJ", "JOKER"]
    # rn.new_text = ["HJ", "JOK"]
    #
    # print(f"하마{rn.selected_files()}")
    # print(f"고양이{rn.search_text()}")
    # print(f"강아지{rn.edit_text()}")
    # print(f"토끼{rn.rename_files()}")


if __name__ == '__main__':
    main()
