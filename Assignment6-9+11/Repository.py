import pickle
from Recipient.data_structure import DataStructure,Functions
class RepoGrade():
    def __init__(self,repoStudent,repoAssignment):
        self.__repoStudent=repoStudent
        self.__repoAssignment=repoAssignment
        self._list_of_grades=DataStructure()
        self._list_of_initialised_grades=[]
    def get_grades(self):
        list_grades=Functions.filter_list(self, self._list_of_grades, self.criteriaFunction)
        return list_grades
    
    def get_initialised_grades(self):
        return self._list_of_initialised_grades[:]
    
    def giveAssignmentToAStudentFromRepository(self,Grade):  
        existence_of_assignment=False
        for grade in self._list_of_grades:
            if(grade.get_assignment_id()==Grade.get_assignment_id() and grade.get_student_id()==Grade.get_student_id()):
                raise Exception("The student with id:"+ " "+str(Grade.get_student_id())+" "+"was already assigned!")
                existence_of_assignment=True
                break
        
        existence_of_graded_assignment=False
        for gradedAssignments in self._list_of_initialised_grades:
            if (gradedAssignments.get_assignment_id()==Grade.get_assignment_id() and gradedAssignments.get_student_id()==Grade.get_student_id()):
                raise Exception("The student with id:"+ " "+str(Grade.get_student_id())+" "+"was already graded for this assignment!")
                existence_of_graded_assignment=True
                break
        if(existence_of_assignment==False and existence_of_graded_assignment==False):
            self.addGradeToRepository(Grade)
            
                   
    def removeAssignmentFromStudent(self,assignmentID,studentID):
        grades=self.get_grades()
        index=0
        for grade in grades:
            if(grade.get_assignment_id()==assignmentID and grade.get_student_id()==studentID):
                del self._list_of_grades[index]
            index=index+1
            break     
    def addGradeToRepository(self,Grade):
        self._list_of_grades.append(Grade)
    def addGradeToGradedAssignmentsList(self,Grade):
        self._list_of_initialised_grades.append(Grade)    
    def removeAStudentFromGradedAssignmentsList(self,studentID):
        allGrades=self.get_initialised_grades()
        index=0
        for grade in allGrades:
            if grade.get_student_id()==studentID:
                del self._list_of_initialised_grades[index]
                index=index-1
            index=index+1
             
    def removeAStudentFromGradesList(self,studentID):
        allGrades=self.get_grades()
        index=0
        for grade in allGrades:
            if grade.get_student_id()==studentID:
                del self._list_of_grades[index]
                index=index-1
            index=index+1
    def removeAnAssignmentFromGradesList(self,assignmentID):
        allGrades=self.get_grades()
        index=0
        for grade in allGrades:
            if grade.get_assignment_id()==assignmentID:
                del self._list_of_grades[index]
                index=index-1
            index=index+1
     
    def removeAnAssignmentGroupFromGradesList(self,assignmentID,studentID):
        allGrades=self.get_grades()
        index=0
        for grade in allGrades:
            if grade.get_assignment_id()==assignmentID and grade.get_student_id()==studentID:
                del self._list_of_grades[index]
                index=index-1
                break
            index=index+1       
    
    def removeAnAssignmentFromGradedAssignmentsList(self,assignmentID):
        allGrades=self.get_initialised_grades()
        index=0
        for grade in allGrades:
            if grade.get_assignment_id()==assignmentID:
                del self._list_of_initialised_grades[index]
                index=index-1
            index=index+1
            
    def removeGradeFromStudent(self,studentID,assignmentID):
        allGrades=self.get_initialised_grades()
        index=0
        for grade in allGrades:
            if grade.get_student_id()==studentID and grade.get_assignment_id()==assignmentID:
                del self._list_of_initialised_grades[index]
                break
            index=index+1
    def gradeStudentFromRepository(self,Grade):
        allGrades=self.get_grades()
        allGradedAssignments=self.get_initialised_grades()
        index=0
        for grade in allGrades:
            existence=False
            if(grade.get_assignment_id()==Grade.get_assignment_id() and grade.get_student_id()==Grade.get_student_id()): 
                for gradedAssignments in allGradedAssignments:
                    if(gradedAssignments.get_assignment_id()==Grade.get_assignment_id() and gradedAssignments.get_student_id()==Grade.get_student_id()):
                        existence=True
                if existence==False:
                    self._list_of_initialised_grades.append(Grade)   
                    del self._list_of_grades[index]
                else:
                    raise Exception("This assignment was already graded!")
            index=index+1  
            
    def studentsOrderedByAverageGradeOfAssignmentFromRepository(self,assignmentID):  
        copyGradedAssignmentsList=self._list_of_initialised_grades.copy()
        allGradedAssignments=self.get_initialised_grades()
        index=0
        for grade in allGradedAssignments:
            if grade.get_assignment_id()!=assignmentID:
                del self._list_of_initialised_grades[index]
                index=index-1
            index=index+1

        #statistics=sorted(self._list_of_initialised_grades, key=lambda x:x.get_grade(), reverse=True)
        statistics=Functions.gnomeSort(self, self._list_of_initialised_grades, self.comparisonFunction)
        self._list_of_initialised_grades=copyGradedAssignmentsList.copy()
        return statistics
    
    def getLateUngradedAssignmentsFromRepository(self,allLateAssignmentsID):

        allLateStudentID=[]
        allUngradedAssignments=self.get_grades()
        for ungradedAssignment in allUngradedAssignments:
            if((ungradedAssignment.get_assignment_id() in allLateAssignmentsID) & (ungradedAssignment.get_student_id() not in allLateStudentID)):
                allLateStudentID.append(ungradedAssignment.get_student_id())
        return allLateStudentID
    

    def comparisonFunction(self, first_element, second_element):   
        if type(first_element) != type(second_element):
            raise Exception ("Invalid types operands!")

        if type(first_element) == int and type(second_element) == int:
            if first_element > second_element:
                return False
            else:
                return True
        else:
            if first_element.get_grade() > second_element.get_grade():
                return False
            else:
                return True
    
    def criteriaFunction(self,entity):
        if entity.get_grade()==0:
            return True 
        else:
            return False      
    def statisticStudentsListOfGrades(self,allStudents):
        allGradedAssignments=self.get_initialised_grades()
        statisticListOfGrades=[]
        for student in allStudents:
            gradesSum=0
            gradedAssignmentsNumber=0
            for  gradedAssignment in allGradedAssignments:
                if student.get_student_id()==gradedAssignment.get_student_id():
                    gradesSum=gradesSum+ gradedAssignment.get_grade()
                    gradedAssignmentsNumber=gradedAssignmentsNumber+1
            if gradedAssignmentsNumber!=0:
                averageScore=gradesSum/gradedAssignmentsNumber
            else:
                averageScore=0
            studentProfile=[averageScore,student.get_student_id()]
            statisticListOfGrades.append(studentProfile) 
        return statisticListOfGrades
        
        
    def studentsWithBestSchoolSituationFromRepository(self,statisticStudentsListOfGrades):
        for i in range(len(statisticStudentsListOfGrades)):
            j=i+1
            for j in range(len(statisticStudentsListOfGrades)):
                if(statisticStudentsListOfGrades[i][0]>statisticStudentsListOfGrades[j][0]):
                    auxiliary=statisticStudentsListOfGrades[i]
                    statisticStudentsListOfGrades[i]=statisticStudentsListOfGrades[j]
                    statisticStudentsListOfGrades[j]=auxiliary
        studentID_bestSchoolSituation=[]
        for i in range(len(statisticStudentsListOfGrades)):
            studentID_bestSchoolSituation.append(int(statisticStudentsListOfGrades[i][1]))
        return studentID_bestSchoolSituation
    
