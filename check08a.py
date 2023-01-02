class GPA :
    def __init__(self) :
        self.gpa=0.0
    
    def get_gpa(self) :
        return self.gpa
    
    def set_gpa(self,value) :
        if self.get_gpa()<0 :
            self.gpa=0
        elif self.get_gpa()>4 :
            self.gpa=4
        else :
            self.gpa=value
    def  get_letter(self) :
        current_gpa=self.get_gpa()
        if current_gpa>=0.0 and current_gpa<=0.99 :
            return 'F'
        if current_gpa>=1.0 and current_gpa<=1.99 :
            return 'D'
        
        if current_gpa>=2.0 and current_gpa<=2.99 :
            return 'C'
        if current_gpa>=3.0 and current_gpa<=3.99 :
            return 'B'
        if current_gpa==4.0 :
            return 'A'
    
    def set_letter(self,letter) :
         if letter=='F':
            self.set_gpa(0.0)
         if letter=='D':
            self.set_gpa(1.0)
         if letter=='C':
            self.set_gpa(2.0)
         if letter=='B':
            self.set_gpa(3.0)
         if letter=='A':
            self.set_gpa(4.0)


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()
     


        



