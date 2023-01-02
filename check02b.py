fileName=input('Enter file: ')
with open(fileName,'r') as file :
    info=file.read()
    words=len(info.split())
    # move the cursor back to the beginning
    file.seek(0)
    lines=0
    #count the number of lines
    for line in file :
        #if line is not empty
        if line!="\n" :
            lines+=1
    
    print(f"The file contains {lines} lines and {words} words.")