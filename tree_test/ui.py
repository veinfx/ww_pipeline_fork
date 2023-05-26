from openpyxl import Workbook
import numpy as np

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