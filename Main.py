from StudentDatabase import StudentDatabase
import time

def Main():
    SDBMS = StudentDatabase()
    flag = False
    print("WELCOME TO STUDENT RECORD MANAGEMENT SYSTEM")
    time.sleep(2)


    while flag == False:
        returnflag = False    
        print("WHAT WOULD YOU LIKE TO DO, CHOOSE FROM THE FOLLOWING OPTIONS:")
        time.sleep(1.5)
        print("1. ADD A NEW STUDENT")
        time.sleep(1)
        print("2. SEARCH FOR A STUDENT")
        time.sleep(1)
        print("3. DELETE A STUDENT")
        time.sleep(1)
        print("4. SHOW ALL STUDENTS")
        time.sleep(1)
        print("5. UPDATE INFORMATION")
        time.sleep(1)
        print("6. EXIT THE PROGRAM")        
        try:
            userinput = int(input("ENTER YOUR COMMAND: "))
            if userinput == 1:
                nameInput = input("ENTER THE NAME OF THE STUDENT: ")
                AgeInput = int(input("ENTER THE AGE OF THE STUDENT: "))
                majorInput = input("ENTER THE MAJOR OF THE STUDENT: ")
                GPAInput = float(input("ENTER THE GPA OF THE STUDENT: "))
                SDBMS.AddStudent(nameInput, AgeInput, majorInput, GPAInput)
                print("Successfully Added")
            elif userinput == 2:
                userID = int(input("ENTER THE ID OF THE STUDENT: "))
                stu_one = SDBMS.SearchStudent(userID)
                if stu_one == None:
                    print("THE STUDENT DOESN'T EXIST")
                else:
                    print(stu_one.Information())
            elif userinput == 3:
                userID = int(input("ENTER THE ID OF THE STUDENT: "))
                stu_two = SDBMS.RemoveStudent(userID)
                if stu_two == None:
                    print("THE STUDENT DOESN'T EXIST")
                else:
                    print("SUCCESSFULLY REMOVED")
            elif userinput == 4:
                temp = SDBMS.ReturnAllStudent()
                if not temp:
                    print("THERE ARE NO STUDENTS ADDED YET.")
                else:
                    for info in temp:
                        print(info.Information())
            elif userinput == 5:
                while returnflag == False:
                    validUserId = False
                    try:
                        userId = int(input("ENTER THE ID NUMBER FOR WHICH YOU WANT TO UPDATE: "))
                        validUserId = True
                        print("WHAT WOULD YOU LIKE TO DO, CHOOSE FROM THE FOLLOWING OPTIONS: ")
                        time.sleep(1)
                        print("1. NAME")
                        time.sleep(1)
                        print("2. ID")
                        time.sleep(1)
                        print("3. AGE")
                        time.sleep(1)
                        print("4. MAJOR")
                        time.sleep(1)
                        print("5. GPA")
                        time.sleep(1)
                        print("6. RETURN TO MAIN MENU")
                        time.sleep(1)
                        print("7. EXIT THE PROGRAM")
                        time.sleep(2)
                    except ValueError:
                        validUserId = False
                        print("ENTER A NUMBER")
                    if validUserId == True:
                        try:
                            userChoice = int(input("ENTER YOUR COMMAND: "))
                            if userChoice == 1:
                                nameUser = input("ENTER THE NEW NAME: ")
                                temp_one = SDBMS.UpdateName(userId, nameUser)
                                if temp_one == None:
                                    print("THE STUDENT DOESN'T EXIST")
                                else:
                                    print(temp_one.Information())
                            elif userChoice == 2:
                                idUser = int(input("ENTER THE NEW ID: "))
                                temp_two = SDBMS.UpdateId(userId, idUser)
                                if temp_two == None:
                                    print("THE STUDENT DOESN'T EXIST OR NEW ID ALREADY EXISTS")
                                else:
                                    print(temp_two.Information())
                            elif userChoice == 3:
                                ageUser = int(input("ENTER THE NEW AGE: "))
                                temp_three = SDBMS.UpdateAge(userId,ageUser)
                                if temp_three == None:
                                    print("THE STUDENT DOESN'T EXIST")
                                else:
                                    print(temp_three.Information())
                            elif userChoice == 4:
                                MajorUser = input("ENTER THE NEW MAJOR: ")
                                temp_four = SDBMS.UpdateMajor(userId,MajorUser)
                                if temp_four == None:
                                    print("THE STUDENT DOESN'T EXIST")
                                else:
                                    print(temp_four.Information())
                            elif userChoice == 5:
                                GPAUser = float(input("ENTER THE NEW GPA: "))
                                temp_five = SDBMS.UpdateGPA(userId, GPAUser)
                                if temp_five == None:
                                    print("THE STUDENT DOESN'T EXIST")
                                else:
                                    print(temp_five.Information())
                            elif userChoice == 6:
                                returnflag = True
                                print("SUCCESSFUL")
                            elif userChoice == 7:
                                flag = True
                                print("SUCCESSFULLY EXITED")
                            else:
                                print("INVALID INPUT: RUN CODE AGAIN")
                        except ValueError:
                            print("ENTER A NUMBER")
            elif userinput == 6:
                flag = True
                print("SUCCESSFULLY EXITED")
            else:
                print("INVALID INPUT: RUN CODE AGAIN")
        except ValueError:
            print("ENTER A NUMBER")

            
                
if __name__ == "__main__":
    Main()
