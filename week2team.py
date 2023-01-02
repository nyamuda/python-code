def prompt_filename() :
     fileName=input('Enter file name: ')
     return fileName


def main() :
    name=prompt_filename()
    print(f'Opening file {name}')
    return name


def parse_file(file_name) :
    chooseWord=input('Choose word: ')
    wordUpper=chooseWord.capitalize()
    with open(file_name,'r') as file :
        info=file.read()
        words=info.split()
        countWord=len([val for val in words if val.capitalize()==wordUpper or wordUpper in val.capitalize()])
        print(f'The word {chooseWord} occurs {countWord} times in this file')


if(__name__=="__main__") :
    parse_file(main())






