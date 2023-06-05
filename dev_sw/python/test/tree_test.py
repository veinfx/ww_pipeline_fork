# -*- coding:utf-8 -*-
import os
import sys

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

user_project_name = "project_tank-2"
user_seq_name = f"{user_project_name}_S010"
user_shot_name = f"{user_seq_name}_0010"

project_data = {"name": user_project_name, "sg_description": "This is a new project. tank_name test",
                "sg_status": "Active", "tank_name" : "sw_project_test_2"}


project_path = f"/show/{user_project_name}"
# os.mkdir(project_path)

defult_dir_list = ['asset', 'seq', 'production/scan', 'production/excel', 'temp']


def make_dirs():
    for item in defult_dir_list:
        print(project_path + "/" + item)
        if os.path.exists(item):
            print("dir_path exists", item)
            pass
        else:
            os.makedirs(project_path + "/" + item)
            print("created dir_path", item)
        pass
        # os.makedirs(project_path + "/" + item)

def create_project():
    # project_data = {"name": usr_project_name, "sg_description": "This is a new project."}
    project = sg.create("Project", project_data)
    print("Created project: {}".format(project))
    return project


def create_shot():
    project_dict = sg.find_one("Project", [["name", "is", user_project_name]], ["id"])
    print(project_dict)
    seq_data = {
        "project":project_dict,
        "code": user_seq_name
    }

    seq_dict = sg.create("Sequence", seq_data)

    shot_data = {
        "project": project_dict,
        "code": user_shot_name,
        "sg_sequence" : seq_dict
    }

    # shot_data = {"code": usr_shot_name, "sg_sequence" : usr_seq_name, "Project": ["name", "is", usr_project_name]}
    shot_dict = sg.create("Shot", shot_data)
    print(shot_dict)

def get_all_project():
    """all project"""
    projects = sg.find("Project", [], ["name"])
    for project in projects:
        return sorted(list(set([project["name"] for project in projects])))

create_project()
create_shot()
a = get_all_project()
# print(a)


# @staticmethod
def create_defult_dir(dir_path):

    if os.path.exists(dir_path):
        print("dir_path exists", dir_path)
        pass
    else:
        os.makedirs(dir_path)
        print("created dir_path", dir_path)
    pass

# create_defult_dir(dir_path)



#*------Used method
'''

""" if project already exist error """
if usr_project_name not in a:
    create_project()
    create_defult_dir()

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

'''





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
