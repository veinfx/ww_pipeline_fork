import os
import glob
import shutil
import ffmpeg
import fileseq

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
        input_path = []
        copy_path = []
        for shot in shots:
            shot_name = shot['code']
            shot_codes.append(shot_name)
            seq_name = shot['sg_sequence']['name']
            scan_path = shot['sg_scan_path']
            input_path.append(scan_path)
            # print(scan_path)
            org_path = f'/show/{project}/seq/{seq_name}/{shot_name}/plate/org/'
            copy_path.append(org_path)
            # print(org_path)
        # shots_scan_path = sorted(list(set([shot['sg_scan_path'] for shot in shots])))
        # print(0, shots_scan_path)
        # a = os.listdir(shots_scan_path[0])
        # print(a)
        # for ai in a:
        #     print(ai)

        return seq_name, shot_codes, copy_path, input_path

    def get_all_files_in_dir(dir_path):
        """
        glob 모듈을 사용하여 디렉토리 경로에 있는 모든 파일명을 가져오고,
        os.path.isfile 함수를 사용하여 파일 여부를 확인한 뒤 파일명만 리스트에 추가
        """
        files = []
        for file_path in glob.glob(os.path.join(dir_path, '*.exr')):
            if os.path.isfile(file_path):
                files.append(file_path)
        return files

    def ffmpeg_convert(self):
        pass

    def get_shot_path(self, path):
        dir_path = path
        print(1, dir_path)
        seqs = fileseq.findSequencesOnDisk(dir_path)




def main():
    project = 'seine'
    data = MyModel()
    _, _, _, input_path = data.scan_org_copy(project)
    # print(input_path)
    for path in input_path:
        # print(1, path)
        data.get_shot_path(path)



if __name__ == '__main__':
    main()