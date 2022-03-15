class  NegativeNumberError(Exception) :
    pass


def get_inverse(n:int) :
    if type(n)!=int :
        raise ValueError
    if n==0 :
        raise ZeroDivisionError
    
    if n<0 :
        raise NegativeNumberError
    
    return 1/n


def main() :
    try :
        num=int(input("Enter a number: "))
        inverse=get_inverse(num)
        print(inverse)
    except ValueError :
        print('Error: The value must be a number')
    except ZeroDivisionError :
        print('Error: Cannot divide by zero')
    except NegativeNumberError :
        print('Error: The value cannot be negative')


if __name__ == "__main__":
    main()

