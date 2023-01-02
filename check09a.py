def main() :
    try :
        num=int(input("Enter a number: "))
        print(f'The result is: {num*2}')
    except ValueError as err :
        print('The value entered is not valid')
        main()


if __name__ == "__main__":
    main()
