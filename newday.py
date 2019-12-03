import os.path
import os
import shutil
from git import Repo
from git import Actor

dirtemplate = './foldertemplate'

day = int(input("Which day?: "))
part = int(input("Which part?: "))

path_to_create = f"./day{day}/part{part}"
shutil.copytree(dirtemplate, path_to_create)
