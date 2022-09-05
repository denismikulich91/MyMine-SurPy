from msilib import add_data
import dearpygui.dearpygui as dpg
from SurPy import*    
import math
import MyMineFunctions as mf

dh = DataHandler()
testList = dh.read_str_file('external data\\teststrings.str')

dh.get_line_coordinates()
dh.print_all_string_coordinates()



string1 = dh.get_2d_coords_for_single_sting(1)
string2 = dh.get_2d_coords_for_single_sting(2)
string3 = dh.get_2d_coords_for_single_sting(3)
string4 = dh.get_2d_coords_for_single_sting(4)

axe_scale = 1
def zoom(sender, app_data):
    global axe_scale
    if app_data == -1:
        axe_scale += 0.1
    else:
        axe_scale -= 0.1

transCoords = [0, 0]
def move(sender, app_data):
    global transCoords
    if app_data[0] == 2:
        transCoords[0] += app_data[1]/10
        transCoords[1] += app_data[2]/10

def restore_screen_view():
    global transCoords, axe_scale
    axe_scale = 1
    transCoords = [0, 0]


color = [255, 255, 255]
def choose_color(sender, app_data):
    global color
    color = [int(i*255) for i in app_data[:-1]]
    

def new_line():
    newLine = mf.MyMineDrawings(color)
    newLine.draw_polyline()


dpg.create_context()
dpg.configure_app(docking=True)

def toggle_layer2(sender):
    show_value = dpg.get_value(sender)
    dpg.configure_item("Canvas", show=show_value)

with dpg.window(tag = 'mainWindow', label="Tutorial", no_scrollbar=True):

    

    with dpg.drawlist(width=900, height=800):

        with dpg.draw_layer(tag="Canvas"):
            with dpg.draw_node(tag="root node"):
                DataHandler.drawing_depending_on_string_type(string1, color=(255,255,255), thickness=1)
                DataHandler.drawing_depending_on_string_type(string2, color=(180,65,65), thickness=1)
                DataHandler.drawing_depending_on_string_type(string3, color=(122,222,111), thickness=1)
                DataHandler.drawing_depending_on_string_type(string4, color=(100,100,200), thickness=2)

with dpg.window(tag = 'toolWindow', label="Tools", pos=[920, 0], min_size=[80,50]):
    dpg.add_button(label='Zoom All', width=70, callback=restore_screen_view)
    dpg.add_button(label='Draw Line', width=70, callback=new_line)
    dpg.add_button(label='New segment', width=70)
    dpg.add_button(label='Button4', width=70)
    dpg.add_checkbox(label="Visible", callback=toggle_layer2, default_value=True)
    dpg.add_color_picker(callback=choose_color, default_value=(255, 255, 255))


with dpg.handler_registry():
    dpg.add_mouse_wheel_handler(callback=zoom)
    dpg.add_mouse_drag_handler(callback=move)
    dpg.add_mouse_double_click_handler(button=2, callback=restore_screen_view)


scale = dpg.create_scale_matrix([axe_scale, axe_scale, axe_scale])
rotation = dpg.create_rotation_matrix(math.pi/2, [0, 0, -1])
translation = dpg.create_translation_matrix(transCoords)
dpg.apply_transform("root node", scale * translation * rotation)


dpg.create_viewport(title='Custom Title', width=1030, height=800,x_pos=20, y_pos=20)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("mainWindow", False)

while dpg.is_dearpygui_running():
    scale = dpg.create_scale_matrix([axe_scale, axe_scale, axe_scale])
    translation = dpg.create_translation_matrix(transCoords)
    dpg.apply_transform("root node", scale * translation)
    dpg.render_dearpygui_frame()
    


dpg.destroy_context()