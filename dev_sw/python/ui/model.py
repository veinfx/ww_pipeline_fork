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
        # print(shots)
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


# def main():
#     project = 'seine'
#     data = MyModel()
#     data.scan_org_copy(project)
#
#
# if __name__ == '__main__':
#     main()