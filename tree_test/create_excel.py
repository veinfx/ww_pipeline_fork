import os
from pprint import pprint

from openpyxl import Workbook
from openpyxl.drawing.image import Image
# from openpyxl.styles.fonts import Font


ROOT_DIR = '/TD/show'
project_name = 'hanjin'
project_dir = os.path.join(ROOT_DIR, project_name)
# scan_dir = os.path.join(project_dir, 'production/scan')
excel_path = os.path.join(project_dir, 'production/excel')
thumbnail_path = os.path.join(project_dir, 'tmp/thumb')

SCAN_PATH = "/TD/show/hanjin/production/scan/20221017_plate_scan"


class CreateExcel:
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.title = 'Shot'
        self.dir_name = os.path.basename(SCAN_PATH).split('_')[0]

    def set_header(self):
        header_list = [
            'check', 'thumbnail', 'roll', 'seq_name', 'shot_name', 'version', 'type',
            'scan_path', 'scan_name', 'clip_name', 'pad', 'ext', 'resoultion',
            'start_frame', 'end_frame', 'duration', 'retime_duration', 'retime_percent', 'retime_start_frame',
            'timecode_in', 'timecode_out', 'just_in', 'just_out', 'framerate', 'date', 'clip_tag'
        ]

        for i, title in enumerate(header_list):
            self.ws.cell(row=1, column=i + 1, value=title)

    def get_data(self):
        self.data = []
        for path, dirs, files in os.walk(SCAN_PATH):
            temp_list = []
            if len(files) == 0:
                pass
            else:
                temp_list.append(path)
                files.sort(reverse=False)
                tmp = files[0].split('.')
                scan_name = tmp[0]
                pad = '%0' + str(len(tmp[1])) + 'd'
                ext = tmp[2]
                temp_list.append(scan_name)
                temp_list.append(pad)
                temp_list.append(ext)

            self.data.append(temp_list)
        pprint(self.data)
        return self.data

    def insert_data(self):
        # thumbnail
        img_dir = thumbnail_path
        img_file_list = os.listdir(img_dir)

        for i, img_file in enumerate(img_file_list):
            image_path = os.path.join(img_dir, img_file)
            image = Image(image_path)
            image.width = 250
            image.height = 150

            col_width = image.width * 50 / 350
            row_height = image.height * 250 / 300

            self.ws.add_image(image, anchor='B' + str(i + 2))
            if i == 0:
                self.ws.column_dimensions['B'].width = col_width
            self.ws.row_dimensions[i + 2].height = row_height
            self.ws.cell(row=i + 2, column=2, value=img_file)

        # other_data
        for d in self.data:
            for row in range(len(self.data)):
                scan_path = d[0]
                scan_name = d[1]
                pad = d[2]
                ext = d[3]
                self.ws.append(
                    {'H': scan_path},
                    {'I': scan_name},
                    {'k': pad},
                    {'L': ext}
                )

    def save_excel_file(self):
        name = self.dir_name + ".xls"
        save_dir_path = os.path.join(excel_path, name)
        self.wb.save(save_dir_path)


if __name__ == "__main__":
    ce = CreateExcel()
    ce.set_header()
    ce.get_data()
    ce.insert_data()
    ce.save_excel_file()


