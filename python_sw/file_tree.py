
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

usr_project_name = "SW_Project_test_4"


def create_project():

    project_data = {"name": usr_project_name, "sg_status": "Active", "sg_description": "This is a new project."}

    project = sg.create("Project", project_data)
    print("Created project: {}".format(project))

    """ if project already exist error """


def get_active_project():
    """
    active 된 프로젝트 목록을 get 하는 함수이다.
    """
    projects = sg.find("Project", [["sg_status", "is", "Active"]], ["name"])
    # pprint(projects)
    for project in projects:
        # print(project["name"])
        # return(project["name"])
        return sorted(list(set([project["name"] for project in projects])))


def set_file_tree():
    print("set file tree")


# set_file_tree()
a = get_active_project()
print(a)

if usr_project_name not in a:
    create_project()
else:
    print("{} : Project already exist".format(usr_project_name))

