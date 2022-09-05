import dearpygui.dearpygui as dpg

class MyMineDrawings:
    def __init__(self):
        self.drawingData = dict()
        self.firstDataKey = 0
        self.pointList = []

    def start_drawing_a_new_line(self):
       with dpg.draw_polyline():
            pass


    def draw_point(sender, app_data, user_data):
        user_data.append(dpg.get_mouse_pos())
        dpg.draw_polyline(user_data, color=(255,255,255), thickness=1, parent='Canvas')

# def test(sender, app_data):
#     print(sender, app_data)
   
modeOn = True
def draw_polyline(modeOn):
    points = []
    with dpg.handler_registry():
        if modeOn:
            dpg.add_mouse_click_handler(callback=draw_point, user_data=points, button=0)
            dpg.add_key_press_handler(key=27)

    
