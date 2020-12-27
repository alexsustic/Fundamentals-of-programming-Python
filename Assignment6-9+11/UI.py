import random
class Console:
    def __init__(self,studentService,assignmentService,gradeService,undoService):
        self.__studentService=studentService
        self.__assignmentService=assignmentService
        self.__gradeService=gradeService
        self.__undoService=undoService
    def readNumerical(self,text,numerical_type):
        number=input(text)
        while(True):
            try:
                number=numerical_type(number)
                return number
            except ValueError:
                number=input("Invalid numerical type! Try again:")
          
    def __uiAddNewStudent(self):
        studentID=self.readNumerical("Enter ID:", int)
        name=self.readNumerical("Enter name:", str)
        group=self.readNumerical("Enter group:", int)
        self.__studentService.addNewStudent(studentID,name,group)
        self.__undoService.addNewOperation("removeStudent",[studentID,name,group],None)
    def __uiAddNewAssignment(self):
        assignmentID=self.readNumerical("Enter ID:", int)
        description=self.readNumerical("Enter description:", str)
        deadline=self.readNumerical("Enter deadline:", str)
        self.__assignmentService.addNewAssignment(assignmentID,description,deadline)
        self.__undoService.addNewOperation("removeAssignment",[assignmentID,description,deadline],None)
    def __uiDisplayListOfAssignments(self):
        allAssignments=self.__assignmentService.displayListofAssignments()
        for assignment in allAssignments:
            print("AssignmentID:"+" "+str(assignment.get_assignment_id())+" "+" "+"Description:" +" "+ str(assignment.get_description())+ " "+ " "+"Deadline:"+ " "+str(assignment.get_deadline()))
    def __uiDisplayListOfStudents(self):
        allStudents=self.__studentService.displayListOfStudents()
        for student in allStudents:
            print("StudentID:"+" "+str(student.get_student_id())+" "+" "+"Name:" +" "+ str(student.get_name())+ " "+ " "+"Group:"+ " "+str(student.get_group()))
    def __uiRemoveAStudent(self):
        studentID=self.readNumerical("Enter the ID of the student you want to remove:", int)
        allStudents=self.__studentService.getAllStudents()
        index=0
        for student in allStudents:
            if(student.get_student_id()==studentID and index==len(allStudents)-1):
                self.__undoService.addNewOperation("addStudent",[studentID,student.get_name(),student.get_group()],None)
                break
            elif(student.get_student_id()==studentID and index<len(allStudents)-1):
                self.__undoService.addNewOperation("addStudentOnPosition",[studentID,student.get_name(),student.get_group()],index)
                break
            index=index+1
        self.__studentService.removeAStudent(studentID)
        self.__gradeService.removeAStudent(studentID)
    def __uiRemoveAnAssignment(self):
        assignmentID=self.readNumerical("Enter the ID of the assignment you want to remove:", int)
        allAssignments=self.__assignmentService.getAssignments()
        index=0
        for assignment in allAssignments:
            if(assignment.get_assignment_id()==assignmentID and index==len(allAssignments)-1):
                self.__undoService.addNewOperation("addAssignment",[assignmentID,assignment.get_description(),assignment.get_deadline()],None)
                break
            elif(assignment.get_assignment_id()==assignmentID and index<len(allAssignments)-1):
                self.__undoService.addNewOperation("addAssignmentOnPosition",[assignmentID,assignment.get_description(),assignment.get_deadline()],index)
                break
            index=index+1
        self.__assignmentService.removeAnAssignment(assignmentID)
        self.__gradeService.removeAnAssignment(assignmentID)
    def __uiUpdateAStudent(self):
        print("1.Update the name of a student")
        print("2.Update the group of a student")
        print("")
        command=self.readNumerical("What option would you like to choose:", int)
        if command==1:
            self.__uiUpdateTheStudentName()
        elif command==2:
            self.__uiUpdateTheStudentGroup()
        else:
            print("Invalid command!")
            
    def __uiUpdateTheStudentName(self):
        print("")
        studentID=self.readNumerical("Enter the ID of the student you want to change the name:", int)
        name=self.readNumerical("Enter the new name:", str)
        allStudents=self.__studentService.getStudents()
        for student in allStudents:
            if(student.get_student_id()==studentID):
                self.__undoService.addNewOperation("updateStudentName",[studentID,student.get_name(),student.get_group(),name],None)
        self.__studentService.updateTheStudentName(studentID,name)
        
    def __uiUpdateTheStudentGroup(self):
        print("")
        studentID=self.readNumerical("Enter the ID of the student you want to change the group:", int)
        group=self.readNumerical("Enter the new group:", int)
        allStudents=self.__studentService.getStudents()
        for student in allStudents:
            if(student.get_student_id()==studentID):
                self.__undoService.addNewOperation("updateStudentGroup",[studentID,student.get_group(),student.get_name(),group],None)
        self.__studentService.updateTheStudentGroup(studentID,group)
        
    def __uiUpdateTheAssignmentDescription(self):
        print("")
        assignmentID=self.readNumerical("Enter the ID of the assignment you want to change description", int)
        description=self.readNumerical("Enter the new description:", str)
        allAssignments=self.__assignmentService.getAssignments()
        for assignment in allAssignments:
            if(assignment.get_assignment_id()==assignmentID):
                self.__undoService.addNewOperation("updateAssignmentDescription",[assignmentID,assignment.get_description(),assignment.get_deadline(),description],None)
        self.__assignmentService.updateTheAssignmentDescription(assignmentID,description)
    
    def __uiUpdateTheAssignmentDeadline(self):
        print("")
        assignmentID=self.readNumerical("Enter the ID of the assignment you want to change deadline", int)
        deadline=self.readNumerical("Enter the new deadline:", str)
        allAssignments=self.__assignmentService.getAssignments()
        for assignment in allAssignments:
            if(assignment.get_assignment_id()==assignmentID):
                self.__undoService.addNewOperation("updateAssignmentDeadline",[assignmentID,assignment.get_deadline(),assignment.get_description(),deadline],None)
        self.__assignmentService.updateTheAssignmentDeadline(assignmentID,deadline)
    def __uiUpdateAnAssignment(self):
        
        print("1.Update the description of an assignment")
        print("2.Update the deadline of a student")
        print("")
        command=self.readNumerical("What option would you like to choose:", int)
        if command==1:
            self.__uiUpdateTheAssignmentDescription()
        elif command==2:
            self.__uiUpdateTheAssignmentDeadline()
        else:
            print("Invalid command!")
    def __uiGiveAssignmentToAStudent(self):
        studentID=self.readNumerical("Enter the id of the student you want to give an assignment:", int)
        assignmentID=self.readNumerical("Enter the id of the assignment you want to give to a student:", int)
        self.__undoService.addNewOperation("removeAssignmentFromStudent",[assignmentID,studentID],None)
        self.__gradeService.giveAssignmentToAStudent(studentID,assignmentID)
        
    def __uiGiveAssignmentToAGroup(self):
        group=self.readNumerical("Enter the group you want to give an assignment:", int)
        assignmentID=self.readNumerical("Enter the id of the assignment you want to give to a group:", int)
        self.__undoService.addNewOperation("removeAssignmentFromGroup",[group,assignmentID],None)
        self.__gradeService.giveAssignmentToAGroup(group,assignmentID)
        
    def __uiDisplayListOfGrades(self):
        allGrades=self.__gradeService.displayListOfGrades()
        for grade in allGrades:
            print("AssignmentID:" +" "+ str(grade.get_assignment_id())+ " "+"StudentID:"+" "+str(grade.get_student_id())+" "+"Grade:"+ " "+str(grade.get_grade()))
    def __uiAddRandomStudentsAndAssignmentsToTheList(self):
        list_of_students_id=[9000,9001,8765,2345,9002,8766,3000,9873,3478,8765,1234,9983,3456,2298,5067,3289,2333,7345,7654,8832]
        list_of_students_name=["Alex","Marius","Adriana","Diana","Dragos","Denisa","Andreea","George","Carina","Mihai","Catalin","Mariuca","Maria","Ioana"]
        list_of_students_group=[900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917]
        list_of_assignment_id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 
        list_of_assignment_description=["Homework","Prepare for the examn","Mandatory","Prepare for the mid-term","Do it or you will fail!","Do not skip it!"]
        list_of_assignment_deadline=["week 1", "week 2","week 3","week 4","week 5", "week 6", "week 7","week 8","week 9", "week 10"]
        index=0
        while(index<10):
            studentID=random.choice(list_of_students_id)
            studentName=random.choice(list_of_students_name)
            studentGroup=random.choice(list_of_students_group)
            verification=False
            while(verification==False):
                try:
                    self.__studentService.addNewStudent(studentID,studentName,studentGroup)
                    verification=True
                except Exception :
                    studentID=random.choice(list_of_students_id)
           
            assignmentID=random.choice(list_of_assignment_id)
            assignmentDescription=random.choice(list_of_assignment_description)
            assignmentDeadline=random.choice(list_of_assignment_deadline)
            verification=False
            while(verification==False):
                try:
                    self.__assignmentService.addNewAssignment(assignmentID,assignmentDescription,assignmentDeadline)
                    verification=True
                except Exception :
                    assignmentID=random.choice(list_of_assignment_id)
            index=index+1
        
    def __uiGradeStudent(self):
        student=self.readNumerical("Which student would you like to grade:", int)   
        assignment=self.readNumerical("Which assignment would you like to grade:", int)
        grade=self.readNumerical("Enter the grade:", int)
        self.__undoService.addNewOperation("removeGrade",[student,assignment,grade],None)
        self.__gradeService.gradeStudent(student,assignment,grade)
        
    def __uiDisplayListOfGradedAssignments(self):
        allGrades=self.__gradeService.displayListOfGradedAssignments()
        for grade in allGrades:
            print("AssignmentID:" +" "+ str(grade.get_assignment_id())+ " "+"StudentID:"+" "+str(grade.get_student_id())+" "+"Grade:"+ " "+str(grade.get_grade()))
    def __uiStudentsOrderedByAverageGradeOfAssignment(self):
        assignmentID=self.readNumerical("Enter assignmentID:", int)
        allGrades= self.__gradeService.studentsOrderedByAverageGradeOfAssignment(assignmentID)  
        allStudents=self.__studentService.getStudents()
        for grades in allGrades:
            for student in allStudents:
                if grades.get_student_id()==student.get_student_id():
                    print("StudentID:"+" "+str(student.get_student_id())+" "+" "+"Name:" +" "+ str(student.get_name())+ " "+ " "+"Group:"+ " "+str(student.get_group()))
                    break
    
    def __uiLateStudentsInHandingAssignment(self):
        deadline=self.readNumerical("Enter the deadline:", str)
        allLateAssignmentsID=self.__assignmentService.getLateAssignments(deadline)
        allLateStudentsID=self.__gradeService.getLateUngradedAssignments(allLateAssignmentsID)
        allStudents=self.__studentService.getAllStudents()
        for studentID in allLateStudentsID:
            for student in allStudents:
                if(student.get_student_id()==studentID):
                    print("StudentID:"+" "+str(student.get_student_id())+" "+" "+"Name:" +" "+ str(student.get_name())+ " "+ " "+"Group:"+ " "+str(student.get_group()))
                    break
                
    def __uiStudentsWithBestSchoolSituation(self):
        allStudents=self.__studentService.getAllStudents()
        StudentID_BestSchoolSituation=self.__gradeService.studentsWithBestSchoolSituation(allStudents)
        for studentID in StudentID_BestSchoolSituation:
            for student in allStudents:
                if(studentID==student.get_student_id()):
                    print("StudentID:"+" "+str(student.get_student_id())+" "+" "+"Name:" +" "+ str(student.get_name())+ " "+ " "+"Group:"+ " "+str(student.get_group()))
                    break
    def __uiUndo(self):
        self.__undoService.performUndo()  
        
    def __uiRedo(self):
        self.__undoService.performRedo()
    def __uiDisplayListOfOperations(self):
        allOperations=self.__undoService.getOperations()
        for operation in allOperations:
            print(str(operation.get_operation()) +" "+str(operation.get_parameters()))
    def printMenu(self):
        print("1.Add new student")   
        print("2.Add new assignment")
        print("3.Display list of students")
        print("4.Display list of assignments")
        print("5.Remove a student")
        print("6.Remove an assignment")
        print("7.Update a student")
        print("8.Update an assignment")
        print("9.Give an assignment to a student")
        print("10.Give an assignment to a group")
        print("11.Display list of ungraded assignments")
        print("12.Grade student for a given assignment")
        print("13.Display list of graded assignments")
        print("14.Display all students who received a given assignment, ordered by average grade for that assignment")
        print("15.Display all students who are late in handing in at least one assignment")
        print("16.Display students with the best school situation")
        print("17.Undo")
        print("18.Redo")
    def run(self):
        functions={"1":self.__uiAddNewStudent,
                   "2":self.__uiAddNewAssignment,
                   "3":self.__uiDisplayListOfStudents,
                   "4":self.__uiDisplayListOfAssignments,
                   "5":self.__uiRemoveAStudent,
                   "6":self.__uiRemoveAnAssignment,
                   "7":self.__uiUpdateAStudent,
                   "8":self.__uiUpdateAnAssignment,
                   "9":self.__uiGiveAssignmentToAStudent,
                   "10":self.__uiGiveAssignmentToAGroup,
                   "11":self.__uiDisplayListOfGrades,
                   "12":self.__uiGradeStudent,
                   "13":self.__uiDisplayListOfGradedAssignments,
                   "14":self.__uiStudentsOrderedByAverageGradeOfAssignment,
                   "15":self.__uiLateStudentsInHandingAssignment,
                   "16":self.__uiStudentsWithBestSchoolSituation,
                   "17":self.__uiUndo,
                   "18":self.__uiRedo,
                   "19":self.__uiDisplayListOfOperations,}
        
        self.__uiAddRandomStudentsAndAssignmentsToTheList()
        while(True):
            print("")
            self.printMenu()
            print("")
            command=str(input("What option would you like to choose:"))
            print("")
            if command=="20":
                return
            if command in functions:
                try:
                    functions[command]()
                except Exception as ex:
                    print(ex)
                
        
        

