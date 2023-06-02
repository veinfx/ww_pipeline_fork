import openpyxl
import shotgun_api3
from pprint import pprint

SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
SCRIPT_NAME = "script_wongyu"
SCRIPT_KEY = "mh3lwvof$rzkUtqndqsfqcckf"
sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)


class xlsx:
    def __init__(self):
        self.just_out = []
        self.resolution = []
        self.ext = []
        self.start_frame = []
        self.end_frame = []
        self.duration = []
        self.timecode_in = []
        self.timecode_out = []
        self.framerate = []
        self.date = []
        self.just_in = []
        self.xlsx_data = []
        self.scan_path = []
        self.type = []

    def set_file_path(self, file_path):
        self.file_path = file_path

    def data_info(self):
        workbook = openpyxl.load_workbook(self.file_path)
        worksheet = workbook.active
        header = [cell.value for cell in worksheet[1]]
        for row in worksheet.iter_rows(min_row=2, values_only=True):
            self.xlsx_data.append(dict(zip(header, row)))
        pprint(self.xlsx_data)

    def sequence_upload(self, project_name):

        project_id = [["name", "is", project_name]]
        project = sg.find_one("Project", project_id)

        existing_sequence_codes = set()

        # Get the existing sequence codes from Shotgun
        existing_sequences = sg.find('Sequence', [['project', 'is', {'type': 'Project', 'id': project['id']}]], ['code'])
        for sequence in existing_sequences:
            existing_sequence_codes.add(sequence['code'])

        for data in self.xlsx_data:
            sequence_code = data['seq_name']

            if sequence_code not in existing_sequence_codes:
                sequence_data = {
                    'code': sequence_code,
                    'project': {'type': 'Project', 'id': project['id']}  # Replace with the actual project ID
                }
                sg.create('Sequence', sequence_data)
                existing_sequence_codes.add(sequence_code)
            else:
                print(f"Sequence '{sequence_code}' already exists. Skipping creation.")

    def shot_upload(self, project_name, shot_entity=None):

        project_id = [["name", "is", project_name]]
        project = sg.find_one("Project", project_id)

        existing_shot_codes = set()

        # Get the existing shot codes from Shotgun
        existing_shots = sg.find('Shot', [['project', 'is', {'type': 'Project', 'id': project['id']}]], ['code'])
        for shot in existing_shots:
            existing_shot_codes.add(shot['code'])

        for data in self.xlsx_data:
            sequence_code = data['seq_name']
            shot_code = data['shot_name']
            self.scan_path = data['scan_path']
            self.type = data['type']
            self.just_in = str(data['just_in'])
            self.just_out = str(data['just_out'])
            self.resolution = str(data['resolution'])
            self.ext = data['ext']
            self.start_frame = str(data['start_frame'])
            self.end_frame = str(data['end_frame'])
            self.duration = str(data['duration'])
            self.timecode_in = str(data['timecode_in'])
            self.timecode_out = str(data['timecode_out'])
            self.framerate = str(data['framerate'])
            self.date = str(data['date'])

            if shot_code not in existing_shot_codes:
                sequence_filters = [['code', 'is', sequence_code]]
                sequence_entity = sg.find_one('Sequence', sequence_filters)
                task_template_filters = [['code', 'is', 'test_chun']]
                task_template = sg.find_one('TaskTemplate', task_template_filters)

                shot_data = {
                    'code': shot_code,
                    'sg_sequence': sequence_entity,
                    'sg_scan_path': self.scan_path,
                    'sg_just_in': self.just_in,
                    'sg_just_out': self.just_out,
                    'sg_shot_type': self.type,
                    'sg_resolution': self.resolution,
                    'sg_ext': self.ext,
                    'sg_start_frame': self.start_frame,
                    'sg_end_frame': self.end_frame,
                    'sg_duration': self.duration,
                    'sg_timecode_in': self.timecode_in,
                    'sg_timecode_out': self.timecode_out,
                    'sg_framerate': self.framerate,
                    'sg_date': self.date,
                    'task_template': task_template,

                    'project': {'type': 'Project', 'id': project['id']}  # Replace with the actual project ID
                }
                sg.create('Shot', shot_data)
                existing_shot_codes.add(shot_code)
            else:
                print(f"Shot '{shot_code}' already exists. Skipping creation.")
        if shot_entity is None:
            shot_entity = sg.create('Shot', shot_data)
        else:
            # Update the shot entity data
            sg.update('Shot', shot_entity['id'], shot_data)

        # task_template_filters =[['code', 'is', 'test_chun']]
        # task_template = sg.find_one('TaskTemplate', task_template_filters)
        #
        # task_data = {
        #     'content': 'test_chun',
        #     'task_template': task_template,
        #     'entity': shot_entity,
        #     'project': project,
        #     'step.Step.short_name': 'Comp'
        # }
        #
        # sg.create('Task', task_data)


    def project_info(self):
        self.project_id = []
        self.project_name = []
        project_filters = [["sg_status", "is", "Active"]]
        self.projects = sg.find("Project", project_filters, fields=['id', 'name'])
        sorted_projects = sorted(self.projects, key=lambda p: p['name'])  # ABC 순서로 정렬
        project_names = [project['name'] for project in sorted_projects]
        for project in self.projects:
            # print(project['name'])
            self.project_id.append(project['id'])
            self.project_name.append(project['name'])
        # print(self.project_id)
        return self.project_name, project_names


if __name__ == '__main__':
    xx = xlsx()
    xx.data_info()
    xx.sequence_upload()
    xx.shot_upload()