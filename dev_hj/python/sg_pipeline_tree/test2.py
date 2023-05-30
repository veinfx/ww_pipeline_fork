import os

from rez.utils import yaml

import shotgun_api3

SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
SCRIPT_NAME = 'script_Ihj'
SCRIPT_KEY = 'uhu1jgfrjmhwEznoul@btwkqd'

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

# 야멜 파일 경로
YAML_FILE_PATH = "/home/west/HJ_config/Ihj_config/config/core/schema/project/sequences/sequence/shot.yml"

# def create_shot_folder(yaml_path):
#     # 야멜 파일 로드
#     with open(yaml_path, "r") as f:
#         yaml_data = yaml.safe_load(f)
#
#     # ShotGrid API를 사용하여 Shot 폴더 생성
#     for entity_type, entity_data in yaml_data.items():
#         if entity_type == "shotgun_entity":
#             entity_field = entity_data.get("name")
#             entity_entity_type = entity_data.get("entity_type")
#             entity_filters = entity_data.get("filters")
#
#             # ShotGrid API를 사용하여 ShotGrid 엔티티 가져오기
#             entities = sg.find(entity_entity_type, entity_filters, fields=[entity_field])
#
#             # Shot 폴더 생성
#             for entity in entities:
#                 folder_name = entity.get(entity_field)
#                 if folder_name:
#                     # ShotGrid API를 사용하여 Shot 폴더 생성
#                     sg.create("Folder", {"name": folder_name, "project": {"type": "Project", "id": sg.project_id}})
#                     print(f"Created folder '{folder_name}' for {entity_entity_type} '{entity.get('name')}'.")
#
# # Shot 폴더 생성 함수 호출
# create_shot_folder(YAML_FILE_PATH)


# 로컬 폴더 경로
LOCAL_FOLDER_PATH = "/home/west/test"


def create_shot_folder(yaml_path, local_folder_path):
    # Load the YAML file
    with open(yaml_path, "r") as f:
        yaml_data = yaml.load(f)

    # Use ShotGrid API to create Shot folders
    for entity_type, entity_data in yaml_data.items():
        if entity_type == "shotgun_entity":
            entity_field = entity_data.get("name")
            entity_entity_type = entity_data.get("entity_type")
            entity_filters = entity_data.get("filters")

            # Use ShotGrid API to retrieve ShotGrid entities
            entities = sg.find(entity_entity_type, entity_filters, fields=[entity_field])

            # Create Shot folders
            for entity in entities:
                folder_name = entity.get(entity_field)
                if folder_name:
                    # Create local folder path
                    local_path = os.path.join(local_folder_path, folder_name)

                    # Create local folder
                    os.makedirs(local_path, exist_ok=True)
                    print(f"Created folder '{local_path}' for {entity_entity_type} '{entity.get('name')}'.")

# Call the Shot folder creation function
create_shot_folder(YAML_FILE_PATH, LOCAL_FOLDER_PATH)