class RepoAssignment():
    _list_of_assignments=DataStructure()
    def __init__(self):
        pass
    
    def getAssignments(self):
        return self._list_of_assignments[:]
    
    def addNewAssignmentToRepository(self,assignment):
        allAssignments=self.getAssignments()
        for assigments in allAssignments:
            if assignment.get_assignment_id()==assigments.get_assignment_id():
                raise Exception("There is an assignment already in the system!")
        self._list_of_assignments.append(assignment)
        
    def addAssignmentOnPosition(self,assignment,position):
        allAssignments=self.getAssignments()
        for assigments in allAssignments:
            if assignment.get_assignment_id()==assigments.get_assignment_id():
                raise Exception("There is an assignment already in the system!")
        self._list_of_assignments.insert(position,assignment)
        
    def removeAnAssignmentFromRepository(self,assignmentID):
        allAssignments=self.getAssignments()
        index=0
        for assignment in allAssignments:
            if assignment.get_assignment_id()==assignmentID:
                del self._list_of_assignments[index]
                break
            index=index+1
        
    def updateTheAssignmentDescriptionFromRepository(self,assignmentID,description):
        allAssignments=self.getAssignments()
        existence_of_assignment=False
        index=0
        for assignment in allAssignments:
            if assignment.get_assignment_id()==assignmentID:
                self._list_of_assignments[index].set_description(description)
                existence_of_assignment=True
                break
            index=index+1
        if(existence_of_assignment==False):
            raise Exception("Nonexistent assignment!")
            
    def updateTheAssignmentDeadlineFromRepository(self,assignmentID,deadline):
        allAssignments=self.getAssignments()
        existence_of_assignment=False
        index=0
        for assignment in allAssignments:
            if assignment.get_assignment_id()==assignmentID:
                self._list_of_assignments[index].set_deadline(deadline)
                existence_of_assignment=True
                break
            
            index=index+1
        if(existence_of_assignment==False):
            raise Exception("Nonexistent assignment!")
    
    def getLateAssignmentsFromRepository(self,deadline):
        lateAssignments=[]
        allAsignments=self.getAssignments()
        deadline_assignments=deadline.split() 
        for assignment in allAsignments:
            assignment_deadline=assignment.get_deadline().split()
            if (int(deadline_assignments[1]) > int(assignment_deadline[1])):
                lateAssignments.append(assignment.get_assignment_id())
        return lateAssignments
    
