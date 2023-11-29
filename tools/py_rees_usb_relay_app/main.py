from nicegui import native, ui

ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))

ui.run(title='py_rees_usb_relay_app', native=True, reload=False, port=native.find_open_port())
