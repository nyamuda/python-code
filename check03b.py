
class Complex :
    def __init__(self) :
        self.imaginary=0
        self.real=0

    def display(self) :
        print(f'{self.real} + {self.imaginary}i')

    def prompt(self) :
        self.real=input('Please enter the real part: ')
        self.imaginary=input('Please enter the imaginary part: ')



def main():
    c1 = Complex()
    c2 = Complex()

    print("The values are:")
    c1.display()
    c2.display()

    print()
    c1.prompt()

    print()
    c2.prompt()

    print("\nThe values are:")
    c1.display()
    c2.display()

# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()
