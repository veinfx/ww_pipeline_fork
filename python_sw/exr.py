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
