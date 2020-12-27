class Settings():
    
    def __init__(self):
        self.repository="inmemory"
        self.students=""
        self.assignments=""
        self.grades=""
    
    def set_database(self):
        if(self.repository=="textfiles"):
            self._list_of_students="_list_of_students.txt"
            self.assignments="assignments.txt"
            self.grades="grades.txt"
        elif(self.repository=="binaryfiles"):
            self._list_of_students="_list_of_students.pickle"
            self.assignments="assignments.pickle"
            self.grades="grades.pickle"
    def get_database(self):
        return self.repository