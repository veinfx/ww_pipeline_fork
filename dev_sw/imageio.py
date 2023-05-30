import imageio.v3 as iio

# EXR 파일 경로
exr_file_path = "/show/seine/production/scan/20221017_plate_scan/002_A130C005_220226_RPGF/A130C005_220226_RPGF.0001014.exr"

# EXR 파일 열기
exr_data = iio.imread(exr_file_path)


print(exr_data)
# 메타데이터 확인
metadata = exr_data.meta

# 메타데이터 출력 또는 처리
print("Metadata:")
for key, value in metadata.items():
    print(f"{key}: {value}")

