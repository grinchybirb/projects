class student_class:
    def __init__(self) -> None:
        print("new person added")
        self.name=None
        self.grade_total=0
        self.semesters=0
        self.average=0
        return

def read_file():
    file_path = 'input.txt'
    file_text = open(file_path, "r")
    student_list=[]
    for i_line in file_text:
        if i_line=="\n":
            continue

        tokens=i_line.split()
        print("tokens",tokens)
        name=tokens[0]
        sub=tokens[1]
        grade=int(tokens[2])
        print(name,sub,grade)
        # check if student is new
        student_found=False
        for student in student_list:
            if student.name==name:
                student_found=True
                student.semesters +=1
                student.grade_total+=grade
                student.average=student.grade_total/student.semesters
                break
        
        
        if student_found==False:
            student_obj=student_class()
            student_obj.name=name
            student_obj.grade_total=grade
            student_obj.semesters=1
            student_list.append(student_obj)

            
    for student in student_list:
        print(student.name,student.average,student.semesters,student.grade_total)
    file_text.close()

read_file()