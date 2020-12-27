from Repository.Repository import RepoStudent, RepoAssignment, RepoGrade, RepoUndo, FileRepoStudent, FileRepoAssignment,BinaryRepoStudent,BinaryAssignmentRepo
from Test.Test import Tests
from Services.Service import StudentService,AssignmentService,GradeService,UndoService
from Interface.UI import Console
from Domains.Domain import Student, Assignment,Grade

def read_settings(filename,settings):
    with open(filename,'r') as file:
        lines=file.readlines()
        for line in lines:
            line=line.strip()
            if line!='':
                parts=line.split('=')
                settings.append(parts[1].strip())

settings=list()

read_settings('settings.properties',settings)

if (settings[0]=='inmemory'):
    repoStudent=RepoStudent()
    repoAssignment=RepoAssignment()
    repoGrade=RepoGrade(repoStudent,repoAssignment)
elif(settings[0]=='textfiles'):
    repoStudent=FileRepoStudent(settings[1],Student.read_student,Student.write_student)
    repoAssignment=FileRepoAssignment(settings[2],Assignment.read_assignment,Assignment.write_assignment)
    repoGrade=RepoGrade(repoStudent,repoAssignment)
    
elif(settings[0]=='binaryfiles'):
    repoStudent=BinaryRepoStudent(settings[1],Student.read_student,Student.write_student)
    repoAssignment=BinaryAssignmentRepo(settings[2],Assignment.read_assignment,Assignment.write_assignment)
    repoGrade=RepoGrade(repoStudent,repoAssignment)

repoUndo=RepoUndo(repoStudent,repoAssignment,repoGrade)
studentService=StudentService(repoStudent,repoUndo)
assignmentService=AssignmentService(repoAssignment,repoUndo)
gradeService=GradeService(repoGrade,repoUndo)
undoService=UndoService(repoUndo)   
ui=Console(studentService,assignmentService,gradeService,undoService)    
test=Tests()
test.runAllTests()
ui.run()