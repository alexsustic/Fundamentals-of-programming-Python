from Domains.Domain import Student, Assignment
from Validators.Validator import ValidateAssignment,ValidateStudent
from Repository.Repository import RepoStudent,RepoAssignment
import unittest

class UnitTesting(unittest.TestCase):
    def testcreateNewStudent__validName__nameCorrectlyAdded(self):
        student=Student(123,"Maria", 917)
        self.assertEqual(student.get_name(), "Maria", "Name incorrectly added!")
    def testcreateNewStudent__validStudentID__studentIDCorrectlyAdded(self):
        student=Student(123,"Maria", 917)
        self.assertEqual(student.get_student_id(), 123, "StudentID incorrectly added!")
    def testcreateNewStudent__validGroup__groupCorrectlyAdded(self):
        student=Student(123,"Maria", 917)
        self.assertEqual(student.get_group(),917,"Group incorrectly added!")
    def testcreateNewAssignment__validAssignmentID__assignmentIDCorrectlyAdeed(self):
        assignment=Assignment(123,"Prepare for the examn", "week 9")
        self.assertEqual(assignment.get_assignment_id(),123,"AssignmentID incorrectly added!")
    def testcreateNewAssignment__validDescription__descriptionCorrectlyAdeed(self):
        assignment=Assignment(123,"Prepare for the examn", "week 9")
        self.assertEqual(assignment.get_description(),"Prepare for the examn","Description incorrectly added!")
    def testcreateNewAssignment__validDeadline__deadlineCorrectlyAdeed(self):
        assignment=Assignment(123,"Prepare for the examn", "week 9")
        self.assertEqual(assignment.get_deadline(),"week 9","Deadline incorrectly added!")   
    def testValidateStudentID__incorrectStudent__raiseWrongIDError(self):
        incorect_student=Student(-123,"Ana Maria",917)
        try:
            ValidateStudent.validateStudentID(self,incorect_student)
            assert(False)
        except Exception as ex:
            self.assertEqual(str(ex),"Wrong ID!","Invalid student ID!")
    def testValidateStudentID__correctStudent__succesfulStudentIDValidation(self):       
        corect_student=Student(123,"Ana Maria",917)
        ValidateStudent.validateStudentID(self, corect_student)
    def testValidateStudentGroup__correctGroup__succesfulGroupValidation(self):
        corect_student=Student(123,"Ana Maria",917)
        ValidateStudent.validateStudentGroup(self, corect_student)
    def testValidateStudentGroup__incorrectGroup__RaiseWrongGroupError(self):
        incorect_student=Student(123,"Ana Maria",-917)
        try:
            ValidateStudent.validateStudentGroup(self,incorect_student)
            assert(False)
        except Exception as ex:
            self.assertEqual(str(ex),"Wrong group!","Invalid group!")
    def testValidateAssignmentID__correctAssignmentID__successfulAssignmentIDValidation(self):
        correct_assignment=Assignment(3,"Prepare for the examn","week 3")
        ValidateAssignment.validateAssignmentID(self,correct_assignment)
    def testValidateAssignmentID__incorrectAssignmentID__RaiseWrongAssignmentIDError(self):
        incorect_assignment=Assignment(-3,"Preapare for the examn","week 3")
        try:
            ValidateAssignment.validateAssignmentID(self,incorect_assignment)
            assert(False)
        except Exception as ex:
            self.assertEqual(str(ex),"Wrong assignment ID!","Invalid assignment ID!")
    def testValidateAssignmentDeadline__correctDeadline__succesfulDeadlineValidation(self):
        correct_assignment=Assignment(3,"Prepare for the examn","week 3")
        ValidateAssignment.validateAssignmentDeadline(self, correct_assignment)  
    def testValidateAssignmentDeadline__incorrectDealine__raiseInvalidDeadlineSyntaxError(self):    
        incorrect_assignment=Assignment(3,"Prepare for the examn","wek 3")
        try:
            ValidateAssignment.validateAssignmentDeadline(self,incorrect_assignment)
            assert(False)
        except Exception as ex:
            self.assertEqual(str(ex),"Invalid deadline syntax!","Invalid deadline!")
    
    def testAddNewStudent__ValidStudent__StudentSuccesfullyAdded(self):
        student=Student(2850,"Ana",910)
        studentRepository=RepoStudent()
        studentRepository.addNewStudentToRepository(student)
        repoStudentsList=studentRepository.getStudents()
        self.assertEqual(len(repoStudentsList),1,"Student adding failed!")
        studentRepository.removeAStudentFromRepository(2850)
    def testAddNewStudent__ValidStudentID__StudentIDSuccesfullyAdded(self):
        student=Student(2850,"Ana",910)
        studentRepository=RepoStudent()
        studentRepository.addNewStudentToRepository(student)
        repoStudentsList=studentRepository.getStudents()
        self.assertEqual(repoStudentsList[0].get_student_id(),2850,"StudentID adding failed!")
        studentRepository.removeAStudentFromRepository(2850)
    def testAddNewStudent__ValidName__NameSuccesfullyAdded(self):
        student=Student(2899,"Ana",910)
        studentRepository=RepoStudent()
        studentRepository.addNewStudentToRepository(student)
        repoStudentsList=studentRepository.getStudents()
        self.assertEqual(repoStudentsList[0].get_name(),"Ana","Name adding failed!")
        studentRepository.removeAStudentFromRepository(2899)
    def testAddNewStudent__ValidGroup__GroupSuccesfullyAdeed(self):
        student=Student(2850,"Ana",910)
        studentRepository=RepoStudent()
        studentRepository.addNewStudentToRepository(student)
        repoStudentsList=studentRepository.getStudents()
        self.assertEqual(repoStudentsList[0].get_group(),910,"Group adding failed!")
        studentRepository.removeAStudentFromRepository(2850)
    def testRemoveStudent(self):
        firstStudent=Student(2999,"Andreea",913)
        secondStudent=Student(2888,"Mihai",922)
        testStudentRepository=RepoStudent()
        testStudentRepository.addNewStudentToRepository(firstStudent)
        testStudentRepository.addNewStudentToRepository(secondStudent)
        testStudentRepository.removeAStudentFromRepository(2999)
        repoStudentsList=testStudentRepository.getStudents()
        self.assertEqual(len(repoStudentsList),1,"Student removing failed!")
        testStudentRepository.removeAStudentFromRepository(2888)
        
    def testUpdateStudent__newStudentName__nameChanged(self):
        student=Student(3000,"Maria",920)
        repoStudent=RepoStudent()
        repoStudent.addNewStudentToRepository(student)
        repoStudent.updateTheStudentNameFromRepository(3000, "Darius")
        testStudentListRepository=repoStudent.getStudents()
        self.assertEqual(testStudentListRepository[0].get_name(),"Darius","Name update failed!")
        repoStudent.removeAStudentFromRepository(3000)
    def testUpdateStudent__newGroup__GroupChanged(self): 
        student=Student(3000,"Maria",920)
        repoStudent=RepoStudent()
        repoStudent.addNewStudentToRepository(student)
        repoStudent.updateTheStudentGroupFromRepository(3000, 900)
        testStudentListRepository=repoStudent.getStudents()
        self.assertEqual(testStudentListRepository[0].get_group(),900,"Group update failed!")
        repoStudent.removeAStudentFromRepository(3000)
    def testAddNewAssignment__validAssignment__AssignmentSuccesfullyAdded(self):
        assignment=Assignment(3,"Haha","week 3")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(assignment)
        repoAssignmentList=repoAssignment.getAssignments()
        self.assertEqual(len(repoAssignmentList),1,"Assignment adding failed!")
        repoAssignment.removeAnAssignmentFromRepository(3)    
        
    def testAddNewAssignment__validDescription__DescriptionSuccesfullyAdded(self):
        assignment=Assignment(3,"Haha","week 3")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(assignment)
        repoAssignmentList=repoAssignment.getAssignments()
        self.assertEqual(repoAssignmentList[0].get_description(),"Haha","Description adding failed!")
        repoAssignment.removeAnAssignmentFromRepository(3)  
        
    def testAddNewAssignment__validDeadline__DeadlineSuccesfullyAdded(self):
        assignment=Assignment(3,"Haha","week 3")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(assignment)
        repoAssignmentList=repoAssignment.getAssignments()
        self.assertEqual(repoAssignmentList[0].get_deadline(),"week 3","Deadline adding failed!")
        repoAssignment.removeAnAssignmentFromRepository(3) 
          
    def testRemoveAnAssignment__newAssignment_NewAssignmentSuccesfullyRemoved(self):
        firstAssignment=Assignment(3,"Haha","week 3")
        secondAssignment=Assignment(4,"Muhaha","week 4")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(firstAssignment)
        repoAssignment.addNewAssignmentToRepository(secondAssignment)
        repoAssignment.removeAnAssignmentFromRepository(3)
        repoAssignmentList=repoAssignment.getAssignments()
        self.assertEqual(len(repoAssignmentList),1,"Assignment removing failed!")
        repoAssignment.removeAnAssignmentFromRepository(4)
        
    def testUpdateAnAssignment_newValidDescription_newValidDescriptionImplemented(self):
        assignment=Assignment(3,"Haha","week 3")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(assignment)
        repoAssignment.updateTheAssignmentDescriptionFromRepository(3, "Lala")
        repoAssignmentList=repoAssignment.getAssignments()
        self.assertEqual(repoAssignmentList[0].get_description(),"Lala","Description update failed!")
        repoAssignment.removeAnAssignmentFromRepository(3)
        
    def testUpdateAnAssignment_newValidDeadline_newValidDeadlineImplemented(self):
        assignment=Assignment(3,"Haha","week 3")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(assignment)
        repoAssignment.updateTheAssignmentDeadlineFromRepository(3, "week 7")
        repoAssignmentList=repoAssignment.getAssignments()
        self.assertEqual(repoAssignmentList[0].get_deadline(),"week 7","Description update failed!")
        repoAssignment.removeAnAssignmentFromRepository(3)
    
    
    def runAllTests(self):
        self.testcreateNewStudent__validName__nameCorrectlyAdded()
        self.testcreateNewStudent__validStudentID__studentIDCorrectlyAdded()
        self.testcreateNewStudent__validGroup__groupCorrectlyAdded()
        self.testcreateNewAssignment__validAssignmentID__assignmentIDCorrectlyAdeed()
        self.testcreateNewAssignment__validDescription__descriptionCorrectlyAdeed()
        self.testcreateNewAssignment__validDeadline__deadlineCorrectlyAdeed()
        self.testValidateStudentID__incorrectStudent__raiseWrongIDError() 
        self.testValidateStudentID__correctStudent__succesfulStudentIDValidation()
        self.testValidateStudentGroup__correctGroup__succesfulGroupValidation()
        self.testValidateStudentGroup__incorrectGroup__RaiseWrongGroupError()
        self.testValidateAssignmentID__correctAssignmentID__successfulAssignmentIDValidation()
        self.testValidateAssignmentID__incorrectAssignmentID__RaiseWrongAssignmentIDError()
        self.testAddNewStudent__ValidStudentID__StudentIDSuccesfullyAdded()
        self.testAddNewStudent__ValidName__NameSuccesfullyAdded()
        self.testAddNewStudent__ValidGroup__GroupSuccesfullyAdeed()
        self.testValidateAssignmentDeadline__correctDeadline__succesfulDeadlineValidation()
        self.testValidateAssignmentDeadline__incorrectDealine__raiseInvalidDeadlineSyntaxError()
        self.testUpdateStudent__newStudentName__nameChanged()
        self.testUpdateStudent__newGroup__GroupChanged()
        self.testAddNewAssignment__validAssignment__AssignmentSuccesfullyAdded()
        self.testAddNewAssignment__validDescription__DescriptionSuccesfullyAdded()
        self.testAddNewAssignment__validDeadline__DeadlineSuccesfullyAdded()
        self.testRemoveAnAssignment__newAssignment_NewAssignmentSuccesfullyRemoved()
        self.testUpdateAnAssignment_newValidDescription_newValidDescriptionImplemented()
        self.testUpdateAnAssignment_newValidDeadline_newValidDeadlineImplemented()
    
