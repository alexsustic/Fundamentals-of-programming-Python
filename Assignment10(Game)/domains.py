class X():
    def __init__(self,line_position,column_position,representation):
        self.__line_position = line_position
        self.__column_position = column_position
        self.__representation = representation

    def get_line_position(self):
        return self.__line_position


    def get_column_position(self):
        return self.__column_position


    def get_representation(self):
        return self.__representation


    def set_line_position(self, value):
        self.__line_position = value


    def set_column_position(self, value):
        self.__column_position = value


    def set_representation(self, value):
        self.__representation = value
        
    def __str__(self):
        return self.get_representation()
        
class O():
    def __init__(self,line_position,column_position,representation):
        self.__line_position = line_position
        self.__column_position = column_position
        self.__representation = representation

    def get_line_position(self):
        return self.__line_position


    def get_column_position(self):
        return self.__column_position


    def get_representation(self):
        return self.__representation


    def set_line_position(self, value):
        self.__line_position = value


    def set_column_position(self, value):
        self.__column_position = value


    def set_representation(self, value):
        self.__representation = value

    def __str__(self):
        return self.get_representation()    



