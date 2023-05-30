## test ##

from openpyxl import Workbook

wb = Workbook()
ws = wb.active  ## 첫 번째 시트
data = [
    ['1', 'a'],
    ['2', 'b']
]

## 리스트를 행에 삽입.
for d in data:
    for row in range(len(data)):
        print(len(data))
        ws.append({'A': d[0], 'C': d[1]})  # @ ws.append({1:random_int1, 3:random_int2}과 동일

wb.save('/TD/show/hanjin/production/excel/test.xlsx')

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
import ffmpeg
import pprint

# filename=# EXR 파일 경로
exr_file_path = "/show/seine/production/scan/20221017_plate_scan/002_A130C005_220226_RPGF/A130C005_220226_RPGF.0001014.exr"

# EXR 파일 열기
exr_file = OpenEXR.InputFile(exr_file_path)

# 메타데이터 가져오기
header = exr_file.header()

# 모든 메타데이터 출력
print("test:")
for key, value in header.items():
    print(f"{key}: {value}")

# 파일 닫기
exr_file.close()

pprint(ffmpeg.probe(filename=filename))


import OpenEXR
# EXR 파일 경로
exr_file_path = "/show/seine/production/scan/20221017_plate_scan/002_A130C005_220226_RPGF/A130C005_220226_RPGF.0001014.exr"

# EXR 파일 열기
exr_file = OpenEXR.InputFile(exr_file_path)

# 메타데이터 가져오기
header = exr_file.header()

# 모든 메타데이터 출력
print("test:")
for key, value in header.items():
    print(f"{key}: {value}")

# 파일 닫기
exr_file.close()

from openpyxl import Workbook
from openpyxl.drawing.image import Image


wb = Workbook()
ws = wb.active

logo = Image(r'/home/west/test/test.jpg')

# A bit of resizing to not fill the whole spreadsheet with the logo
logo.height = 150
logo.width = 250

ws.add_image(logo, "A2")

wb.save('/home/west/다운로드/dummy.csv')

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


def get_col_width_row_height(img_width, img_height):
    col_width = img_width * 63.2 / 504.19
    # row_height = img_height * 225.35 / 298.96
    row_height = img_height * 250 / 298.96
    return col_width, row_height


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

wb = Workbook()  ## 워크북 생성
ws = wb.active  ## 첫 번째 시트

img_dir = '/home/west/test/images'
img_file_list = os.listdir(img_dir)  ## 이미지 파일 리스트

for i, img_file in enumerate(img_file_list):
    image_path = os.path.join(img_dir, img_file)  ## 이미지 경로
    image = Image(image_path)  ## 이미지 로드
    image.height = 150
    image.width = 250
    ws.add_image(image, anchor='A' + str(i +2))  ## 이미지 삽입
    col_width, row_height = get_col_width_row_height(image.width, image.height)  ## 엑셀 셀 폭 높이 단위
    if i == 0:
        ws.column_dimensions['A'].width = col_width  ## 셀 폭은 한 번만 변경
    ws.row_dimensions[i + 2].height = row_height  ## 셀 높이 변경
    ws.cell(row=i + 2, column=1, value=img_file)  ## 첫 번째 칼럼에 이미지 경로 입력

wb.save('/home/west/test/multiple_images.xlsx')
