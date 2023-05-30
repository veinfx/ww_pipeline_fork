import os

from pprint import pprint
import ffmpeg
from ffmpeg import input
from ffmpeg import output

# INPUT_PATH = "/TD/show/hanjin/production/scan/20221017_plate_scan"
# root_path = INPUT_PATH.split('/production/scan')
#
# thumbnail_path = os.path.join(root_path[0], f'tmp/thumb{root_path[1]}')
# if not os.path.exists(thumbnail_path):
#     os.makedirs(thumbnail_path, exist_ok=True)


def get_thumbnail(INPUT_PATH):
    root_path = INPUT_PATH.split('/production/scan')
    thumbnail_path = os.path.join(root_path[0], f'tmp/thumb{root_path[1]}')
    if not os.path.exists(thumbnail_path):
        os.makedirs(thumbnail_path, exist_ok=True)

    exr_files_dict = {}
    for path, dirs, files in os.walk(INPUT_PATH):
        if len(files) > 0:
            files.sort(reverse=False)
            names = files[0].split('.exr')[0]
            exr_files_dict[os.path.join(path, files[0])] = names
    # for exr_file, file_name in exr_files_dict.items():
    #     ffmpeg.run(output(input(exr_file), f'{thumbnail_path}/{file_name}.jpg'))
    pprint(exr_files_dict)
    return thumbnail_path

get_thumbnail("/TD/show/hanjin/production/scan/20221017_plate_scan")
