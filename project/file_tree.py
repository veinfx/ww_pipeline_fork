import os
import json
import shotgun_api3
import schedule
import time

# ShotGrid connection settings
SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
SCRIPT_NAME = "script_wongyu"
API_KEY = "mh3lwvof$rzkUtqndqsfqcckf"

# Connect to ShotGrid
sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, API_KEY)


def generate_file_tree(project_id, base_path):
    """
    Generate a file tree for the given project in ShotGrid.
    """
    file_tree = {
        "name": "Project",
        "path": "",
        "children": []
    }

    # Get all sequences in the project
    sequences = sg.find("Sequence", [["project", "is", {"type": "Project", "id": project_id}]], ["code"])
    for sequence in sequences:
        sequence_tree = {
            "name": sequence["code"],
            "path": os.path.join(base_path, "Sequences", sequence["code"]),
            "children": []
        }

        # Get all shots in the sequence
        shots = sg.find("Shot",
                        [["project", "is", {"type": "Project", "id": project_id}], ["sg_sequence", "is", sequence]],
                        ["code"])
        for shot in shots:
            shot_path = os.path.join(sequence_tree["path"], shot["code"])
            os.makedirs(shot_path, exist_ok=True)
            sequence_tree["children"].append({
                "name": shot["code"],
                "path": shot_path
            })

        file_tree["children"].append(sequence_tree)

    # Convert the tree to a JSON string
    json_string = json.dumps(file_tree, indent=4)

    # Save the JSON string as a file
    file_path = os.path.join(base_path, "file_tree.json")
    with open(file_path, "w") as file:
        file.write(json_string)

    print(f"File tree updated at {file_path}")


def update_file_tree(project_id, project_path):
    """
    Function to update the file tree periodically.
    """
    generate_file_tree(project_id, project_path)


def handle_event_notification(event_data):
    """
    Function to handle event notifications from ShotGrid.
    """
    # Extract relevant information from the event data
    event_type = event_data.get("event_type")
    entity_type = event_data.get("entity_type")
    entity_id = event_data.get("entity_id")

    # Check if the event is for a new asset, shot, or sequence
    if event_type == "Shotgun_Asset_New":
        print("New asset added")
    elif event_type == "Shotgun_Shot_New":
        print("New shot added")
    elif event_type == "Shotgun_Seq_New":
        print("New sequence added")

    # Update the file tree
    update_file_tree(project_id, project_path)


# Example usage
project_id = 299  # Replace with your project ID
project_path = "/TD/WG_test/project/zombie_city"  # Absolute project path

# Schedule the job to run every 1 hour
schedule.every(1).hours.do(update_file_tree, project_id=project_id, project_path=project_path)

# Run the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)

# #
# # import os
# # import json
# # import shotgun_api3
# #
# # # ShotGrid connection settings
# # SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
# # SCRIPT_NAME = "script_wongyu"
# # API_KEY = "mh3lwvof$rzkUtqndqsfqcckf"
# #
# # # Connect to ShotGrid
# # sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, API_KEY)
# #
# # def generate_file_tree(project_id, base_path):
# #     """
# #     Generate a file tree for the given project in ShotGrid.
# #     """
# #     file_tree = {
# #         "name": "Project",
# #         "path": base_path,
# #         "children": []
# #     }
# #
# #     # Get all assets in the project
# #     assets = sg.find("Asset", [["project", "is", {"type": "Project", "id": project_id}]], ["code"])
# #     asset_tree = {
# #         "name": "Assets",
# #         "path": os.path.join(base_path, "Assets"),
# #         "children": []
# #     }
# #     for asset in assets:
# #         asset_path = os.path.join(asset_tree["path"], asset["code"])
# #         os.makedirs(asset_path, exist_ok=True)
# #         asset_tree["children"].append({
# #             "name": asset["code"],
# #             "path": asset_path
# #         })
# #     file_tree["children"].append(asset_tree)
# #
# #     # Get all shots in the project
# #     shots = sg.find("Shot", [["project", "is", {"type": "Project", "id": project_id}]], ["code"])
# #     shot_tree = {
# #         "name": "Shots",
# #         "path": os.path.join(base_path, "Shots"),
# #         "children": []
# #     }
# #     for shot in shots:
# #         shot_path = os.path.join(shot_tree["path"], shot["code"])
# #         os.makedirs(shot_path, exist_ok=True)
# #         shot_tree["children"].append({
# #             "name": shot["code"],
# #             "path": shot_path
# #         })
# #     file_tree["children"].append(shot_tree)
# #
# #     return file_tree
# #
# # # Example usage
# # project_id = 299  # Replace with your project ID
# # project_path = "/TD/WG_test/project/zombie_city"
# # tree = generate_file_tree(project_id, project_path)
# #
# # # Convert the tree to a JSON string
# # json_string = json.dumps(tree, indent=4)
# #
# # # Save the JSON string as a file
# # file_path = os.path.join(project_path, "file_tree.json")
# # with open(file_path, "w") as file:
# #     file.write(json_string)
# #
# # print(f"File tree saved at {file_path}")
#
# import os
# import json
# import shotgun_api3
#
# # ShotGrid connection settings
# SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
# SCRIPT_NAME = "script_wongyu"
# API_KEY = "mh3lwvof$rzkUtqndqsfqcckf"
#
# # Connect to ShotGrid
# sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, API_KEY)
#
# def generate_file_tree(project_id, base_path):
#     """
#     Generate a file tree for the given project in ShotGrid.
#     """
#     file_tree = {
#         "name": "Project",
#         "path": "",
#         "children": []
#     }
#
#     # Get all sequences in the project
#     sequences = sg.find("Sequence", [["project", "is", {"type": "Project", "id": project_id}]], ["code"])
#     for sequence in sequences:
#         sequence_tree = {
#             "name": sequence["code"],
#             "path": os.path.join(base_path, "Sequences", sequence["code"]),
#             "children": []
#         }
#
#         # Get all shots in the sequence
#         shots = sg.find("Shot", [["project", "is", {"type": "Project", "id": project_id}], ["sg_sequence", "is", sequence]], ["code"])
#         for shot in shots:
#             shot_path = os.path.join(sequence_tree["path"], shot["code"])
#             os.makedirs(shot_path, exist_ok=True)
#             sequence_tree["children"].append({
#                 "name": shot["code"],
#                 "path": shot_path
#             })
#
#         file_tree["children"].append(sequence_tree)
#
#     return file_tree
#
# # Example usage
# project_id = 299  # Replace with your project ID
# project_path = "/TD/WG_test/project/zombie_city"  # Absolute project path
# tree = generate_file_tree(project_id, project_path)
#
# # Convert the tree to a JSON string
# json_string = json.dumps(tree, indent=4)
#
# # Save the JSON string as a file
# file_path = os.path.join(project_path, "file_tree.json")
# with open(file_path, "w") as file:
#     file.write(json_string)
#
# print(f"File tree saved at {file_path}")
