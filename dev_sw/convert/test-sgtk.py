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


def get_active_project():
    projects = sg.find("Project", [["sg_status", "is", "Active"]], ["name"])
    project_dict = sorted(list(set([project["name"] for project in projects])))
    print(project_dict)


project_name = "seine"

user_project = sg.find("Project", [["name", "is", project_name]], [])

print(user_project)
# for dict in user_project:
#     user_project.extend(dict)
#     print(user_project[0])


filters = [["project", "is", user_project]]

fields = ["id", "code"]
shot_list = sg.find("Shot", filters, fields)

print(shot_list)

print(user_project[0]['id'])

# import sgtk
#
# # 프로젝트 설정 파일 경로
# config_path = '/path/to/your/shotgun.yml'
#
# # 프로젝트 생성
# sg = sgtk.Shotgun.from_config_location(config_path)
#
# # ShotGrid 폴더 생성
# folder = sg.create('Folder', {'name': '새로운 폴더 이름', 'project': {'type': 'Project', 'id': 프로젝트_ID}})