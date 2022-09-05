import dearpygui.dearpygui as dpg
LAYERS = []
class MyMineDrawings:
    def __init__(self, color):
        self.drawingData = dict()
        self.DataKey = 0
        self.pointList = []
        self.drawingMode = True
        self.color = color


    def draw_point(self, sender, app_data):
        if self.drawingMode:
            self.pointList.append(dpg.get_mouse_pos())
            dpg.draw_polyline(self.pointList, color=self.color, thickness=1, parent='Canvas')


    def test(self, sender, app_data):
        print('Key number:', app_data)
    

    def draw_polyline(self):
        with dpg.handler_registry():
            dpg.add_mouse_click_handler(callback=self.draw_point, button=0)
            # dpg.add_key_press_handler(callback=self.test)
            dpg.add_key_press_handler(key=27, callback=self.cancel_drawing)
            dpg.add_key_press_handler(key=78, callback=self.start_new_segment)
    

    def cancel_drawing(self):
        self.drawingMode = False
        self.drawingData[self.DataKey] = self.pointList
        self.pointList = []
        LAYERS.append(self.drawingData)
        self.drawingData = {}


    def start_new_segment(self):
        self.drawingData[self.DataKey] = self.pointList
        self.pointList = []
        self.DataKey += 1



    
