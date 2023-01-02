x=[1,2,18,7,3,4,5,6]
def sort(numbers):
    """
    Fill in this method to sort the numbers of numbers
    """
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i-1
        while j >=0 and key < numbers[j] :
                numbers[j+1] = numbers[j]
                j -= 1
        numbers[j+1] = key
    
   


sort(x)
print(x)