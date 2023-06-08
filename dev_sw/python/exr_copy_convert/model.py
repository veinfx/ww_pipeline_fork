import os
import shutil

from PySide2.QtCore import QStringListModel, Qt

from sg_mapping import SgMapping

sg = SgMapping()


class MyModel(QStringListModel):

    def __init__(self, data=None):
        super().__init__(data)
        self._data_list = []

    def data(self, index, role=Qt.DisplayRole):
        """Model의 선택된 index에 맞는 data를 반환해주는 메소드.
        """
        if role == Qt.DisplayRole:
            if 0 <= index.row() < len(self._data_list):
                return self._data_list[index.row()]
        return None

    def setData(self, index, value, role=Qt.EditRole):
        """ index에 새로운 value를 설정 EditRole일 경우 해당 인덱스의 데이터를 새로운 value로 변경하고,
        데이터 변경을 알리는 dataChanged 시그널을 발생
        """
        if role == Qt.EditRole:
            self._data_list[index.row()] = value
            self.dataChanged.emit(index, index, [Qt.DisplayRole])
            return True
        return False

    def rowCount(self, data=None):
        """모델의 행 개수를 반환"""
        return len(self._data_list)

    def flags(self, index):
        """모든 아이템이 선택 가능하고, 편집이 불가능"""
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def scan_org_copy(self, project):
        shots = sg.get_all_shots(project)
        shot_codes = []
        seq_name = []
        copy_path = []
        for shot in shots:
            shot_name = shot['code']
            shot_codes.append(shot_name)
            seq_name = shot['sg_sequence']['name']
            org_path = f'/show/{project}/seq/{seq_name}/{shot_name}/plate/org/'
            copy_path.append(org_path)
            # print(org_path)
        # shots_scan_path = sorted(list(set([shot['sg_scan_path'] for shot in shots])))
        # print(0, shots_scan_path)
        # a = os.listdir(shots_scan_path[0])
        # print(a)
        # for ai in a:
        #     print(ai)

        return seq_name, shot_codes, copy_path

    def get_shot_path(self):
        pass

    def copy_rename(self):
        # Source directories - relative or absolute paths.
        source = "./src/"
        destination = "./dest/"

        # A list of all files in the source directory
        files_in_src = os.listdir(source)

        # Iterate over all files on the source and copy them to the destination.
        for file in files_in_src:
            # for example, file = exclude.txt
            # os.path.join joins the source directory to the file to get a valid source path
            # , e.g./home/kiprono/Desktop/src/exclude.txt
            src_file = os.path.join(source, file)
            # splitext() splits the basename and extension from the filename
            # , eg exclude.txt becomes (exclude, .txt)
            filename, extension = os.path.splitext(file)
            # Create a new filename with the string "_copy" added to it
            new_file = f"{filename}_copy{extension}"
            # Join the destination folder with the new filename
            dest_file = os.path.join(destination, new_file)
            # If the destination file already exists, skip it
            if os.path.exists(dest_file):
                continue
            # Copy the source file to the destination folder with the new filename
            shutil.copy(src_file, dest_file)