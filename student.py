
class Student:
    def __init__(self,stid,stName,stAge,stMajor,stGPA):
        self.__ID = stid
        self.__Name = stName
        self.__Age = stAge
        self.__Major = stMajor
        self.__GPA = stGPA
    
    def GetId(self): #
        return self.__ID
    def GetName(self): #
        return self.__Name
    def GetAge(self): #
        return self.__Age
    def GetMajor(self): #
        return self.__Major
    def GetGPA(self): #
        return self.__GPA   
    def SetName(self,NewName):
        self.__Name = NewName
    def SetAge(self,NewAge):
        self.__Age = NewAge
    def SetMajor(self,NewMajor):
        self.__Major = NewMajor
    def SetGPA(self,NewGpa):
        self.__GPA = NewGpa
    def SetId(self, newId):
        self.__ID = newId
    
    def Information(self):
        return("Student Name: " + self.__Name + "\n" + "Student ID: " + str(self.__ID) + "\n" + "Student Age: " + str(self.__Age) + "\n" + ("Student Major: " + self.__Major) + "\n" + "Student GPA: " + str(self.__GPA))

