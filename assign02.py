import csv


def enterFile() :
    fileName=input('Please enter the data file: ')
    print("")
    readFile(fileName)


def readFile(name) :
    with open(name) as file :
        reader=csv.DictReader(file)
        data=list(reader)
        #getting all comm_rates as a list
        comm_rates =[float(val['comm_rate']) for val in data]
        findAverage(comm_rates)
        findMax(comm_rates,data)
        findMin(comm_rates, data)
        

def findAverage(comm_rates) :
     avCommRate=sum(comm_rates)/len(comm_rates)
     print(f'The average commercial rate is: {avCommRate}\n')

def findMax(comm_rates,allData) :
     maxCommRate=str(max(comm_rates))
     #searching for the first dictionary with maximum value above
     maxCompany=[val for val in allData if val['comm_rate']==maxCommRate][0]
     print('The highest rate is:')
     print(f"{maxCompany['utility_name']} ({maxCompany['zip']}, {maxCompany['state']}) - ${maxCommRate}\n")

def findMin(comm_rates,allData) :
     minCommRate=min(comm_rates)
     #searching for the first dictionary with manimum value above
     minCompany=[val for val in allData if float(val['comm_rate'])==minCommRate][0]
     print('The lowest rate is:')
     print(f"{minCompany['utility_name']} ({minCompany['zip']}, {minCompany['state']}) - ${minCommRate}")


enterFile()


    