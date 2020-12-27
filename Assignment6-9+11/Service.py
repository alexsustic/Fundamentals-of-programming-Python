from Domains.Domain import Student,Assignment,Grade,Undo
from Validators.Validator import ValidateStudent, ValidateAssignment, ValidateGrade
from Repository.Repository import RepoStudent
class StudentService(object):
    def __init__(self,repoStudent,repoUndo):
        self.__repoStudent=repoStudent
        self.__repoUndo=repoUndo
    def getAllStudents(self):
        return self.__repoStudent.getStudents()
    def addNewStudent(self,studentID,name,group):
        student=Student(studentID, name, group)
        ValidateStudent.validateStudentID(self,student)
        ValidateStudent.validateStudentGroup(self,student)
        self.__repoStudent.addNewStudentToRepository(student)
    def getStudents(self):
        allstudents=self.__repoStudent.getStudents()
        return allstudents
    def displayListOfStudents(self):
        allStudents=self.__repoStudent.getStudents()
        return allStudents
    
    def removeAStudent(self,studentID):
        self.__repoStudent.removeAStudentFromRepository(studentID)
    
    def updateTheStudentName(self,studentID,name):
        if studentID<0:
            raise Exception("Invalid studentID!")
        else:
            self.__repoStudent.updateTheStudentNameFromRepository(studentID,name)
            
    def updateTheStudentGroup(self,studentID,group):
        if studentID<0:
            raise Exception("Invalid studentID!")
        elif group<0:
            raise Exception("Invalid group!")
        else:
            self.__repoStudent.updateTheStudentGroupFromRepository(studentID,group)
        
class AssignmentService:
    def __init__(self,repoAssignment,repoUndo):
        self.__repoAssignment=repoAssignment
        self.__repoUndo=repoUndo
    def addNewAssignment(self,assignmentID,description,deadline):
        assignment=Assignment(assignmentID,description,deadline)
        ValidateAssignment.validateAssignmentID(self,assignment)
        ValidateAssignment.validateAssignmentDeadline(self,assignment)
        self.__repoAssignment.addNewAssignmentToRepository(assignment)
    def displayListofAssignments(self):
        allAssignments=self.__repoAssignment.getAssignments()
        return allAssignments
            
    def updateTheAssignmentDescription(self,assignmentID,description):
        if(assignmentID<0):
            raise Exception("Invalid assignmentID!")
        else:
            self.__repoAssignment.updateTheAssignmentDescriptionFromRepository(assignmentID,description)
            
    def updateTheAssignmentDeadline(self,assignmentID,deadline):
        assignment=Assignment(assignmentID," ",deadline)
        try:
            ValidateAssignment.validateAssignmentID(self,assignment)
            ValidateAssignment.validateAssignmentDeadline(self,assignment)
            self.__repoAssignment.updateTheAssignmentDeadlineFromRepository(assignmentID,deadline)
        except Exception as ex:
            raise Exception(ex)
        
    def removeAnAssignment(self,assignmentID):
        self.__repoAssignment.removeAnAssignmentFromRepository(assignmentID)
        
        
    def getLateAssignments(self,deadline):
        try:
            assignment=Assignment(0," ",deadline)
            ValidateAssignment.validateAssignmentDeadline(self, assignment)
            lateAssignments=self.__repoAssignment.getLateAssignmentsFromRepository(deadline)
            return lateAssignments
        except Exception as ex:
            raise Exception(ex)
        
    def getAssignments(self):
        return self.__repoAssignment.getAssignments()   
        
