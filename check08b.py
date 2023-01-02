class GPA :
    def __init__(self) :
        self._gpa=0.0
    
    def _get_gpa(self) :
        return self._gpa
    
    def _set_gpa(self,value) :
        if self._get_gpa()<0 :
            self._gpa=0
        elif self._get_gpa()>4 :
            self._gpa=4
        else :
            self._gpa=value

    @property
    def letter(self) :
        current_gpa=self._get_gpa()
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
    @letter.setter
    def letter(self,letter) :
         if letter=='F':
            self._set_gpa(0.0)
         if letter=='D':
            self._set_gpa(1.0)
         if letter=='C':
            self._set_gpa(2.0)
         if letter=='B':
            self._set_gpa(3.0)
         if letter=='A':
            self._set_gpa(4.0)

    gpa=property(_get_gpa,_set_gpa)


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa=value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter=letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()
     


        



