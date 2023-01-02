class Phone :
    def __init__(self) :
        self.area_code=0
        self.prefix=0
        self.suffix=0
    
    def prompt_number(self) :
        self.area_code=input('Area Code: ')
        self.prefix=input('Prefix: ')
        self.suffix=input('Suffix: ')
    
    def display(self) :
        print('Phone info:')
        print(f"({self.area_code}){self.prefix}-{self.suffix}")


class SmartPhone(Phone) :
    def __init__(self) :
        super().__init__()
        self.email=""
    

    def prompt(self) :
        super().prompt_number()
        self.email=input('Email: ')

    def display(self) :
        super().display()
        print(self.email)


def main() :
   phone=Phone()
   print("Phone:")
   phone.prompt_number()
   print("")
   phone.display()
   print("")
   smartPhone=SmartPhone()
   print('Smart phone:')
   smartPhone.prompt()
   print("")
   smartPhone.display()

if __name__ == "__main__":
    main()

    


