from Repository.Repository import RepoStudent,RepoAssignment
class ValidateStudent:
    def validateStudentID(self,student):
        error=''
        if student.get_student_id()<0:
            error+="Wrong ID!"
        if(len(error)>0):
            raise Exception(error)
    def validateStudentGroup(self,student):
        error=''
        group=student.get_group()
        if group<0:
            error+="Wrong group!"
        if(len(error)>0):
            raise Exception(error)    
        
class ValidateAssignment:
    
    def validateAssignmentID(self, assignment):
        error=''
        if assignment.get_assignment_id()<0:
            error+="Wrong assignment ID!"
        if(len(error)>0):
            raise Exception(error)

    def validateAssignmentDeadline(self, assignment):
        error=''
        deadline=assignment.get_deadline()
        list_of_words=deadline.split()
        if(len(list_of_words)!=2):
            error+="Invalid deadline syntax!"
        if(list_of_words[0]!="week"):
            error+="Invalid deadline syntax!"
        try:
            int(list_of_words[1])
        except Exception as ex:
            raise Exception(ex)
        if(int(list_of_words[1])<0):
            error+="Invalid deadline!"
        if(len(error)>0):
            raise Exception(error)

class ValidateGrade:
    def validateStudentID(self,Grade):
        if(Grade.get_student_id()<0):
            raise Exception("Invalid studentID!")
        existence_of_student=False
        repoStudent=RepoStudent()
        allStudents=repoStudent.getStudents()
        for student in allStudents:
            if student.get_student_id()==Grade.get_student_id():
                existence_of_student=True
        if(existence_of_student==False):
            raise Exception("Nonexistent student!")
        
    def validateAssignmentID(self,Grade):
        if(Grade.get_assignment_id()<0):
            raise Exception("Invalid assignmentID!")
        existence_of_assignment=False
        repoAssignment=RepoAssignment()
        allAssignments=repoAssignment.getAssignments()
        for assignment in allAssignments:
            if assignment.get_assignment_id()==Grade.get_assignment_id():
                existence_of_assignment=True
        if(existence_of_assignment==False):
            raise Exception("Nonexistent assignment!")
        

