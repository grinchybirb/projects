class student_class:
    def __init__(self) -> None:
        print("new person added")
        self.subject_dict={}
        return
    
    def print(self):
        for temp in self.subject_dict:
            print(temp,self.subject_dict[temp].grade_total/self.subject_dict[temp].count,"max",self.subject_dict[temp].max)
        return

class std_sub_class:
    def __init__(self,grade) -> None:
        self.grade_total=grade
        self.count=1
        self.max=grade


        return




def read_file():
    file_path = 'input.txt'
    file_text = open(file_path, "r")
    student_dict={}
    for i_line in file_text:
        if i_line=="\n":
            continue
        if i_line=="#":
            continue

        tokens=i_line.split()
        print("tokens",tokens)
        student_name=tokens[0]
        subject_name=tokens[1]
        grade=int(tokens[2])
        print(student_name,subject_name,grade)
        # check if student is new

        if student_name in student_dict:
            # look for subject in the student dictionary of subjects
            student_obj=student_dict[student_name]
            if subject_name  in student_obj.subject_dict:
                # updating existing std_sub
                student_obj.subject_dict[subject_name].grade_total +=grade
                student_obj.subject_dict[subject_name].count +=1
                if student_obj.subject_dict[subject_name].max<grade:
                    student_obj.subject_dict[subject_name].max=grade
                

            else:
                # new std_sub
                std_sub=std_sub_class(grade)
                student_obj.subject_dict[subject_name]=std_sub           
        
        else:
            
            # new std_sub
            std_sub=std_sub_class(grade)
            # new student
            student_obj=student_class()
            student_obj.subject_dict[subject_name]=std_sub
            # add new student to the dictionary
            student_dict[student_name]=student_obj


    file_text.close()
    for student in student_dict:
        print(student)
        student_dict[student].print()

read_file()