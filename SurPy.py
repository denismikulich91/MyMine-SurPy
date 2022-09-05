import dearpygui.dearpygui as dpg

class DataHandler():
     
    def __init__(self):
        self.__points = []
        self.__allStringCoords = dict()
        
    def read_str_file(self, fileName: str)-> list:
        """ 
        This function reads .str file all at once, splitting
        into list items by comma and returns data to __points value
        """
        with open(fileName, encoding="utf-8") as strFile:
            strFileDataList = strFile.readlines()
        for line in strFileDataList:
            self.__points.append(line.split(', '))
            # TODO: Delete \n object in te end of lists

    # Getter of the all points from string file, including zeroes
    def show_points(self):
        for line in self.__points:
            print(line)
    

    def get_line_coordinates(self) -> dict:
        """Creates a dict with string number as a key
        and XYZ coords as a list of list of values (list[list[float]])""" 
        for line in self.__points[2:-1]:
            if int(line[0]) != 0:
                if int(line[0]) not in self.__allStringCoords.keys():
                    singleStringCoords = []
                    singleStringCoords.append(line[1:4])
                    self.__allStringCoords[int(line[0])] = singleStringCoords
                else:
                    singleStringCoords.append(line[1:4])
            else:
                singleStringCoords.append(line[1:4])
        return self.__allStringCoords

    
    def print_all_string_coordinates(self):
        # Getter to accurately draw all coords within all strings (clean show_points)
        for key, value in self.__allStringCoords.items():
            print(f"String #{key}")
            for i in value:
                print(i)
    
    
    def get_2d_coords_for_single_sting(self, stringNumber: int) -> list[list[float]]:
        """Returns list of lists of coordinates of the choosen string
        however strings which consists of several segments are just splitted with zeroes
        correct segment drawing must be reliased in drawing function"""
        stringCoordsList = [[float(x) for x in coords[0:2] ] 
                            for coords in self.__allStringCoords[stringNumber][:-1]]
        return stringCoordsList  # Format: [[float_x, float_y], [float_x, float_y]...]

    @staticmethod
    def drawing_depending_on_string_type(string, color, thickness):
        """Checks if string consists of several segment and for each type
        launches it's own draw_polyline DPG function"""

        if [0.0, 0.0] not in string:  # Checking if single-segment polyline
            dpg.draw_polyline(string, color=color, thickness=thickness)

        else:  # Checking if multi-segment string 
            segmentCoords = []
            for point in string:
                if point != [0.0, 0.0]:
                    segmentCoords.append(point)
                else:
                   dpg.draw_polyline(segmentCoords, color=color, thickness=thickness)
                   segmentCoords = []
            dpg.draw_polyline(segmentCoords, color=color, thickness=thickness)














