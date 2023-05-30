import os
import glob

# import fileseq

# filepath = os.path.dirname(os.path.realpath(__file__))
#
# print(filepath)

project_name = 'seine'
# input_data = input("scan data dir name : ")
input_dir_1 = '20221017_plate_scan'
input_dir_2 = '001_C140C022_220304_WOFX'
input_dir_2 = '002_A130C005_220226_RPGF'

dir_path = f'/show/{project_name}/production/scan/{input_dir_1}/{input_dir_2}'
print(dir_path)


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


exr_file_path = get_all_files_in_dir(dir_path)
print(exr_file_path[0])


import OpenEXR

# EXR 파일 경로
# exr_file_path = "파일경로.exr"

# EXR 파일 열기
exr_file = OpenEXR.InputFile(exr_file_path)

# 메타데이터 가져오기
header = exr_file.header()

# 메타데이터 출력 또는 처리
metadata = header['']
for key, value in metadata.items():
    # 여기에 원하는 작업을 수행하거나 메타데이터를 출력할 수 있습니다.
    print(f"{key}: {value}")

# 파일 닫기
exr_file.close()





# seq = fileseq.FileSequence("/show/seine/production/scan/20221017_plate_scan/001_C140C022_220304_WOFX/C140C022_220304_WOFX.000100#.exr")
# seq.format(template='{dirname}{basename}{padding}{extension}')
# seqs = fileseq.findSequencesOnDisk(dir_path)
# print(seqs)