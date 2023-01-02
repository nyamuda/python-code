class Student :
    def __init__(self,first_name,last_name,id_num) :
        self.first_name=first_name
        self.last_name=last_name
        self.id_num=id_num


def prompt_student() :
    first_name=input('Please enter your first name: ')
    last_name=input('Please enter your last name: ')
    id_num= input('Please enter your id number: ')
    print("")
    student=Student(first_name, last_name, id_num)
    display_student(student)

def display_student(obj) :
    print('Your information:')
    print(f"{obj.id_num} - {obj.first_name} {obj.last_name}")



prompt_student()