class GradeService:
    def __init__(self,repoGrade,repoUndo):
        self.__repoGrade=repoGrade
        self.__repoUndo=repoUndo
    def giveAssignmentToAStudent(self,studentID,assignmentID):
            grade=Grade(studentID, assignmentID ,0)
            try: 
                ValidateGrade.validateStudentID(self,grade)
                ValidateGrade.validateAssignmentID(self,grade)
                self.__repoGrade.giveAssignmentToAStudentFromRepository(grade)
            except Exception as ex:
                raise Exception(ex)  
    def removeAStudent(self,studentID):
            self.__repoGrade.removeAStudentFromGradesList(studentID)
            self.__repoGrade.removeAStudentFromGradedAssignmentsList(studentID)
    def removeAnAssignment(self,assignmentID):
            self.__repoGrade.removeAnAssignmentFromGradesList(assignmentID)
            self.__repoGrade.removeAnAssignmentFromGradedAssignmentsList(assignmentID)           
    def giveAssignmentToAGroup(self,group,assignmentID):
            repoStudent=RepoStudent()
            allStudents=repoStudent.getStudents()
            existence_of_group=False
            for student in allStudents:
                if student.get_group()==group:
                    grade=Grade(student.get_student_id(),assignmentID,0)
                    try:
                        ValidateGrade.validateAssignmentID(self,grade)
                        self.__repoGrade.giveAssignmentToAStudentFromRepository(grade)
                    except Exception as ex:
                        raise Exception(ex)
                    existence_of_group=True
            if(existence_of_group==False):
                raise Exception("Nonexistent group!")
            
    def studentsOrderedByAverageGradeOfAssignment(self,assignmentID):
        grades=self.__repoGrade.studentsOrderedByAverageGradeOfAssignmentFromRepository(assignmentID)
        return grades
    
    def studentsWithBestSchoolSituation(self,allStudents):
        statisticStudentsListOfGrades=self.__repoGrade.statisticStudentsListOfGrades(allStudents)
        topStudentsID=self.__repoGrade.studentsWithBestSchoolSituationFromRepository(statisticStudentsListOfGrades)
        return topStudentsID
    
    def gradeStudent(self,studentID,assignmentID,grade):
        validationGrade=Grade(studentID, assignmentID ,grade)
        try: 
            ValidateGrade.validateStudentID(self,validationGrade)
            ValidateGrade.validateAssignmentID(self,validationGrade)
            self.__repoGrade.gradeStudentFromRepository(validationGrade)
        except Exception as ex:
            raise Exception(ex)  
            
    def getLateUngradedAssignments(self,allLateAssignmentsID):
        allLateUngradedStudentsID=self.__repoGrade.getLateUngradedAssignmentsFromRepository(allLateAssignmentsID)
        return allLateUngradedStudentsID
    def displayListOfGradedAssignments(self):
        allGrades=self.__repoGrade.get_initialised_grades()
        return allGrades
    def displayListOfGrades(self):
        allGrades=self.__repoGrade.get_grades()
        return allGrades
    
class UndoService():
    def __init__(self,undoRepo):
        self.__undoRepo=undoRepo
    def performUndo(self):
        self.__undoRepo.performUndoFromRepository()
    def performRedo(self):
        self.__undoRepo.performRedoFromRepository()
    def addNewOperation(self,operation,parameters,position):
        
        if operation in ["addStudent","addStudentOnPosition"]:
            undo=Undo(operation,Student(parameters[0],parameters[1],parameters[2]),position)
            redo=Undo("removeStudent",parameters,position)
            self.__undoRepo.addNewOperation(undo,redo)
            
        elif operation in ["addAssignmentOnPosition","addAssignment"] :
            undo=Undo(operation,Assignment(parameters[0],parameters[1],parameters[2]),position)
            redo=Undo("removeAssignment",parameters,position)
            self.__undoRepo.addNewOperation(undo,redo)
         
        elif operation in ["updateStudentName","updateStudentGroup","updateAssignmentDescription","updateAssignmentDeadline"]:
            undo=Undo(operation,[parameters[0],parameters[3],parameters[2],parameters[1]],position)
            redo=Undo(operation,parameters,position)
            self.__undoRepo.addNewOperation(undo,redo)
            
        elif operation=="removeStudent":
            undo=Undo(operation,parameters,position)
            redo=Undo("addStudent",Student(parameters[0],parameters[1],parameters[2]),None)
            self.__undoRepo.addNewOperation(undo,redo)
            
        elif operation=="removeAssignment":
            undo=Undo(operation,parameters,position)
            redo=Undo("addAssignment",Assignment(parameters[0],parameters[1],parameters[2]),None)
            self.__undoRepo.addNewOperation(undo,redo)
            
        elif operation=="removeAssignmentFromStudent":
            undo=Undo(operation,parameters,position)
            redo=Undo("addGrade",Grade(parameters[1],parameters[0],0),None)
            self.__undoRepo.addNewOperation(undo,redo)
            
        elif operation=="removeAssignmentFromGroup":
            undo=Undo(operation,parameters,None)
            repoStudent=RepoStudent()
            allStudents=repoStudent.getStudents()
            list_of_grades=[]
            for student in allStudents:
                if student.get_group()==parameters[0]:
                    grade=Grade(student.get_student_id(),parameters[1],0)
                    list_of_grades.append(grade)
            redo=Undo("addAssignmentToGroup",list_of_grades,None)
            self.__undoRepo.addNewOperation(undo,redo)
            
        elif operation=="removeGrade":
            undo=Undo(operation,parameters,None)
            redo=Undo("gradeStudent",Grade(parameters[0],parameters[1],parameters[2]),None)
            self.__undoRepo.addNewOperation(undo,redo)
            
    def getOperations(self):
        operations=self.__undoRepo.getListOfOperations()
        return operations