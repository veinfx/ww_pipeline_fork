import fileseq


project_name = 'seine'
# input_data = input("scan data dir name : ")
input_dir_1 = '20221017_plate_scan'
input_dir_2 = '001_C140C022_220304_WOFX'
# input_dir_2 = '002_A130C005_220226_RPGF'

# path = f'/show/{project_name}/production/scan/{input_dir_1}'
dir_path = f'/show/{project_name}/production/scan/{input_dir_1}/{input_dir_2}/'

# print(1, dir_path)


# print(2, dir(fileseq))
seqs = fileseq.findSequencesOnDisk(dir_path)
# seqs = fileseq.findSequencesOnDisk(path)
print(seqs)
# seq = fileseq.findSequencesOnDisk(dir_path + '/' + input_dir_2[4:] + '.@.exr')
# print(seq)
for item in seqs:
    print(1, dir(item))
    break

for item in seqs:
    print(item.frameRange())

for item in seqs:
    print(item.start(), item.end())
# 1001 1111

# for item in seqs:
#     item.copy('~/sw/')

# seqs.format(template='{dirname}{basename}{padding}{extension}')
for item in seqs:
    a = ''.join([item.dirname(), item.basename(), '%0{}d'.format(len(str(item.end()))), item.extension()])
    print(11, a)