class RepoStudent():
    _list_of_students=DataStructure()
    def __init__(self):
        pass
    
    def getStudents(self):
        return self._list_of_students[:]
    
    def addNewStudentToRepository(self,student):
        allStudents=self.getStudents()
        for Student in allStudents:
            if(student.get_student_id()==Student.get_student_id()):
                raise Exception("There is already a student in the system!")
        self._list_of_students.append(student) 
           
    def addNewStudentOnPosition(self,student,position):
        allStudents=self.getStudents()
        for students in allStudents:
            if(student.get_student_id()==students.get_student_id()):
                raise Exception("There is already a student in the system!")
        self._list_of_students.insert(position,student)
        
    def removeAStudentFromRepository(self,studentID):
        allStudents=self.getStudents()
        index=0
        for student in allStudents:
            if studentID==student.get_student_id():
                del self._list_of_students[index]
                break
            index=index+1  
            
    def updateTheStudentNameFromRepository(self,studentID,name):
        allStudents=self.getStudents()
        index=0
        existence_of_id=False
        for student in allStudents:
            if studentID==student.get_student_id():
                self._list_of_students[index].set_name(name)
                existence_of_id=True
                break
            index=index+1
        if(existence_of_id==False):
            raise Exception("Nonexistent student!")
    def updateTheStudentGroupFromRepository(self,studentID,group):
        allStudents=self.getStudents()
        index=0
        existence_of_id=False
        for student in allStudents:
            if studentID==student.get_student_id():
                self._list_of_students[index].set_group(group)
                existence_of_id=True
                break
            index=index+1
        if(existence_of_id==False):
            raise Exception("Nonexistent student!")
     
        
