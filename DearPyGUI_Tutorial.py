
from fnmatch import translate
import dearpygui.dearpygui as dpg
from SurPy import*    
import math

dh = DataHandler()
testList = dh.read_str_file('external data\\teststrings.str')

dh.get_line_coordinates()
dh.print_all_string_coordinates()

string1 = dh.get_2d_coords_for_single_sting(1)
string2 = dh.get_2d_coords_for_single_sting(2)
string3 = dh.get_2d_coords_for_single_sting(3)
string4 = dh.get_2d_coords_for_single_sting(4)

dpg.create_context()

def toggle_layer2(sender):
    show_value = dpg.get_value(sender)
    dpg.configure_item("layer1", show=show_value)

with dpg.window(tag = 'mainWindow', label="Tutorial"):
    dpg.add_checkbox(label="show layer", callback=toggle_layer2, default_value=True)

    with dpg.drawlist(width=800, height=900):

        with dpg.draw_layer(tag="layer1"):
            with dpg.draw_node(tag="root node"):
                DataHandler.drawing_depending_on_string_type(string1, color=(255,255,255), thickness=1)
                DataHandler.drawing_depending_on_string_type(string2, color=(180,65,65), thickness=1)
                DataHandler.drawing_depending_on_string_type(string3, color=(122,222,111), thickness=1)
                DataHandler.drawing_depending_on_string_type(string4, color=(100,100,200), thickness=2)


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
    transCoords[0] += app_data[1]/10
    transCoords[1] += app_data[2]/10

def restore_screen_view():
    global transCoords, axe_scale
    axe_scale = 1
    transCoords = [0, 0]

with dpg.handler_registry():
    dpg.add_mouse_wheel_handler(callback=zoom)
    dpg.add_mouse_drag_handler(callback=move)
    dpg.add_mouse_double_click_handler(button=2, callback=restore_screen_view)


scale = dpg.create_scale_matrix([axe_scale, axe_scale, axe_scale])
rotation = dpg.create_rotation_matrix(math.pi/2, [0, 0, -1])
translation = dpg.create_translation_matrix(transCoords)
dpg.apply_transform("root node", scale * translation * rotation)


dpg.create_viewport(title='Custom Title', width=800, height=900,x_pos=50, y_pos=50)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("mainWindow", True)

while dpg.is_dearpygui_running():
    scale = dpg.create_scale_matrix([axe_scale, axe_scale, axe_scale])
    translation = dpg.create_translation_matrix(transCoords)
    dpg.apply_transform("root node", scale * translation)
    dpg.render_dearpygui_frame()
    


dpg.destroy_context()