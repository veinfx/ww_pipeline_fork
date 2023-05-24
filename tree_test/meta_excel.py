import os

from openpyxl import Workbook
from openpyxl.drawing.image import Image
# from openpyxl.styles.fonts import Font


# class CreateExcel:
#     def __init__(self) -> None:
        
#         self.wb = Workbook()
#         self.ws = self.wb.active
#         self.ws.title = 'Shot'
#         # ws = wb.create_sheet(title="Shot")
#         header_list = [
#             'check', 'thumbnail', 'roll', 'seq_name', 'shot_name', 'version', 'type', 
#             'scan_path', 'scan_name', 'clip_name', 'pad', 'ext', 'resoultion', 
#             'start_frame', 'end_frame', 'duration', 'retime_duration', 'retime_percent', 'retime_start_frame', 
#             'timecode_in', 'timecode_out', 'just_in', 'just_out', 'framerate', 'date', 'clip_tag'
#             ]
        
#         for i, title in enumerate(header_list):
#             self.ws.cell(row=1, column=i + 1, value=title)
        
#         # img_dir = '/home/west/test/images'
#         img_dir = 'C:/Users/jin91/PipelineTD/git/images'
#         img_file_list = os.listdir(img_dir)

#         for i, img_file in enumerate(img_file_list):
#             print(i, img_file)
#             image_path = os.path.join(img_dir, img_file)
#             image = Image(image_path)
#             image.height = 150
#             image.width = 250
#             self.ws.add_image(image, anchor='B' + str(i +2))
#             col_width, row_height = ce.get_col_width_row_height(image.width, image.height)  ## 엑셀 셀 폭 높이 단위
#             if i == 0:
#                 self.ws.column_dimensions['B'].width = col_width  ## 셀 폭은 한 번만 변경
#             self.ws.row_dimensions[i + 2].height = row_height  ## 셀 높이 변경
#             self.ws.cell(row=i + 2, column=1, value=img_file)  ## 첫 번째 칼럼에 이미지 경로 입력
            
#         self.wb.save("C:/Users/jin91/PipelineTD/git/test2.xls")
    
    # def get_file_name(self):
    #     pass

    # def extract_metadata(self):
    #     pass
    
    # def get_infoo(self):
    #     pass

    # def input_data(self):
    #     pass

    # def get_col_width_row_height(img_width, img_height):
    #     col_width = img_width * 63.2 / 504.19
    #     # row_height = img_height * 225.35 / 298.96
    #     row_height = img_height * 250 / 298.96
    #     return col_width, row_height

    # def input_thumbnail(self):
    #     # img_dir = '/home/west/test/images'
    #     img_dir = 'C:/Users/jin91/PipelineTD/git/images'
    #     img_file_list = os.listdir(img_dir)

    #     for i, img_file in enumerate(img_file_list):
    #         print(i, img_file)
    #         image_path = os.path.join(img_dir, img_file)
    #         image = Image(image_path)
    #         image.height = 150
    #         image.width = 250
    #         self.ws.add_image(image, anchor='A' + str(i +2))  ## 이미지 삽입
    #         # col_width, row_height = ce.get_col_width_row_height(image.width, image.height)  ## 엑셀 셀 폭 높이 단위
    #         # if i == 0:
    #         #     self.ws.column_dimensions['B'].width = col_width  ## 셀 폭은 한 번만 변경
    #         # self.ws.row_dimensions[i + 2].height = row_height  ## 셀 높이 변경
    #         self.ws.cell(row=i + 2, column=1, value=img_file)  ## 첫 번째 칼럼에 이미지 경로 입력


# if __name__ == "__main__":
    # ce = CreateExcel()
    # ce.input_thumbnail()



def get_col_width_row_height(img_width, img_height):
    col_width = img_width * 50 / 350
    row_height = img_height * 250 / 300
    return col_width, row_height

wb = Workbook()
ws = wb.active
ws.title = 'Shot'
# ws = wb.create_sheet(title="Shot")
header_list = [
    'check', 'thumbnail', 'roll', 'seq_name', 'shot_name', 'version', 'type', 
    'scan_path', 'scan_name', 'clip_name', 'pad', 'ext', 'resoultion', 
    'start_frame', 'end_frame', 'duration', 'retime_duration', 'retime_percent', 'retime_start_frame', 
    'timecode_in', 'timecode_out', 'just_in', 'just_out', 'framerate', 'date', 'clip_tag'
    ]

for i, title in enumerate(header_list):
    ws.cell(row=1, column=i + 1, value=title)

# img_dir = '/home/west/test/images'
img_dir = 'C:/Users/jin91/PipelineTD/git/images'
img_file_list = os.listdir(img_dir)

for i, img_file in enumerate(img_file_list):
    print(i, img_file)
    image_path = os.path.join(img_dir, img_file)
    image = Image(image_path)
    image.height = 150
    image.width = 250
    ws.add_image(image, anchor='B' + str(i +2))
    col_width, row_height = get_col_width_row_height(image.width, image.height)  ## 엑셀 셀 폭 높이 단위
    if i == 0:
        ws.column_dimensions['B'].width = col_width  ## 셀 폭은 한 번만 변경
    ws.row_dimensions[i + 2].height = row_height  ## 셀 높이 변경
    ws.cell(row=i + 2, column=2, value=img_file)  
    
wb.save("C:/Users/jin91/PipelineTD/git/test2.xls")