# -*- coding:utf-8 -*-

import shotgun_api3
import PySide2
import ffmpeg
import openpyxl

SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
SCRIPT_NAME = "pipeline_sw"
SCRIPT_KEY = "gvvsnbqrnckmmf3zhw?tqbDib"

sg = shotgun_api3.Shotgun(SERVER_PATH,
                          script_name=SCRIPT_NAME, api_key=SCRIPT_KEY)

# project_data = {"name": "New Project", "sg_description": "This is a new project."}
#
# project = sg.create("Project", project_data)

usr_project_name = "SW_Project_test_3"
project_data = {"name": usr_project_name, "sg_description": "This is a new project."}
usr_shot_name = "SH003"

def create_project():
    # project_data = {"name": usr_project_name, "sg_description": "This is a new project."}
    project = sg.create("Project", project_data)
    print("Created project: {}".format(project))
    return project


def create_shot():
    shot_data = {"code": "test", "Project": ["name", "is", usr_project_name]}
    shot = sg.create("Asset", shot_data)
    print(shot)


def get_all_project():
    """all project"""
    projects = sg.find("Project", [], ["name"])
    for project in projects:
        return sorted(list(set([project["name"] for project in projects])))


a = get_all_project()
print(a)

""" if project already exist error """
if usr_project_name not in a:
    create_project()

else:
    print("{} : Project already exist".format(usr_project_name))


project_dict = sg.find_one("Project", [["name", "is", usr_project_name]], ["id"])
print(project_dict)
# print(tt["id"])
shot_data = {
    "project": project_dict,
    "code": usr_shot_name
}

# sg.create("Shot", shot_data)
shot_filters = [
    ['project', 'is', project_dict]
]

get_all_shot = sg.find("Shot", shot_filters, ["id", "code"])
print(get_all_shot)







# ========================================================

def get_active_project():
    """
    active 된 프로젝트 get 하는 함수이다.
    """
    projects = sg.find("Project", [["sg_status", "is", "Active"]], ["name"])
    # pprint(projects)
    for project in projects:
        # print(project["name"])
        # return(project["name"])
        return sorted(list(set([project["name"] for project in projects])))


def add_shot():
    fields = ["code", "sg_status_list"]
    filters = [['id', 'in']]
    shots = sg.find("Shot", filters, fields)


def set_file_tree():
    print("set file tree")
# set_file_tree()