class RepoUndo():
    
    list_of_operations=[]
    list_of_operations_redo=[]
    index_of_operation_redo=-1
    index_of_operation=-1
    new_operation=False    
       
    def __init__(self,RepoStudent,RepoAssignment,RepoGrade):
        self.__repoStudent=RepoStudent
        self.__repoAssignment=RepoAssignment
        self.__repoGrade=RepoGrade
        
    def getListOfOperations(self):
        return self.list_of_operations[:]
    
    def getListOfOperationsRedo(self):
        return self.list_of_operations_redo[:]
    
    def addNewOperation(self,newOperationUndo,newOperationRedo):
        if (self.index_of_operation>=0):
            del self.list_of_operations[(self.index_of_operation+1):]
            del self.list_of_operations_redo[(self.index_of_operation+1):]
        self.new_operation=True
        self.list_of_operations.append(newOperationUndo)
        self.list_of_operations_redo.append(newOperationRedo)
        self.index_of_operation+=1
       
    def performUndoFromRepository(self):
        commands={"removeStudent":self.__repoStudent.removeAStudentFromRepository,
                  "removeAssignment":self.__repoAssignment.removeAnAssignmentFromRepository,
                  "addStudent":self.__repoStudent.addNewStudentToRepository,
                  "addStudentOnPosition":self.__repoStudent.addNewStudentOnPosition,
                  "addAssignment":self.__repoAssignment.addNewAssignmentToRepository,
                  "addAssignmentOnPosition":self.__repoAssignment.addAssignmentOnPosition,
                  "updateStudentName":self.__repoStudent.updateTheStudentNameFromRepository,
                  "updateStudentGroup":self.__repoStudent.updateTheStudentGroupFromRepository,
                  "updateAssignmentDescription":self.__repoAssignment.updateTheAssignmentDescriptionFromRepository,
                  "updateAssignmentDeadline":self.__repoAssignment.updateTheAssignmentDeadlineFromRepository,
                  "removeAssignmentFromStudent":self.__repoGrade.removeAssignmentFromStudent,
                  "removeAssignmentFromGroup":self.__repoGrade.removeAnAssignmentGroupFromGradesList,
                  "removeGrade":self.__repoGrade.removeGradeFromStudent,
                  "addGrade":self.__repoGrade.giveAssignmentToAStudentFromRepository}
       
        if self.new_operation==True:
            self.index_of_operation=len(self.list_of_operations)-1
            
        listOfOperations=self.getListOfOperations()
        lastOperation=listOfOperations[self.index_of_operation]
        
        if self.index_of_operation>=0 :
            if(lastOperation.get_operation() in ["removeStudent" ,"removeAssignment"]):
                commands[lastOperation.get_operation()](lastOperation.get_parameters()[0])
                
            elif (lastOperation.get_operation()=="removeAssignmentFromStudent"):
                commands[lastOperation.get_operation()](lastOperation.get_parameters()[0],lastOperation.get_parameters()[1])
                
            elif(lastOperation.get_operation()=="removeAssignmentFromGroup"):
                group=lastOperation.get_parameters()[0]
                allStudents=self.__repoStudent.getStudents()
                for student in allStudents:
                    if(student.get_group()==group):
                        commands[lastOperation.get_operation()](lastOperation.get_parameters()[1],student.get_student_id())
                        
            elif(lastOperation.get_operation()=="removeGrade"):
                commands[lastOperation.get_operation()](lastOperation.get_parameters()[0],lastOperation.get_parameters()[1])
            
            elif(lastOperation.get_operation() in ["addStudent","addAssignment","addGrade"] ):
                commands[lastOperation.get_operation()](lastOperation.get_parameters_object())
          
            elif(lastOperation.get_operation() in ["addStudentOnPosition","addAssignmentOnPosition"]):
                commands[lastOperation.get_operation()](lastOperation.get_parameters_object(),lastOperation.get_position())
                 
            elif(lastOperation.get_operation() in ["updateStudentName","updateStudentGroup","updateAssignmentDescription","updateAssignmentDeadline"]):
                commands[lastOperation.get_operation()](lastOperation.get_parameters()[0],lastOperation.get_parameters()[3])
            
            self.new_operation=False
            self.index_of_operation-=1
        
                    
        else:
            raise Exception("No more undo are available!")
    
    def performRedoFromRepository(self):
        
        commands={"removeStudent":self.__repoStudent.removeAStudentFromRepository,
                  "removeAssignment":self.__repoAssignment.removeAnAssignmentFromRepository,
                  "addStudent":self.__repoStudent.addNewStudentToRepository,
                  "addStudentOnPosition":self.__repoStudent.addNewStudentOnPosition,
                  "addAssignment":self.__repoAssignment.addNewAssignmentToRepository,
                  "addAssignmentOnPosition":self.__repoAssignment.addAssignmentOnPosition,
                  "updateStudentName":self.__repoStudent.updateTheStudentNameFromRepository,
                  "updateStudentGroup":self.__repoStudent.updateTheStudentGroupFromRepository,
                  "updateAssignmentDescription":self.__repoAssignment.updateTheAssignmentDescriptionFromRepository,
                  "updateAssignmentDeadline":self.__repoAssignment.updateTheAssignmentDeadlineFromRepository,
                  "removeAssignmentFromStudent":self.__repoGrade.removeAssignmentFromStudent,
                  "removeAssignmentFromGroup":self.__repoGrade.removeAnAssignmentGroupFromGradesList,
                  "removeGrade":self.__repoGrade.removeGradeFromStudent,
                  "addGrade":self.__repoGrade.giveAssignmentToAStudentFromRepository,
                  "addAssignmentToGroup":self.__repoGrade.giveAssignmentToAStudentFromRepository,
                  "gradeStudent":self.__repoGrade.addGradeToGradedAssignmentsList}
        
        self.index_of_operation+=1
        if(self.index_of_operation>=0 and self.index_of_operation!=len(self.list_of_operations_redo)):
            listOfOperations=self.getListOfOperationsRedo()
            lastOperation=listOfOperations[self.index_of_operation]
            
            if lastOperation.get_operation() in commands:
                if(lastOperation.get_operation() in ["removeStudent" ,"removeAssignment"]):
                    commands[lastOperation.get_operation()](lastOperation.get_parameters()[0])
                    
                elif (lastOperation.get_operation()=="removeAssignmentFromStudent"):
                    commands[lastOperation.get_operation()](lastOperation.get_parameters()[0],lastOperation.get_parameters()[1])
                    
                elif(lastOperation.get_operation()=="removeAssignmentFromGroup"):
                    group=lastOperation.get_parameters()[0]
                    allStudents=self.__repoStudent.getStudents()
                    for student in allStudents:
                        if(student.get_group()==group):
                            commands[lastOperation.get_operation()](lastOperation.get_parameters()[1],student.get_student_id()) 
                    
                elif(lastOperation.get_operation()=="removeGrade"):
                    commands[lastOperation.get_operation()](lastOperation.get_parameters()[0],lastOperation.get_parameters()[1])
                    
                elif(lastOperation.get_operation() in ["addStudent","addAssignment","addGrade"] ):
                    commands[lastOperation.get_operation()](lastOperation.get_parameters_object())
                   
                elif(lastOperation.get_operation() in ["addStudentOnPosition","addAssignmentOnPosition"]):
                    commands[lastOperation.get_operation()](lastOperation.get_parameters_object(),lastOperation.get_position())
                    
                elif(lastOperation.get_operation() in ["updateStudentName","updateStudentGroup","updateAssignmentDescription","updateAssignmentDeadline"]):
                    commands[lastOperation.get_operation()](lastOperation.get_parameters()[0],lastOperation.get_parameters()[3]) 
                      
                elif(lastOperation.get_operation()=="addAssignmentToGroup"):
                    list_of_grades=lastOperation.get_parameters()
                    for grades in list_of_grades:
                        commands[lastOperation.get_operation()](grades)
                        
                elif(lastOperation.get_operation()=="gradeStudent"):
                    commands[lastOperation.get_operation()](lastOperation.get_parameters_object())
        else:
            self.index_of_operation-=1
            raise Exception("No more redo are available!")  
         
