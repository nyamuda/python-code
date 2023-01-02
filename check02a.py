def prompt_number() :
    num=int(input('Enter a positive number: '))
   
    if(num<0) :
        print('Invalid entry. The number must be positive.')
        return prompt_number()
    else :
        return num


def compute_sum(a,b,c) :
    return a+b+c

def main() :
    one=prompt_number()
    print("")
    two=prompt_number()
    print("")
    three=prompt_number()
    print("")
    print(f'The sum is: {compute_sum(one, two, three)}')


if __name__ == "__main__":
    main()