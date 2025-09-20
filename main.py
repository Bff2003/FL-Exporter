import os
import subprocess
from subprocess import PIPE
import traceback
from pathlib import Path
import logging
import shutil

class Exporter:
    def __init__(self, executable_fl64_path, projects_path = None):
        self.executable = executable_fl64_path
        self.projects_path = projects_path

    def discover_projects(self, path, file_extension = ".flp", name_folders_to_ignore = ["Backup"]):
        found_files = []
        to_return = []
        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(file_extension):
                        full_path = os.path.join(root, file)
                        found_files.append(full_path)
            
            to_add = True
            for found_file in found_files:
                to_add = True
                for folder_to_ignore in name_folders_to_ignore:
                    if folder_to_ignore in found_file:
                        to_add = False
                        break

                    if to_add:
                        to_return.append(found_file)

            return to_return
        except Exception as e:
            print(f"Erro ao procurar arquivos: {e}")
            return []

    def export_project(self, project_flp_file):
        project_name = os.path.splitext(os.path.basename(project_flp_file))[0]
        print(f"Exporting project: {project_name}")

        # Construct the full path to the .flp file
        project_path = project_flp_file

        # Check if the project file exists
        if not os.path.exists(project_path):
            print(f"Error: Project file does not exist: {project_path}")
            return

        # Construct the command
        command = [self.executable, f'/Z"{project_path}"']

        result = subprocess.run(
            self.executable + " " + command[1], 
            shell=True, 
            stdout=PIPE, 
            stderr=PIPE
        )

        if result.returncode != 0:
            raise Exception(f"Error exporting project: {project_name}", stdout=result.stdout, stderr=result.stderr, returncode=result.returncode)

        exported_file = project_path.replace(".flp", ".zip")
        print(f"Exported file: {exported_file}")
        return exported_file


    def main(self, folder_to_save_projects, discover_projects = None):
        if discover_projects != None:
            projects = self.discover_projects(discover_projects)
            print(projects)

        for project in projects:
            logging.info(f"Exporting project: {project}")
            project_exported = self.export_project(project)
            logging.debug(f"Exported file: {project_exported}")

            # Move the exported file to the folder
            if project_exported:
                logging.debug(f"Moving file to: {folder_to_save_projects}")
                shutil.move(project_exported, folder_to_save_projects)
                logging.debug(f"File moved to: {folder_to_save_projects}")
            

if __name__ == "__main__":
    executable = r'c:\PROGRA~1\Image-Line\"FL Studio 21"\fl64.exe'
    path_to_exported_projects = r"%UserProfile%\Documents\fl_exporter"
    default_projects_path = r"%UserProfile%\Documents\Image-Line\FL Studio\Projects"

    exporter = Exporter(executable)

    os.makedirs(path_to_exported_projects, exist_ok=True)

    exporter.main(
        folder_to_save_projects=path_to_exported_projects, 
        discover_projects=default_projects_path
    )