class FileRepoStudent(RepoStudent):
    def __init__(self,filename,read_student,write_student):
        RepoStudent.__init__(self)
        self.__filename= filename
        self.__read_student= read_student
        self.__write_student= write_student
        
    def __read_all_from_file(self):
        self._list_of_students=[]
        with open(self.__filename,"r") as file:
            lines= file.readlines()
            for line in lines:
                line= line.strip()
                if line!="":
                    student=self.__read_student(line)
                    self._list_of_students.append(student)
                    
    def __write_all_to_file(self):
        with open(self.__filename,"w") as file:
            for student in self._list_of_students:
                file.write(self.__write_student(student) + "\n")
                
    def getStudents(self):
        self.__read_all_from_file()
        return RepoStudent.getStudents(self)
    
    def addNewStudentToRepository(self, student):
        self.__read_all_from_file()
        RepoStudent.addNewStudentToRepository(self, student)   
        self.__write_all_to_file()
    def addNewStudentOnPosition(self, student, position):
        self.__read_all_from_file()
        RepoStudent.addNewStudentOnPosition(self, student, position) 
        self.__write_all_to_file()
        
    def removeAStudentFromRepository(self, studentID):
        self.__read_all_from_file()
        RepoStudent.removeAStudentFromRepository(self, studentID)
        self.__write_all_to_file()
        
    def updateTheStudentGroupFromRepository(self, studentID, group):
        self.__read_all_from_file()
        RepoStudent.updateTheStudentGroupFromRepository(self, studentID, group)
        self.__write_all_to_file()
        
    def updateTheStudentNameFromRepository(self, studentID, name):
        self.__read_all_from_file()
        RepoStudent.updateTheStudentNameFromRepository(self, studentID, name)
        self.__write_all_to_file()
 
 
        
