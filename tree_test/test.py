## test ##

from pprint import pprint
from openpyxl import Workbook

wb = Workbook()
ws = wb.active  ## 첫 번째 시트

header_list = [
    'check', 'thumbnail', 'roll', 'seq_name', 'shot_name', 'version', 'type',
    'scan_path', 'scan_name', 'clip_name', 'pad', 'ext', 'resoultion',
    'start_frame', 'end_frame', 'duration', 'retime_duration', 'retime_percent', 'retime_start_frame',
    'timecode_in', 'timecode_out', 'just_in', 'just_out', 'framerate', 'date', 'clip_tag'
]
for i, title in enumerate(header_list):
    ws.cell(row=1, column=i + 1, value=title)

data = [
    ['C255C014_220511_WOFX.1001.jpg', '/TD/dongjin/projects/gamja/production/scan/20221017_plate_scan/003_C255C014_220511_WOFX',
     'C255C014_220511_WOFX', 'C255C014_220511_WOFX', '%04d', 'exr', '3840 x 2160', '1001', '24000', '23000',
     '18:54:53:07', '18:54:54:00', '23.976', '2022-05-11 18:47:28'],
    ['C140C022_220304_WOFX.1001.jpg', '/TD/dongjin/projects/gamja/production/scan/20221017_plate_scan/001_C140C022_220304_WOFX',
     'C140C022_220304_WOFX', 'C140C022_220304_WOFX', '%04d', 'exr', '3840 x 2160', '1001', '24000', '23000',
     '12:05:15:09', '12:05:15:22', '23.976', '2022-03-04 11:59:46'],
    ['A130C005_220226_RPGF.1001.jpg', '/TD/dongjin/projects/gamja/production/scan/20221017_plate_scan/002_A130C005_220226_RPGF',
     'A130C005_220226_RPGF', 'A130C005_220226_RPGF', '%04d', 'exr', '3840 x 2160', '1001', '24000', '23000',
     '11:36:22:03', '11:36:22:20', '23.976', '2022-02-26 04:19:29']
]
data.sort(reverse=False)
pprint(data)

## 리스트를 행에 삽입.
for d in data:
    ws.append(  
    {
        'B': d[0],
        'H': d[1],
        'I': d[2],
        'J': d[3],
        'K': d[4],
        'L': d[5],
        'M': d[6],
        'N': d[7],
        'O': d[8],
        'P': d[9],
        'T': d[10],
        'U': d[11],
        'X': d[12],
        'Y': d[13]
        })

wb.save(r'C:\Users\jin91\PipelineTD\excel\test.xlsx')

# import ffmpeg
# import subprocess
#
# def convert_mov_to_seq():
#     input = r"/home/west/test/show/goguma/production/scan/20221017_plate_scan/001_C140C022_220304_WOFX/C140C022_220304_WOFX.0001001.exr"
#     output = r"/home/west/test/show/goguma/production/scan/20221017_plate_scan/001_C140C022_220304_WOFX/test.jpg"
#
#     cmd = f'ffmpeg -i "{input}" "{output}"'
#     print(cmd)
#     subprocess.check_output(cmd, shell=True)
#
# convert_mov_to_seq()

# self.data = []
# for root, dirs, files in os.walk(SCAN_PATH):
#     temp_list = []
#     if len(dirs) > 0:
#         for dir in dirs:
#             scan_path = os.path.join(root, dir)
#
#     if len(files) > 0:
#         files.sort(reverse=False)
#         tmp = files[0].split('.')
#         scan_name = tmp[0]
#         pad = '%0' + str(len(tmp[1])) + 'd'
#         ext = tmp[2]
#
#         temp_list.append(scan_path)
#         temp_list.append(scan_name)
#         temp_list.append(pad)
#         temp_list.append(ext)
#
#     self.data.append(temp_list)
#
# pprint(self.data)
# return self.data

# import sys
# import ffmpeg
# import pprint
#
# m_file = sys.argv[1]
# pprint(ffmpeg.probe(m_file))
# import os
#
# os.system('convert /home/west/test/C140C022_220304_WOFX.000100%d.exr[1-9] test.mp4')

