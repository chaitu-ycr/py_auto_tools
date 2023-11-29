import os
import win32gui
from nicegui import native, ui


def select_single_file(dir_path=''):
    init_dir = dir_path if dir_path != '' else os.getcwd()
    file_list = win32gui.GetOpenFileNameW(InitialDir=init_dir,
                                            Title='Select py file',
                                            Filter="Python Files\0*.py;",
                                            FilterIndex=0)
    return file_list[0]


async def select_file():
    selected_file = select_single_file()
    ui.notify(f'File selected: {selected_file}')

ui.button('Select file', on_click=select_file)

ui.run(title='py_uml_gen_app', native=True, reload=False, port=native.find_open_port())
