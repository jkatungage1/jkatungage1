import os

os.system('cls')
destination_folder = r"c:\users\mukendi\onedrive - nokia\python-course\automatic update of the l2rt config\git\deplo"
destination_folder = os.path.normpath(destination_folder)
repo_name = "jkatungage1"

command = os.system(f'RMDIR /S "{destination_folder}\\{repo_name}"')