#
# from wand.image import Image
#
# filename='/home/west/test/show/goguma/production/scan/20221017_plate_scan/001_C140C022_220304_WOFX/C140C022_220304_WOFX.0001001.exr'
#
# # exif = {}
# # with Image(filename) as image:
# #     exif.update((k[5:], v) for k, v in image.metadata.items()
# #                            if k.startswith('exif:'))
#
# with Image.convert('mp4') as converted:
#     converted.save(filename='/home/west/test/C140C022_220304_WOFX.000100%d.exr')
#
#
# import ffmpeg
# import pprint
#
# # filename=# EXR 파일 경로
# exr_file_path = "/show/seine/production/scan/20221017_plate_scan/002_A130C005_220226_RPGF/A130C005_220226_RPGF.0001014.exr"
#
# # EXR 파일 열기
# exr_file = OpenEXR.InputFile(exr_file_path)
#
# # 메타데이터 가져오기
# header = exr_file.header()
#
# # 모든 메타데이터 출력
# print("test:")
# for key, value in header.items():
#     print(f"{key}: {value}")
#
# # 파일 닫기
# exr_file.close()
#
# pprint(ffmpeg.probe(filename=filename))
#
#
# import OpenEXR
# # EXR 파일 경로
# exr_file_path = "/show/seine/production/scan/20221017_plate_scan/002_A130C005_220226_RPGF/A130C005_220226_RPGF.0001014.exr"
#
# # EXR 파일 열기
# exr_file = OpenEXR.InputFile(exr_file_path)
#
# # 메타데이터 가져오기
# header = exr_file.header()
#
# # 모든 메타데이터 출력
# print("test:")
# for key, value in header.items():
#     print(f"{key}: {value}")
#
# # 파일 닫기
# exr_file.close()
#
# from openpyxl import Workbook
# from openpyxl.drawing.image import Image
#
#
# wb = Workbook()
# ws = wb.active
#
# logo = Image(r'/home/west/test/test.jpg')
#
# # A bit of resizing to not fill the whole spreadsheet with the logo
# logo.height = 150
# logo.width = 250
#
# ws.add_image(logo, "A2")
#
# wb.save('/home/west/다운로드/dummy.csv')

# # Let's use the hello_world spreadsheet since it has less data
# workbook = load_workbook(filename="merging.xlsx")
# sheet = workbook.active
#
# logo = Image(r"logo.png")
#
# # A bit of resizing to not fill the whole spreadsheet with the logo
# logo.height = 150
# logo.width = 300
#
# sheet.add_image(logo, "E2")
# workbook.save(filename="logo.xlsx")





import os

from openpyxl import Workbook
from openpyxl.drawing.image import Image

# wb = Workbook()  ## 워크북 생성
# ws = wb.active  ## 첫 번째 시트
#
# ## 이미지 불러오기
# image_path = '/home/west/test/test.jpg'
#
# image = Image(image_path)
# image.height = 150
# image.width = 250
#
# ws.add_image(image, 'A1')  ## 이미지 삽입
#
# ## 이미지 픽셀을 셀 폭과 높이로 변환
# col_width, row_height = get_col_width_row_height(image.width, image.height)
#
# ws.column_dimensions['A'].width = col_width  ## 셀 폭 변경
# ws.row_dimensions[1].height = row_height  ## 셀 높이 변경
#
# wb.save('/home/west/test/one_image.xlsx')
# wb.close()

# wb = Workbook()  ## 워크북 생성
# ws = wb.active  ## 첫 번째 시트

# def thumbnail_data():
#     thumbnail_dir= r'C:\Users\jin91\PipelineTD\git\images'
#     thumbnail_lists = os.listdir(thumbnail_dir)

#     for i, thumbnail_list in enumerate(thumbnail_lists):
#         image = Image(os.path.join(thumbnail_dir, thumbnail_list))
#         image.width = 250
#         image.height = 150
#         col_width = image.width * 50 / 350   ## 엑셀 셀 폭 높이 단위
#         row_height = image.height * 250 / 300
#         ws.add_image(image, anchor='B' + str(i + 2))  ## 이미지 삽입
#         if i == 0:
#             ws.column_dimensions['B'].width = col_width  ## 셀 폭은 한 번만 변경
#         ws.row_dimensions[i + 2].height = row_height  ## 셀 높이 변경
#         ws.cell(row=i + 2, column=2, value=thumbnail_list) ## 이미지 경로 입력

#     wb.save(r'C:\Users\jin91\PipelineTD\git\images\test.xlsx')

# thumbnail_data()



