class Robot :
    def __init__(self,x,y,fuel) :
        self.x=x
        self.y=y
        self.fuel=fuel
    
    def left(self) :
        if(self.fuel-5 >= 0) :
            self.x-=1
            self.fuel-=5
        else :
            print('Insufficient fuel to perform action') 

    def right(self) :
         if(self.fuel-5 >= 0) :
             self.x+=1
             self.fuel-=5
         else :
             print('Insufficient fuel to perform action') 

    def up(self) :
      if(self.fuel-5 >= 0) :
            self.y-=1
            self.fuel-=5
      else :
           print('Insufficient fuel to perform action')    

    def down(self) :
         if(self.fuel-15 >= 0) :
             self.y+=1
             self.fuel-=5
         else :
              print('Insufficient fuel to perform action')  

    def fire(self) :
         if(self.fuel-15 >= 0) :
             print('Pew! Pew!')
             self.fuel-=15
         else :
              print('Insufficient fuel to perform action')

    def status(self) :
        print(f'({self.x}, {self.y}) - Fuel: {self.fuel}')


def runCommands(obj) :
    command=input('Enter command: ')
    if(command=='quit') :
        print('Goodbye.')
    elif(command=='left') :
        obj.left()
        runCommands(obj)
    elif(command=='right') :
        obj.right()
        runCommands(obj)
    elif(command=='down') :
        obj.down()
        runCommands(obj)
    elif(command=='up') :
        obj.up()
        runCommands(obj)
    elif(command=='fire') :
        obj.fire()
        runCommands(obj)
    elif(command=='status') :
        obj.status()
        runCommands(obj)
    else :
        runCommands(obj)


def main() :
    robotObj=Robot(10, 10, 100)
    runCommands(robotObj)



if __name__ == "__main__":
    main()
