# :coding: utf-8

from dev_sw.python.ui.sg_mapping import SgMapping

project = 'seine'
sg = SgMapping()

projects = sg.get_active_project()
print(projects)


def scan_copy_org(select_project):
    seqs = sg.get_seq_list(select_project)
    return seqs

seqs = scan_copy_org(project)

print(seqs)






