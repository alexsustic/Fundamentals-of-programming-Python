import copy
class Assignment:
    def __init__(self,assignmentID,description,deadline):
        self.__assignmentID=assignmentID
        self.__description=description
        self.__deadline=deadline

    def get_assignment_id(self):
        return self.__assignmentID


    def get_description(self):
        return self.__description


    def get_deadline(self):
        return self.__deadline


    def set_description(self, value):
        self.__description = value


    def set_deadline(self, value):
        self.__deadline = value

    
    def display_assignment(self):
        print("AssignmentID:" + " "+str(self.__assignmentID)+" "+ " "+"Description:"+ " "+str(self.__description)+ " "+ " "+"Deadline:" + " "+str(self.__deadline))
    
    @staticmethod
    def read_assignment(line):
        parts=line.split(",")
        return Assignment(int(parts[0].strip()),parts[1].strip(),parts[2].strip())
    @staticmethod
    def write_assignment(assignment):
        return str(assignment.__assignmentID)+","+ str(assignment.__description) +","+str(assignment.__deadline)
    
class Grade():
    def __init__(self,studentID,assignmentID,grade):
        self.__assignmentID=assignmentID
        self.__studentID=studentID
        self.__grade=grade

    def get_assignment_id(self):
        return self.__assignmentID


    def get_student_id(self):
        return self.__studentID


    def get_grade(self):
        return self.__grade


    def set_grade(self, value):
        self.__grade = value


    def display_grade(self):
        print("AssignmentID:" + " "+str(self.__assignmentID)+" "+ " "+"StudentID:"+ " "+str(self.__studentID)+ " "+ " "+"Grade:" + " "+str(self.__grade))       
 
    @staticmethod
    def read_grade(line):
        parts=line.split()
        return Grade(int(parts[0].strip()), int(parts[1].strip()), int(parts[2].strip()) )  
    @staticmethod
    def write_grade(grade):
        return str(grade.__assignmentID)+" "+str(grade.__studentID)+" "+str(grade.__grade)


class Student(object):
    def __init__(self,studentID,name,group):
        self.__studentID=studentID
        self.__name=name
        self.__group=group

    def get_student_id(self):
        return self.__studentID


    def get_name(self):
        return self.__name


    def get_group(self):
        return self.__group


    def set_name(self, value):
        self.__name = value


    def set_group(self, value):
        self.__group = value

  
    def display_student(self):
        print("studentID:" + " "+str(self.__studentID)+" "+ " "+"Name:"+ " "+str(self.__name)+ " "+ " "+"Group:" + " "+str(self.__group))     
        
    @staticmethod
    def read_student(line):
        parts=line.split()
        return Student(int(parts[0].strip()),str(parts[1].strip()),int(parts[2].strip()))   
    
    @staticmethod
    def write_student(student):
        return str(student.__studentID)+" "+ str(student.__name)+" " +str(student.__group)
class Undo():
    def __init__(self,operation, extraParameters,position):
        self.__operation=operation
        self.__extraParameters=extraParameters
        self.__position=position
        
    def get_operation(self):
        return self.__operation
    
    def set_operation(self,newOperation):
        self.__operation=newOperation
        
    def get_parameters(self):
        return self.__extraParameters[:]
    
    def get_position(self):
        return self.__position
    
    def get_parameters_object(self):
        return copy.deepcopy(self.__extraParameters)
        
