import os

def create_str(inside,   root='my_project'):
  dir_path = os.path.join(root, inside)
  if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    pass


structure =['settings','mainapp', 'adminapp', 'authapp' ]

for inside in structure:
 create_str(inside)