class FileRepoAssignment(RepoAssignment):
    def __init__(self,filename,read_assignment,write_assignment):
        RepoAssignment.__init__(self)
        self.__filename=filename
        self.__read_assignment=read_assignment
        self.__write_assignment=write_assignment
        
    def __read_all_from_file(self):
        self._list_of_assignments=[]
        with open(self.__filename,"r") as file:
            lines=file.readlines()
            for line in lines:
                line=line.strip()
                if line!="":
                    assignment=self.__read_assignment(line)
                    self._list_of_assignments.append(assignment)
                    
    def __write_all_to_file(self):
        with open(self.__filename,"w") as file:
            for assignment in self._list_of_assignments:
                file.write(self.__write_assignment(assignment) + "\n")
    
    def getAssignments(self):
        self.__read_all_from_file()
        return RepoAssignment.getAssignments(self)   
    #   self.__write_all_to_file()
    def addAssignmentOnPosition(self, assignment, position):
        self.__read_all_from_file()
        RepoAssignment.addAssignmentOnPosition(self, assignment, position)
        self.__write_all_to_file()
    def addNewAssignmentToRepository(self, assignment):
        self.__read_all_from_file()
        RepoAssignment.addNewAssignmentToRepository(self, assignment)
        self.__write_all_to_file()
        
    def removeAnAssignmentFromRepository(self, assignmentID):
        self.__read_all_from_file()
        RepoAssignment.removeAnAssignmentFromRepository(self, assignmentID)
        self.__write_all_to_file()
        
    def updateTheAssignmentDeadlineFromRepository(self, assignmentID, deadline):
        self.__read_all_from_file()
        RepoAssignment.updateTheAssignmentDeadlineFromRepository(self, assignmentID, deadline)
        self.__write_all_to_file()
        
    def updateTheAssignmentDescriptionFromRepository(self, assignmentID, description):
        self.__read_all_from_file()
        RepoAssignment.updateTheAssignmentDescriptionFromRepository(self, assignmentID, description)
        self.__write_all_to_file()
        
    def getLateAssignmentsFromRepository(self, deadline):
        self.__read_all_from_file()
        return RepoAssignment.getLateAssignmentsFromRepository(self, deadline)   
    #    self.__write_all_to_file() 
         
                
