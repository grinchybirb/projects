class student_class:
    def __init__(self) -> None:
        print("new person added")
        self.name=None
        self.grade_total=0
        self.semesters=0
        self.average=0
        return
    
    def print(self):
        self.average=self.grade_total/self.semesters
        print(self.name,self.average,self.semesters,self.grade_total)
        return

class sub_class:
    def __init__(self) -> None:
        self.name=None
        self.grade_total=0
        self.semesters=0
        self.average=0
        return
        
    def print(self):
        self.average=self.grade_total/self.semesters
        print(self.name,self.average,self.semesters,self.grade_total)
        return


def read_file():
    file_path = 'input.txt'
    file_text = open(file_path, "r")
    sub_list=[]
    student_list=[]
    for i_line in file_text:
        if i_line=="\n":
            continue

        tokens=i_line.split()
        print("tokens",tokens)
        name=tokens[0]
        subject=tokens[1]
        grade=int(tokens[2])
        print(name,subject,grade)
        # check if student is new
        student_found=False
        for student in student_list:
            if student.name==name:
                student_found=True
                student.semesters +=1
                student.grade_total+=grade
                break
        
        if student_found==False:
            student=student_class()
            student.name=name
            student.grade_total=grade
            student.semesters=1
            student_list.append(student)

        # check if subject is new
        sub_found=False
        for sub in sub_list:
            if sub.name==subject:
                sub_found=True
                sub.semesters +=1
                sub.grade_total +=grade
                break

        if sub_found==False:
            sub=sub_class()
            sub.name=subject
            sub.grade_total=grade
            sub.semesters=1
            sub_list.append(sub)

            
  
    file_text.close()
    for student in student_list:
        student.print()
    for sub in sub_list:
        sub.print()
read_file()