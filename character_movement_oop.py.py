
class Character:
    def __init__(self,Name,XPosition,YPosition):
        self.__Name=Name#STRING
        self.__xposition=XPosition#INTEGER
        self.__yposition=YPosition#INTEGER
    def getname(self):#gets name
        return self.__Name
    def GetXPosition(self):#gets x postion
        return self.__xposition
    def GetYPosition(self):#gets y postion
        return self.__yposition
    def SetXPosition(self,value):
        self.__xposition=self.__xposition+value
        if self.__xposition>10000:
            self.__xposition=10000
        elif  self.__xposition<0:
             self.__xposition=0
    def SetYPosition(self,value):
        self.__yposition=self.__yposition+value
        if self.__yposition>10000:
            self.__yposition=10000
        elif self.__yposition<0:
             self.__yposition=0
    def Move(self,Direction):
        if Direction=="up":
            self.SetYPosition(10)
        elif Direction=="down":
            self.SetYPosition(-10)
        elif Direction=="right":
            self.SetXPosition(10)
        elif Direction=="left":
            self.SetXPosition(-10)
#inheritance used to use features of parent class(meaning class declared in the position) in child class
#whenever you want to use this you have to use super,super is a subroutine that provides access to methods of parent class
class BikeCharacter(Character):
    def __init__(self,Name,XPosition,YPosition):
        super().__init__(Name,XPosition,YPosition)#gets parameters of parent class,so we can use methods related to these parameters   
    def Move(self, Direction):
        if Direction=="up":
            super().SetYPosition(20)
        elif Direction=="down":
                    super().SetYPosition(-20)
        elif Direction=="right":
                    super().SetXPosition(20)
        elif Direction=="left":
                    super().SetXPosition(-20)
    
#argument sent from main program to subroutine   
#when a base class method overrides a parent class method it is called polymorphism
#same name method exists in parent class
            #main
Jack=Character("Jack",50,50)
Karla=BikeCharacter("Karla",100,50)

choice=input("Which Character would you like to move ").lower()
while choice!="jack" and choice!="karla":
     choice=input("Which Character would you like to move ").lower()
newdirection=input("which direction would you like to move ").lower()
while newdirection!="up" and newdirection!="down" and newdirection!="left" and newdirection!="right":
     newdirection=input("which direction would you like to move ").lower()
if choice=="jack":
    Jack.Move(newdirection)
    print("Jack's y position is",Jack.GetYPosition(),"Jack's x position is",Jack.GetXPosition())
elif choice=="karla":
     Karla.Move(newdirection)
     print("Karla's y position is",Karla.GetYPosition(),"Karla's x position is",Karla.GetXPosition())

        


           
    
    
       