class FileRepoGrade(RepoGrade):
    def __init__(self,filename_first,filename_second,read_grade,write_grade,repoStudent,repoAssignment):
        RepoGrade.__init__(self,repoStudent,repoAssignment)
        self.__filename_first=filename_first
        self.__filename_second=filename_second
        self.__read_grade=read_grade
        self.__write_grade=write_grade
        
    def __read_all_from_first_file(self):
        self._list_of_grades=[]
        with open(self.__filename_first,"r") as file:
            lines=file.readlines()
            for line in lines:
                line=line.strip()
                if line!="":
                    grade=self.__read_grade(line)
                    self._list_of_grades.append(grade)
                    
    def __write_all_to_first_file(self):
        with open(self.__filename_first,"w") as file:
            for grade in self._list_of_grades:
                file.write(self.__write_grade(grade) + "\n")
                
    def __read_all_from_second_file(self):
        self._list_of_initialised_grades=[]
        with open(self.__filename_second,"r") as file:
            lines=file.readlines()
            for line in lines:
                line=line.strip()
                if line!="":
                    grade=self.__read_grade(line)
                    self._list_of_initialised_grades.append(grade)
                    
    def __write_all_to_second_file(self):
        with open(self.__filename_second,"w") as file:
            for grade in self._list_of_initialised_grades:
                file.write(self.__write_grade(grade) + "\n")
                    
    def get_grades(self):
        self.__read_all_from_first_file()
        return RepoGrade.get_grades(self)
    
    def get_initialised_grades(self):
        self.__read_all_from_second_file()
        return RepoGrade.get_initialised_grades(self)
    
    def giveAssignmentToAStudentFromRepository(self, Grade):
        self.__read_all_from_first_file()
        RepoGrade.giveAssignmentToAStudentFromRepository(self, Grade)
        self.__write_all_to_first_file()
        
    def removeAssignmentFromStudent(self, assignmentID, studentID):
        self.__read_all_from_first_file()
        RepoGrade.removeAssignmentFromStudent(self, assignmentID, studentID)
        self.__write_all_to_first_file()
        
    def addGradeToRepository(self, Grade):
        self.__read_all_from_first_file()
        RepoGrade.addGradeToRepository(self, Grade)
        self.__write_all_to_first_file()
        
    def addGradeToGradedAssignmentsList(self, Grade):
        self.__read_all_from_second_file()
        RepoGrade.addGradeToGradedAssignmentsList(self, Grade)
        self.__write_all_to_second_file()
        
    def removeAStudentFromGradedAssignmentsList(self, studentID):
        self.__read_all_from_second_file()
        RepoGrade.removeAStudentFromGradedAssignmentsList(self, studentID)
        self.__write_all_to_second_file()
        
    def removeAStudentFromGradesList(self, studentID):
        self.__read_all_from_first_file()
        RepoGrade.removeAStudentFromGradesList(self, studentID)
        self.__write_all_to_first_file()
        
    def removeAnAssignmentFromGradesList(self, assignmentID):
        self.__read_all_from_first_file()
        RepoGrade.removeAnAssignmentFromGradesList(self, assignmentID)
        self.__write_all_to_first_file()
        
    def removeAnAssignmentGroupFromGradesList(self, assignmentID, studentID):
        self.__read_all_from_first_file()
        RepoGrade.removeAnAssignmentGroupFromGradesList(self, assignmentID, studentID)
        self.__write_all_to_first_file()
        
    def removeAnAssignmentFromGradedAssignmentsList(self, assignmentID):
        self.__read_all_from_second_file()
        RepoGrade.removeAnAssignmentFromGradedAssignmentsList(self, assignmentID)
        self.__write_all_to_second_file()
        
    def removeGradeFromStudent(self, studentID, assignmentID):
        self.__read_all_from_second_file()
        RepoGrade.removeGradeFromStudent(self, studentID, assignmentID)
        self.__write_all_to_second_file()
     # !!!!!!!!!!!!!!!!!!!!!!!!
     #!!!!!!!!!!!!!!!
     #!!!!!!!!!!!!   
    def gradeStudentFromRepository(self, Grade):
        self.__read_all_from_first_file()
      #  self.__read_all_from_second_file()
        RepoGrade.gradeStudentFromRepository(self, Grade)
     #   self.__write_all_to_first_file()
        self.__write_all_to_second_file()
        
    def studentsOrderedByAverageGradeOfAssignmentFromRepository(self, assignmentID):
        self.__read_all_from_second_file()
        return RepoGrade.studentsOrderedByAverageGradeOfAssignmentFromRepository(self, assignmentID)
    
    def getLateUngradedAssignmentsFromRepository(self, allLateAssignmentsID):
        self.__read_all_from_first_file()
        return RepoGrade.getLateUngradedAssignmentsFromRepository(self, allLateAssignmentsID)
    
    def statisticStudentsListOfGrades(self, allStudents):
        self.__read_all_from_second_file()
        return RepoGrade.statisticStudentsListOfGrades(self, allStudents)
    
    def studentsWithBestSchoolSituationFromRepository(self, statisticStudentsListOfGrades):
        self.__read_all_from_second_file()
        return RepoGrade.studentsWithBestSchoolSituationFromRepository(self, statisticStudentsListOfGrades)
    
    
