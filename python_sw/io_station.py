# -*- coding:utf-8 -*-
import os
import sys
import subprocess

import shotgun_api3

# import PySide2
# import ffmpeg
# import openpyxl

SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
SCRIPT_NAME = "pipeline_sw"
SCRIPT_KEY = "gvvsnbqrnckmmf3zhw?tqbDib"

sg = shotgun_api3.Shotgun(SERVER_PATH,
                          script_name=SCRIPT_NAME, api_key=SCRIPT_KEY)


defult_config_path = '/home/west/ww/RND/configs/project_tank-1/tank setup_project --force'

# os.system('/home/west/ww/RND/configs/project_tank-1/tank')
subprocess.call(defult_config_path, shell=True)


def create_project():
    user_project_name = input("project name : ")
    print(type(user_project_name))

    project_data = {"name": user_project_name,
                    "tank_name": "sw_project_test_2",
                    "sg_description": "This is a new SungWoo project.",
                    "sg_status": "Active"
                    }
    project = sg.create("Project", project_data)
    print("Created project: {}".format(project))
    # return project

# create_project()
