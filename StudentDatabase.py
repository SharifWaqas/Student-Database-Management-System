from student import Student
class StudentDatabase():
    def __init__(self):
        self.__StudentDatabase = []
        self.__OldId = 1000

    def SearchStudent(self,id):
        for index in range(len(self.__StudentDatabase)):
            studentObject = self.__StudentDatabase[index]
            idLst = studentObject.GetId()
            if idLst == id:
                return studentObject
        return None

    def AddStudent(self,name,age,major,gpa):
        temp = Student(self.__OldId,name,age,major,gpa)
        self.__OldId += 1
        self.__StudentDatabase.append(temp)
        return temp

    def ReturnAllStudent(self):
        return self.__StudentDatabase
    
    def RemoveStudent(self,id):
        for index in range(len(self.__StudentDatabase)):
            studentObject = self.__StudentDatabase[index]
            idLst = studentObject.GetId()
            if idLst == id:
                del self.__StudentDatabase[index]
                return (studentObject)       
        return None

    def UpdateId(self, oldId, newId):
        for index in range(len(self.__StudentDatabase)):
            studentObject = self.__StudentDatabase[index]
            idLst = studentObject.GetId()
            if idLst == oldId:
                if oldId == newId:
                    return studentObject
                else:
                    for i in range(len(self.__StudentDatabase)):
                        databaseid = self.__StudentDatabase[i].GetId()
                        if databaseid == newId:
                            return None
                        
                    studentObject.SetId(newId) 
                    return studentObject
        return None


    def UpdateMajor(self,oldId, newMajor):
        for index in range(len(self.__StudentDatabase)):
            studentObject = self.__StudentDatabase[index]
            idLst = studentObject.GetId()
            if idLst == oldId:
                studentObject.SetMajor(newMajor)
                return studentObject
        return None

    def UpdateName(self,oldId, newName):
        for index in range(len(self.__StudentDatabase)):
            studentObject = self.__StudentDatabase[index]
            idLst = studentObject.GetId()
            if idLst == oldId:
                studentObject.SetName(newName)
                return studentObject
        return None   

    def UpdateGPA(self, oldId, newGPA):
        for index in range(len(self.__StudentDatabase)):
            studentObject = self.__StudentDatabase[index]
            idLst = studentObject.GetId()
            if idLst == oldId:
                studentObject.SetGPA(newGPA)
                return studentObject
        return None

    def UpdateAge(self, oldId, newAge):
        for index in range(len(self.__StudentDatabase)):
            studentObject = self.__StudentDatabase[index]
            idLst = studentObject.GetId()
            if idLst == oldId:
                studentObject.SetAge(newAge)
                return studentObject
        return None
