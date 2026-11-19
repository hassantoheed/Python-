class myclass:#class
    def __init__(self,name,age,gender):#constructor
        self._name=name
        self._age=age
        self._gender=gender
    #Methods
    def getname(self):#Getter method,gets the value of name
        return self._name
    def setname(self,newname):#Setter method,updates the value of name
        self._name=newname
        return self._name
    def getage(self):#Getter method,gets the value of age
        return self._age
    def setage(self,newage):#Setter method,updates the value of age
        self._age=newage
        return self._age
    def getgender(self):#Getter method,gets the value of gender
        return self._gender
    def setgender(self,newgender):#Setter method,updates the value of gender
        self._gender=newgender
        return self._gender
Teacher=myclass("Hassan",23,"Male")#teacher is object of class myclass
print(Teacher.getname())
print(Teacher.setname("Zohair"))
print(Teacher.getname())
print(Teacher.getage())
print(Teacher.setage(34))
print(Teacher.getgender())
print(Teacher.setgender("Female"))
      