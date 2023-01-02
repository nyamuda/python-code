class Person :
    def __init__(self,name='anonymous',birth_year='unknown') :
        self.name=name
        self.birth_year=birth_year

    def display(self) :
        author_info=f'{self.name} (b. {self.birth_year})'
        return author_info


class Book :
    def __init__(self,title='untitled',publisher='unpublished') :
        self.title=title
        self.publisher=publisher
        self.author=Person()

    def display(self) :
        print(self.title)
        print(F'Publisher:\n{self.publisher}')
        print(f'Author:\n{self.author.display()}')



def main() :
    b=Book()
    b.display()
    print('')
    print('Please enter the following:')
    author_name=input('Name: ')
    birth_year=input('Year: ')
    title=input('Title: ')
    publisher=input('Publisher: ')
    b.title=title
    b.publisher=publisher
    b.author.birth_year=birth_year
    b.author.name=author_name
    print('')
    b.display()

if __name__ == "__main__":
    main()
