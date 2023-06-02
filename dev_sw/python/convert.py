import ffmpeg

cat_jpg_path = '/home/west/chelsea.jpg'

exr_file_path = "/show/seine/production/scan/20221017_plate_scan/002_A130C005_220226_RPGF/A130C005_220226_RPGF.0001014.exr"


stream = ffmpeg.input(cat_jpg_path)

stream = ffmpeg.input(exr_file_path)


stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, '/home/west/A130C005_220226_RPGF.0001014.jpg')

ffmpeg.run(stream)