class BinaryRepoStudent(RepoStudent):
    def __init__(self,filename,read_student,write_student):
        RepoStudent.__init__(self)
        self.__filename=filename
        self.__read_student=read_student
        self.__write_student=write_student
        
    def __write_binary_file(self):
        with open(self.__filename,"wb") as file:
            for student in self._list_of_students:
                pickle.dump(self.__write_student(student),file)
    
    def __read_binary_file(self):
        self._list_of_students=[]
        with open(self.__filename,"rb") as file:
            while True:
                try:
                    line=pickle.load(file)
                    student=self.__read_student(line)
                    self._list_of_students.append(student)
                except EOFError:
                    break
                
    def getStudents(self):
        self.__read_binary_file()
        return RepoStudent.getStudents(self)
    
    def addNewStudentToRepository(self, student):
        self.__read_binary_file()
        RepoStudent.addNewStudentToRepository(self, student)   
        self.__write_binary_file()
    def addNewStudentOnPosition(self, student, position):
        self.__read_binary_file()
        RepoStudent.addNewStudentOnPosition(self, student, position) 
        self.__write_binary_file()
        
    def removeAStudentFromRepository(self, studentID):
        self.__read_binary_file()
        RepoStudent.removeAStudentFromRepository(self, studentID)
        self.__write_binary_file()
        
    def updateTheStudentGroupFromRepository(self, studentID, group):
        self.__read_binary_file()
        RepoStudent.updateTheStudentGroupFromRepository(self, studentID, group)
        self.__write_binary_file()
        
    def updateTheStudentNameFromRepository(self, studentID, name):
        self.__read_binary_file()
        RepoStudent.updateTheStudentNameFromRepository(self, studentID, name)
        self.__write_binary_file()
        
class BinaryAssignmentRepo(RepoAssignment):
    def __init__(self,filename,read_assignment,write_assignment):
        RepoAssignment.__init__(self)
        self.__filename=filename
        self.__read_assignment=read_assignment
        self.__write_assignment=write_assignment
    
    def __write_binary_file(self):
        with open(self.__filename,"wb") as file:
            for assignment in self._list_of_assignments:
                pickle.dump(self.__write_assignment(assignment),file)
    
    def __read_binary_file(self):
        self._list_of_assignments=[]
        with open(self.__filename,"rb") as file:
            while True:
                try:
                    line=pickle.load(file)
                    assignment=self.__read_assignment(line)
                    self._list_of_assignments.append(assignment)
                except EOFError:
                    break  
        
    def getAssignments(self):
        self.__read_binary_file()
        return RepoAssignment.getAssignments(self)   
    
    def addAssignmentOnPosition(self, assignment, position):
        self.__read_binary_file()
        RepoAssignment.addAssignmentOnPosition(self, assignment, position)
        self.__write_binary_file()
    def addNewAssignmentToRepository(self, assignment):
        self.__read_binary_file()
        RepoAssignment.addNewAssignmentToRepository(self, assignment)
        self.__write_binary_file()
        
    def removeAnAssignmentFromRepository(self, assignmentID):
        self.__read_binary_file()
        RepoAssignment.removeAnAssignmentFromRepository(self, assignmentID)
        self.__write_binary_file()
        
    def updateTheAssignmentDeadlineFromRepository(self, assignmentID, deadline):
        self.__read_binary_file()
        RepoAssignment.updateTheAssignmentDeadlineFromRepository(self, assignmentID, deadline)
        self.__write_binary_file()
        
    def updateTheAssignmentDescriptionFromRepository(self, assignmentID, description):
        self.__read_binary_file()
        RepoAssignment.updateTheAssignmentDescriptionFromRepository(self, assignmentID, description)
        self.__write_binary_file()
        
    def getLateAssignmentsFromRepository(self, deadline):
        self.__read_binary_file()
        return RepoAssignment.getLateAssignmentsFromRepository(self, deadline)   