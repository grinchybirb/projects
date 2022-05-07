class student_class:
    def __init__(self,name) -> None:
        print("new person added")
        self.name=name
        self.subject_dict={}
        return
    
    def print(self):
        print("=====",self.name)
        for temp in self.subject_dict:
            print(temp,self.subject_dict[temp].grade_total/self.subject_dict[temp].count)
        return

class std_sub_class:
    def __init__(self,grade_total,count) -> None:
        self.grade_total=grade_total
        self.count=count



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
                # look for subject in the student dictionary of subjects

                if subject  in student.subject_dict:
                    # updating existing std_sub
                    student.subject_dict[subject].grade_total +=grade
                    student.subject_dict[subject].count +=1
                   

                else:
                    # new std_sub
                    std_sub=std_sub_class(grade,1)
                    student.subject_dict[subject]=std_sub

                break
        
        if student_found==False:
            
            # new std_sub
            std_sub=std_sub_class(grade,1)

            # new student
            student=student_class(name)
            student.subject_dict[subject]=std_sub
            # add new student to the list
            student_list.append(student)

        # check if subject is new

            
  
    file_text.close()
    for student in student_list:
        student.print()

read_file()