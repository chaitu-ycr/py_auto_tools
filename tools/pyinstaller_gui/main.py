import os
import contextlib
from pathlib import Path
import PyInstaller.__main__
import nicegui
from nicegui import native, ui


class PyToExe:
    def __init__(self) -> None:
        self.app_title = 'PyToExe UI'
        self.app_description = '''converts python 🐍 script to exe 💾 
        [
        <strong>
            <span style="color:blue">.py</span>
            <span style="color:green">➡</span>
            <span style="color:red">.exe</span>
        </strong>
        ]
        '''
        ui.html(self.app_description)
        self.python_script_to_convert = ui.input(label="enter python script", placeholder='python script absolute path').style('width: 100%')
        self.app_name = ui.input(label="name of your app. (default: my_application)", value='my_application').style('width: 50%')
        ui.label('Create a one-folder bundle containing an executable or one-file bundled executable')
        self.one_folder_or_one_file = ui.radio(['--onedir', '--onefile'], value='--onefile').props('inline')
        self.clean = ui.checkbox('Clean PyInstaller cache and remove temporary files before building', value=True)
        self.windowed = ui.checkbox('prevent console appearing, only use with ui.run(native=True, ...)', value=True)
        self.start_packaging = ui.button('START PACKAGING', on_click=lambda: self.start_bundling())

    async def start_bundling(self):
        py_installer_command = list()
        if os.path.isfile(self.python_script_to_convert.value):
            py_installer_command.append(self.python_script_to_convert.value)
        else:
            return False
        py_installer_command.append(f'--name={self.app_name.value}')
        py_installer_command.append(self.one_folder_or_one_file.value)
        if self.clean.value:
            py_installer_command.append('--clean')
        if self.windowed.value:
            py_installer_command.append('--windowed')
        py_installer_command.append(f'--add-data={Path(nicegui.__file__).parent}{os.pathsep}nicegui')
        PyInstaller.__main__.run(py_installer_command)
        return True
    
    def run_app(self):
        ui.run(title=self.app_title, reload=False, port=native.find_open_port(), dark=True)

# TODO: add logic to run py installer in backend.
pytoexe_inst = PyToExe()
pytoexe_inst.run_app()