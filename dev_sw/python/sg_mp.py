# -*- coding:utf-8 -*-
import os
import sys

import fileseq
import shutil
import shotgun_api3
import PySide2
import ffmpeg
import openpyxl

SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
SCRIPT_NAME = "pipeline_sw"
SCRIPT_KEY = "gvvsnbqrnckmmf3zhw?tqbDib"

sg = shotgun_api3.Shotgun(SERVER_PATH,
                          script_name=SCRIPT_NAME, api_key=SCRIPT_KEY)


class SgMapping:
    def __init__(self):
        pass

    def get_active_project(self):
        """
        active 된 프로젝트 목록을 get 하는 함수이다.
        """
        projects = sg.find("Project", [["sg_status", "is", "Active"]], ["name"])
        project_dict = sorted(list(set([project["name"] for project in projects])))
        return project_dict

    def get_seq_list(self, usr_project):
        """
        프로젝트의 sequence를 구하는 함수이다.
        """
        project = sg.find_one("Project", [["name", "is", usr_project]], ["id"])
        project_id = project["id"] # project_name : Topgun_psw , id : 139
        filters = [["project", "is", {"type": "Project", "id": project_id}]]
        sequences = sg.find("Sequence", filters, ["code"])

    def get_seq_list(self, user_project):
        """
        프로젝트의 sequence를 구하는 함수이다.
        """
        project = sg.find_one("Project", [["name", "is", user_project]], ["id"])
        project_id = project["id"] # project_name : Topgun_psw , id : 139
        filters = [["project", "is", {"type": "Project", "id": project_id}]]
        sequences = sg.find("Sequence", filters, ["code"])

        seq_list_dict = sorted(list(set([sequence["code"] for sequence in sequences])))
        return seq_list_dict

    def get_shot_list(self,user_project, user_seq):
        """
        프로젝트의 shot을 구하는 함수이다.
        """
        project = sg.find_one("Project", [["name", "is", user_project]], ["id"])
        project_id = project["id"]

        sequence = sg.find_one("Sequence", [["project", "is", project],
                                            ["code", "is", user_seq]], ["id"])
        # print(4,sequence)
        if sequence is None:  # sequence가 None인 경우
            # print("Sequence not found")
            return []  # 빈 리스트 반환 또는 예외 처리

        sequence_id = sequence["id"]
        # print(5,sequence_id)
        filters = [["project", "is", {"type": "Project", "id": project_id}],
                   ["sg_sequence", "is", {"type": "Sequence", "id": sequence_id}]]

        shots = sg.find("Shot", filters, ["code"])
        # pprint(shots)

        shot_list_dict = sorted(list(set([shots["code"] for shots in shots])))
        return shot_list_dict