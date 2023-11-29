import os
import subprocess
from pathlib import Path
import nicegui

python_exe_abs_path = r'D:\git_repos\py_auto_tools\.venv\Scripts\python.exe'
main_file_abs_path = r'D:\git_repos\py_auto_tools\tools\py_tenma_ps_app\main.py'
app_name = 'py_tenma_ps_app'

cmd = [
    python_exe_abs_path,
    '-m', 'PyInstaller',
    main_file_abs_path, # your main file with ui.run()
    '--name', app_name, # name of your app
    '--onefile',
    '--clean',
    '--windowed', # prevent console appearing, only use with ui.run(native=True, ...)
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'
]

subprocess.call(cmd)