class Tests(object):
    def testcreateNewStudent__validName__nameCorrectlyAdded(self):
        student=Student(123,"Maria", 917)
        assert(student.get_name()=="Maria")
    def testcreateNewStudent__validStudentID__studentIDCorrectlyAdded(self):
        student=Student(123,"Maria", 917)
        assert(student.get_student_id()==123)
    def testcreateNewStudent__validGroup__groupCorrectlyAdded(self):
        student=Student(123,"Maria", 917)
        assert(student.get_group()==917)
    def testcreateNewAssignment__validAssignmentID__assignmentIDCorrectlyAdeed(self):
        assignment=Assignment(123,"Prepare for the examn", "week 9")
        assert(assignment.get_assignment_id()==123)
    def testcreateNewAssignment__validDescription__descriptionCorrectlyAdeed(self):
        assignment=Assignment(123,"Prepare for the examn", "week 9")
        assert(assignment.get_description()=="Prepare for the examn")
    def testcreateNewAssignment__validDeadline__deadlineCorrectlyAdeed(self):
        assignment=Assignment(123,"Prepare for the examn", "week 9")
        assert(assignment.get_deadline()=="week 9")   
    def testValidateStudentID__incorrectStudent__raiseWrongIDError(self):
        incorect_student=Student(-123,"Ana Maria",917)
        try:
            ValidateStudent.validateStudentID(self,incorect_student)
            assert(False)
        except Exception as ex:
            assert(str(ex)=="Wrong ID!")
    def testValidateStudentID__correctStudent__succesfulStudentIDValidation(self):       
        corect_student=Student(123,"Ana Maria",917)
        ValidateStudent.validateStudentID(self, corect_student)
            
    def testValidateStudentGroup__correctGroup__succesfulGroupValidation(self):
        corect_student=Student(123,"Ana Maria",917)
        ValidateStudent.validateStudentGroup(self, corect_student)
    def testValidateStudentGroup__incorrectGroup__RaiseWrongGroupError(self):
        incorect_student=Student(123,"Ana Maria",-917)
        try:
            ValidateStudent.validateStudentGroup(self,incorect_student)
            assert(False)
        except Exception as ex:
            assert(str(ex)=="Wrong group!")
    def testValidateAssignmentID__correctAssignmentID__successfulAssignmentIDValidation(self):
        correct_assignment=Assignment(3,"Prepare for the examn","week 3")
        ValidateAssignment.validateAssignmentID(self,correct_assignment)
    def testValidateAssignmentID__incorrectAssignmentID__RaiseWrongAssignmentIDError(self):
        incorect_assignment=Assignment(-3,"Preapare for the examn","week 3")
        try:
            ValidateAssignment.validateAssignmentID(self,incorect_assignment)
            assert(False)
        except Exception as ex:
            assert(str(ex)=="Wrong assignment ID!")
    def testValidateAssignmentDeadline__correctDeadline__succesfulDeadlineValidation(self):
        correct_assignment=Assignment(3,"Prepare for the examn","week 3")
        ValidateAssignment.validateAssignmentDeadline(self, correct_assignment)  
    def testValidateAssignmentDeadline__incorrectDealine__raiseInvalidDeadlineSyntaxError(self):    
        incorrect_assignment=Assignment(3,"Prepare for the examn","wek 3")
        try:
            ValidateAssignment.validateAssignmentDeadline(self,incorrect_assignment)
            assert(False)
        except Exception as ex:
            assert(str(ex)=="Invalid deadline syntax!")
    
    def testAddNewStudent__ValidStudent__StudentSuccesfullyAdded(self):
        student=Student(2850,"Ana",910)
        studentRepository=RepoStudent()
        studentRepository.addNewStudentToRepository(student)
        repoStudentsList=studentRepository.getStudents()
        assert(len(repoStudentsList)==1)
        studentRepository.removeAStudentFromRepository(2850)
    def testAddNewStudent__ValidStudentID__StudentIDSuccesfullyAdded(self):
        student=Student(2850,"Ana",910)
        studentRepository=RepoStudent()
        studentRepository.addNewStudentToRepository(student)
        repoStudentsList=studentRepository.getStudents()
        assert(repoStudentsList[0].get_student_id()==2850)
        studentRepository.removeAStudentFromRepository(2850)
    def testAddNewStudent__ValidName__NameSuccesfullyAdded(self):
        student=Student(2899,"Ana",910)
        studentRepository=RepoStudent()
        studentRepository.addNewStudentToRepository(student)
        repoStudentsList=studentRepository.getStudents()
        assert(repoStudentsList[0].get_name()=="Ana")
        studentRepository.removeAStudentFromRepository(2899)
    def testAddNewStudent__ValidGroup__GroupSuccesfullyAdeed(self):
        student=Student(2850,"Ana",910)
        studentRepository=RepoStudent()
        studentRepository.addNewStudentToRepository(student)
        repoStudentsList=studentRepository.getStudents()
        assert(repoStudentsList[0].get_group()==910)
        studentRepository.removeAStudentFromRepository(2850)
    def testRemoveStudent(self):
        firstStudent=Student(2999,"Andreea",913)
        secondStudent=Student(2888,"Mihai",922)
        testStudentRepository=RepoStudent()
        testStudentRepository.addNewStudentToRepository(firstStudent)
        testStudentRepository.addNewStudentToRepository(secondStudent)
        testStudentRepository.removeAStudentFromRepository(2999)
        repoStudentsList=testStudentRepository.getStudents()
        assert(len(repoStudentsList)==1)
        testStudentRepository.removeAStudentFromRepository(2888)
        
    def testUpdateStudent__newStudentName__nameChanged(self):
        student=Student(3000,"Maria",920)
        repoStudent=RepoStudent()
        repoStudent.addNewStudentToRepository(student)
        repoStudent.updateTheStudentNameFromRepository(3000, "Darius")
        testStudentListRepository=repoStudent.getStudents()
        assert(testStudentListRepository[0].get_name()=="Darius")
        repoStudent.removeAStudentFromRepository(3000)
    def testUpdateStudent__newGroup__GroupChanged(self): 
        student=Student(3000,"Maria",920)
        repoStudent=RepoStudent()
        repoStudent.addNewStudentToRepository(student)
        repoStudent.updateTheStudentGroupFromRepository(3000, 900)
        testStudentListRepository=repoStudent.getStudents()
        assert(testStudentListRepository[0].get_group()==900)
        repoStudent.removeAStudentFromRepository(3000)
    def testAddNewAssignment__validAssignment__AssignmentSuccesfullyAdded(self):
        assignment=Assignment(3,"Haha","week 3")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(assignment)
        repoAssignmentList=repoAssignment.getAssignments()
        assert(len(repoAssignmentList)==1)
        repoAssignment.removeAnAssignmentFromRepository(3) 
          
    def testAddNewAssignment__validDescription__DescriptionSuccesfullyAdded(self):
        assignment=Assignment(3,"Haha","week 3")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(assignment)
        repoAssignmentList=repoAssignment.getAssignments()
        assert(repoAssignmentList[0].get_description()=="Haha")
        repoAssignment.removeAnAssignmentFromRepository(3)  
        
    def testAddNewAssignment__validDeadline__DeadlineSuccesfullyAdded(self):
        assignment=Assignment(3,"Haha","week 3")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(assignment)
        repoAssignmentList=repoAssignment.getAssignments()
        assert(repoAssignmentList[0].get_deadline()=="week 3")
        repoAssignment.removeAnAssignmentFromRepository(3)  
    def testRemoveAnAssignment__newAssignment_NewAssignmentSuccesfullyRemoved(self):
        firstAssignment=Assignment(3,"Haha","week 3")
        secondAssignment=Assignment(4,"Muhaha","week 4")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(firstAssignment)
        repoAssignment.addNewAssignmentToRepository(secondAssignment)
        repoAssignment.removeAnAssignmentFromRepository(3)
        repoAssignmentList=repoAssignment.getAssignments()
        assert(len(repoAssignmentList)==1)
        repoAssignment.removeAnAssignmentFromRepository(4)
        
        
    def testUpdateAnAssignment_newValidDescription_newValidDescriptionImplemented(self):
        assignment=Assignment(3,"Haha","week 3")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(assignment)
        repoAssignment.updateTheAssignmentDescriptionFromRepository(3, "Lala")
        repoAssignmentList=repoAssignment.getAssignments()
        assert(repoAssignmentList[0].get_description()=="Lala")
        repoAssignment.removeAnAssignmentFromRepository(3)
        
    def testUpdateAnAssignment_newValidDeadline_newValidDeadlineImplemented(self):
        assignment=Assignment(3,"Haha","week 3")
        repoAssignment=RepoAssignment()
        repoAssignment.addNewAssignmentToRepository(assignment)
        repoAssignment.updateTheAssignmentDeadlineFromRepository(3, "week 7")
        repoAssignmentList=repoAssignment.getAssignments()
        assert(repoAssignmentList[0].get_deadline()=="week 7")
        repoAssignment.removeAnAssignmentFromRepository(3)
    def runAllTests(self):
        self.testcreateNewStudent__validName__nameCorrectlyAdded()
        self.testcreateNewStudent__validStudentID__studentIDCorrectlyAdded()
        self.testcreateNewStudent__validGroup__groupCorrectlyAdded()
        self.testcreateNewAssignment__validAssignmentID__assignmentIDCorrectlyAdeed()
        self.testcreateNewAssignment__validDescription__descriptionCorrectlyAdeed()
        self.testcreateNewAssignment__validDeadline__deadlineCorrectlyAdeed()
        self.testValidateStudentID__incorrectStudent__raiseWrongIDError() 
        self.testValidateStudentID__correctStudent__succesfulStudentIDValidation()
        self.testValidateStudentGroup__correctGroup__succesfulGroupValidation()
        self.testValidateStudentGroup__incorrectGroup__RaiseWrongGroupError()
        self.testValidateAssignmentID__correctAssignmentID__successfulAssignmentIDValidation()
        self.testValidateAssignmentID__incorrectAssignmentID__RaiseWrongAssignmentIDError()
        self.testAddNewStudent__ValidStudentID__StudentIDSuccesfullyAdded()
        self.testAddNewStudent__ValidName__NameSuccesfullyAdded()
        self.testAddNewStudent__ValidGroup__GroupSuccesfullyAdeed()
        self.testValidateAssignmentDeadline__correctDeadline__succesfulDeadlineValidation()
        self.testValidateAssignmentDeadline__incorrectDealine__raiseInvalidDeadlineSyntaxError()
        self.testUpdateStudent__newStudentName__nameChanged()
        self.testUpdateStudent__newGroup__GroupChanged()
        self.testAddNewAssignment__validAssignment__AssignmentSuccesfullyAdded()
        self.testAddNewAssignment__validDescription__DescriptionSuccesfullyAdded()
        self.testAddNewAssignment__validDeadline__DeadlineSuccesfullyAdded()
        self.testRemoveAnAssignment__newAssignment_NewAssignmentSuccesfullyRemoved()
        self.testUpdateAnAssignment_newValidDescription_newValidDescriptionImplemented()
        self.testUpdateAnAssignment_newValidDeadline_newValidDeadlineImplemented()