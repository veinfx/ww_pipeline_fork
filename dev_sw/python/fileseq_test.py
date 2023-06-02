import fileseq


project_name = 'seine'
# input_data = input("scan data dir name : ")
input_dir_1 = '20221017_plate_scan'
input_dir_2 = '001_C140C022_220304_WOFX'
# input_dir_2 = '002_A130C005_220226_RPGF'

dir_path = f'/show/{project_name}/production/scan/{input_dir_1}/{input_dir_2}/'
# print(1, dir_path)


# print(2, dir(fileseq))
seqs = fileseq.findSequencesOnDisk(dir_path)
print(seqs)
# seq = fileseq.findSequencesOnDisk(dir_path + '/' + input_dir_2[4:] + '.@.exr')
# print(seq)
for item in seqs:
    print(dir(item))
    break

for item in seqs:
    print(item.frameRange())

for item in seqs:
    print(item.start(), item.end())
# 1001 1111