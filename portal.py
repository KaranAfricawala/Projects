
import random

class Account:
    # implements class account here
    __userData={}               #It will store username and password
    __userStudentAccount={}     #It will store username and corresponding its student Account object for login 
    def __init__(self,username="",password=""):
        Account.__userData[username]=password

    @staticmethod
    def get_user_student_account(username):
        return Account.__userStudentAccount[username]

    @staticmethod
    def set_user_student_account(username, student):
        Account.__userStudentAccount[username]=student

    @staticmethod
    def createAccount(username, password):
        Account.__userData[username]=password
    
    @staticmethod
    def get_user_data():
        return Account.__userData
    
    #It will check login credentials whether username or password is correct or not 
    def checkLogin(self, username, password):
        if (username in Account.__userData.keys()):
            if (password == Account.__userData[username]):
                return True
        return False
    
    #It will check username exist or not 
    def checkUsername(self,username):
        return username in Account.get_user_data().keys()
class Course:
    def __init__(self, name, code, unit):
        self._courseName = name
        self._courseCode = code
        
        self._courseUnit = unit

    def getCourseName(self):
        return self._courseName

    def getCourseCode(self):
        return self._courseCode

    def getCourseUnit(self):
        return self._courseUnit


class TakenCourse(Course):
    # implements class TakenCourse
    def __init__(self, collegeCourse, semester, grade=0):
        name = collegeCourse.getCourseName()
        code = collegeCourse.getCourseCode()
        unit = collegeCourse.getCourseUnit()
        super().__init__(name, code, unit)

        self.__semester = semester
        self.__grade = grade
    def getGrade(self):
        return self.__grade
    
    def getSemester(self):
        return self.__semester
    
    def printCourse(self,number, reason):
        if (reason.lower() == "course"):
            if self.getSemester().isCurrentSemester():
                print("    %d)   %s: %s [Current semester]" % (number, self._courseCode, self._courseName))
            else:
                print("    %d)   %s: %s " % (number, self._courseCode, self._courseName))
        elif(reason.lower() == "transcript"):
            if self.getSemester().isCurrentSemester():
                print("    %d)   %s: %s: %d [Current semester]" % (number, self._courseCode, self._courseName, self.__grade))
            else:
                print("    %d)   %s: %s: %d " % (number, self._courseCode, self._courseName, self.__grade))
class CollegeCourse(Course):
    # implements and complete class CollegeCourse
    def __init__(self, name, code, unit):
        super().__init__(name, code, unit)
        self._courseUnit = unit

    def printCourse(self):
        print("Course Name: %s | Course Code: %s | Course Unit %d \n" % (self._courseName, self._courseCode, self._courseUnit))
    

class Student:
    # implements class student here
    def __init__(self, studentProfile, admissionYear=2018):
        self._admissionYear = admissionYear
        self._admissionSemester = 1  # Suppose each student starts in semester 1 of the admission year
        self._generalTranscript = GeneralTranscript()
        self._semesterTranscript = CurrentSemesterTranscript()
        self._studentProfile = studentProfile

    def get_student_profile(self):
        return self._studentProfile
    
    #To Display First name and Last name based on Gender
    def displayName(self):
        print()
        print()
        
        if (self.get_student_profile().get_gender().lower() == "m"):
            temp="Mr."
        else:
            temp="Ms."
        print("Hi "+temp+" "+self.get_student_profile().get_first_name()+" "+self.get_student_profile().get_last_name()+",")
    
    def getAdmissionYear(self):
        return self._admissionYear
    
    def getAdmissionSemester(self):
        return self._admissionSemester
    
    def semesterNumber(self):
        currentYear=Portal.getCurrentSemester().getYear()
        currentSemester=Portal.getCurrentSemester().getSemesterNo()
        studentSemester=self.getAdmissionSemester()
        studentYear=self.getAdmissionYear()
        semester=1
        while currentYear!=studentYear and currentSemester!=studentSemester:
            studentSemester+=1
            if studentSemester>2:
                studentSemester=1
                studentYear+=1
            studentSemester+=1   
            semester+=1
        return semester
    #Enrollment Certificate for student
    def getEnrollmentCertificate(self):
        q=""
        print()
        print()
        
        if (self.get_student_profile().get_gender().lower() == "m"):
            temp="Mr."
            q="He"
        else:
            temp="Ms."
            q="She"
        print("Dear Sir/Madam,")
        print()
        print("This is to certify that "+temp+" "+self.get_student_profile().get_first_name()+" "+self.get_student_profile().get_last_name()+
              " with student id "+str(self.get_student_profile().get_studen_Id())+" is a student at semester "+str(self.semesterNumber())+" at Columbia. ")
        print(q+" was admitted to our college in "+str(self.getAdmissionYear())+" and has taken "+str(self.getGTranscript().totalCourses())+
              " course(s) so far."
              +" Currently "+q.lower()+" resides at "+self.get_student_profile().get_address()+", "+self.get_student_profile().get_country())
        print()
        print("If you have any question, please don't hesitate to contact us.")
        print("Thanks,")
        print("[Manager: "+Manager.get_first_name()+" "+Manager.get_last_name()+" ]")
    
    
    #Display All courses which are taken by student
    def getMyCourses(self):
        self.displayName()
        print("You have taken the following courses so far:")   
        self.getGTranscript().printTranscript("Course")
    
    #Display Transcript of student with its general and current Semester GPA
    def getMyTranscript(self):
        self.displayName()
        print("Here is your general transcript:")
        print()
        self.getGTranscript().printTranscript("Transcript")
        print("     YOUR GPA IS: %.2f"%(self.getGTranscript().getGPA()))
        print()
        print("Here is your current semester transcript:")
        self.getSTranscript().printTranscript("Transcript")
        print("     YOUR Current Semester GPA IS: %.2f"%(self.getSTranscript().getGPA()))
     
    #display courses which is taken by current student
    def getCourseTaken(self):
        takenCourse=""
        for i in range(self.getGTranscript().totalCourses()-1):
            takenCourse+=self.getGTranscript().returnCourseTaken(i)+","
        if i<self.getSTranscript().totalCourses():
            takenCourse+=self.getGTranscript().returnCourseTaken(i)
        i=0
        for i in range(self.getSTranscript().totalCourses()-1):
            takenCourse+=self.getSTranscript().returnCourseTaken(i)+"[Current semester] ,"
        if i<self.getSTranscript().totalCourses():
            takenCourse+=self.getSTranscript().returnCourseTaken(i)+"[Current semester]"
        return takenCourse
    
    #display Overall and CurrentSemester GPA of Student
    def getMyGPA(self):
        self.displayName()
        GPA=self.getGTranscript().getGPA()
        print("     YOUR overall GPA IS: %.2f"%(GPA))
        GPA=self.getSTranscript().getGPA()
        print("     YOUR Current Semester GPA IS: %.2f"%(GPA))
    
    #Register Student for new course with the course and semester 
    def registerCourse(self, collegeCourse, semester, grade=0):
        course = TakenCourse(collegeCourse, semester, grade)
        semester._setIfCurrentSemester()
        if semester.isCurrentSemester():
            self._semesterTranscript.addCourse(course)
            self._generalTranscript.addCourse(course)
        else:
            self._generalTranscript.addCourse(course)
    def getGTranscript(self):
        return self._generalTranscript

    def getSTranscript(self):
        return self._semesterTranscript

class StudentProfile:
    # implements class student here
    __studentId=10000000
    def __init__(self, firstName, lastName, gender, address, country, age, studentid=0):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__gender = gender
        self.__country = country
        self.__address=address
        if(studentid != 0):
            self.__studentId = studentid
        else:
            self.__studentId=StudentProfile.__studentId+1
        StudentProfile.__studentId+=1
        self.__age=age
    
    #To display profile of Student for Option 8
    def displayProfile(self):
        if (self.get_gender().lower() == "m"):
            temp="Mr."
        else:
            temp="Ms."
            
        print("Name: %s"%(temp+" "+self.get_first_name()+" "+self.get_last_name()))
        print("StudentId: %s"%(self.get_studen_Id()))
        print("Gender: %s"%(self.get_gender()))
        print("Address: %s"%(self.get_address()))
        print("Country of Origin: %s"%(self.get_country()))
        print("Age: %s"%(self.get_age()))

    def get_first_name(self):
        return self.__firstName

    def get_last_name(self):
        return self.__lastName
   
    def get_gender(self):
        return self.__gender
    
    def get_address(self):
        return self.__address

    def get_country(self):
        return self.__country

    def get_studen_Id(self):
        return self.__studentId

    def get_age(self):
        return self.__age

class Transcript:
    # implements class transcript here
    def __init__(self):
        self._allTakenCourses = []

    def addCourse(self, takenCourse):
        self._allTakenCourses.append(takenCourse)
    
    # complete this method
    def totalCourses(self):
        return len(self._allTakenCourses)
    
    #It will return the String of All courses within its code for Student Profile
    def returnCourseTaken(self,i):
        courses=""
        c=self._allTakenCourses[i]
        courses+=c.getCourseCode()+": "+c.getCourseName()
        return courses
    
    def bothEqual(self,course,c):
        return (course.getCourseName()==c.getCourseName() and course.getCourseCode()==c.getCourseCode() and course.getCourseUnit()==c.getCourseUnit())
        
    #It will return Semester number of course taken. If not taken then 0
    def getSemesterOfCourse(self, course):
        for i in range(len(self._allTakenCourses)):
            c=self._allTakenCourses[i]
            if self.bothEqual(course,c):
                return c.getSemester().getSemesterNo()
        return 0
    #It will print All courses taken by student in desired order
    def printTranscript(self, reason):
        for i in range(len(self._allTakenCourses)):
            c=self._allTakenCourses[i]
            c.printCourse(i+1,reason)
class GeneralTranscript(Transcript):
    # implements class GeneralTranscript here
    def __init__(self):
        super().__init__()
        
    #It will return GPA of All taken Course for All Semester
    def getGPA(self):
        GPA=0
        total=0
        for i in range(len(self._allTakenCourses)):
            c=self._allTakenCourses[i]
            unit=c.getCourseUnit()
            total+=unit
            GPA+=c.getGrade()*unit
        if(total>0):
            GPA=GPA/total
        return GPA
class CurrentSemesterTranscript(Transcript):
    # implements class CurrentSemesterTranscript here
    def __init__(self):
        super().__init__()
    
    #It will return GPA of All taken Course for Current Semester
    def getGPA(self):
        GPA=0
        total=0
        for i in range(len(self._allTakenCourses)):
            c=self._allTakenCourses[i]
            unit=c.getCourseUnit()
            total+=unit
            GPA+=c.getGrade()*unit
        if(total>0):
            GPA=GPA/total
        return GPA
class Manager:
    __firstName=""
    __lastName=""
    __title=""
    def __init__(self, firstName="Peter", lastName="Jackson", title="Manager"):
        Manager.__firstName = firstName
        Manager.__lastName = lastName
        Manager.__title = title
            
    @staticmethod
    def get_first_name():
        return Manager.__firstName
    @staticmethod
    def get_last_name():
        return Manager.__lastName
    @staticmethod
    def get_title():
        return Manager.__title

class Semester:
    # implements class Semester here
    def __init__(self, semesterNo, year):
        self._semesterNo = semesterNo
        self._year = year
        self._setIfCurrentSemester()

    def getYear(self):
        return self._year

    def getSemesterNo(self):
        return self._semesterNo

    # checks whether the semester object is representing current semester or not. Suppose, current semester is year = 2019, semester = 2
    def _setIfCurrentSemester(self):
        currentSemester = 1
        currentYear = 2020

        if (self._semesterNo == currentSemester) and (self._year == currentYear):
            self._isCurrentSemester = True
        else:
            self._isCurrentSemester = False

    def isCurrentSemester(self):
        return self._isCurrentSemester

    def printSemester(self):
        print("Year: %d Semester%d isCurrent %d" % (self._year, self._semesterNo, self._isCurrentSemester))

class Menu:
    #display menu for option 11 from Main menu
    def displayElevenMenu(self):
        print("************************************************************")
        print("Welcome to Extra features of Application:")
        print("************************************************************")
        print("--[1] Print the list of all students based on their GPA (Ascendingly)")
        print("--[2] Print the list of names of all students alphabetically")
        print("--[3] Print the list of all Male students")
        print("--[4] Print the list of all Female students")
        print("--[5] List of top (highest GPA) male and female students")
        print("--[6] Back to the previous menu")
        print("************************************************************")
        print()
        
    def displayMenu(self):
        print("************************************************************")
        print("Select from the options:")
        print("************************************************************")
        print("--[1] Print my enrolment certificate")
        print("--[2] Print my courses")
        print("--[3] Print my transcript")
        print("--[4] Print my GPA")
        print("--[5] Print my ranking among all students in the college")
        print("--[6] List all available courses")
        print("--[7] List all students")
        print("--[8] Show My Profile")
        print("--[9] Logout")
        print("--[10] Exit")
        print("--[11] Bonus")
        print("************************************************************")
        print()
    def callChoice(self):
        choice=""
        while(not choice.isdigit()):
            choice=input("Enter the number corresponding to each item to proceed: ")
        return int(choice)
class Portal:
    _currentSemester = Semester(1, 2020)  # Static/class property. Suppose the current semester is second semester 2019
    def __init__(self):
        self._collegeCourses = []
        self._registeredStudents = []

    # use this method to register a student
    def registerStudent(self, student):
        self._registeredStudents.append(student)
    
    def updatManager(self,firstName,lastName,title):
        Manager(firstName,lastName,title)
    
    #Eleven Option of Application
    
    #Option 11, Extra feature of application for student
    def elevenOption(self, menu):
        choice=0
        while choice!=6:
            menu.displayElevenMenu()
            choice=menu.callChoice()
            if choice == 1:
                self.getAllStudentByGPA()
            elif choice==2:
                self.getAllStudentByName()
            elif choice==3:
                self.getAllGenderStudent("Male")
            elif choice==4:
                self.getAllGenderStudent("Female")
            elif choice==5:
                self.topMaleNFemaleStudent()
            elif choice==6:
                break
            else:
                print("You have not entered correct option..")
            if choice<=5:
                input()
                
    # display rank and GPA of student object which is passed in this method
    def getRankNGPA(self, student):
        rank=len(self._registeredStudents)
        GPA=student.getGTranscript().getGPA()
        for current in self._registeredStudents:
            if GPA>current.getGTranscript().getGPA():
                rank-=1
        student.displayName()
        print("Your overall GPA is %2f and therefore your rank is %d."%(GPA,rank))  
         
    #Display All courses which is offered by College  
    def getAllCourses(self, student):
        for i in range(len(self._collegeCourses)):
            course=self._collegeCourses[i]
            takenSemester=student.getGTranscript().getSemesterOfCourse(course)
            if takenSemester>0:
                taken="Taken at semester "+str(takenSemester)
            else:
                taken="Not taken"
            print("%d)   %s: %s: %d units [%s]" % (i+1, course.getCourseCode(), course.getCourseName(),course.getCourseUnit(),taken))
    
    def countGender(self, requiredGender):
        count=0
        for i in range(len(self._registeredStudents)):
            student=self._registeredStudents[i]
            gender=student.get_student_profile().get_gender()
            if gender.lower() in [requiredGender[0].lower()]:
                count+=1
        return count
    def topMaleNFemaleStudent(self):
        male=False
        female=False
        self._registeredStudents.sort(key=lambda x:x.getGTranscript().getGPA(), reverse=False)
        for i in range(len(self._registeredStudents)):
            student=self._registeredStudents[i]
            firstName=student.get_student_profile().get_first_name()
            lastName=student.get_student_profile().get_last_name()
            gender=student.get_student_profile().get_gender()
            GPA=student.getGTranscript().getGPA()
            if not male and gender.lower() in ["m"]:
                print("Top (highest GPA) Male student")
                print("%d)   %s %s: %s : %d" % (1, firstName, lastName,gender, GPA))
                male=True
                print()
            if not female and gender.lower() in ["f"]:
                print("Top (highest GPA) Female student")
                print("%d)   %s %s: %s : %d" % (1, firstName, lastName, gender, GPA))
                female=True
                print()
            if male and female:
                break
    def getAllGenderStudent(self, requiredGender):
        count=self.countGender(requiredGender)
        print("There are %d %s students in Columbia College as following:"%(count,requiredGender))
        number=1
        for i in range(len(self._registeredStudents)):
            student=self._registeredStudents[i]
            firstName=student.get_student_profile().get_first_name()
            lastName=student.get_student_profile().get_last_name()
            studentId=student.get_student_profile().get_studen_Id()
            gender=student.get_student_profile().get_gender()
            if gender.lower() in [requiredGender[0].lower()]:
                print("%d)   %s %s: %s" % (number, firstName, lastName,studentId))
                number+=1
    def getAllStudentByName(self):
        print("There are %d students based on their Name Alphabetically in Columbia College as following:"%(len(self._registeredStudents)))
        self._registeredStudents.sort(key=lambda x:x.get_student_profile().get_first_name()+" "+x.get_student_profile().get_last_name(), reverse=False)
        for i in range(len(self._registeredStudents)):
            student=self._registeredStudents[i]
            firstName=student.get_student_profile().get_first_name()
            lastName=student.get_student_profile().get_last_name()
            studentId=student.get_student_profile().get_studen_Id()
            print("%d)   %s %s: %d" % (i+1, firstName, lastName,studentId))
    
    def getAllStudentByGPA(self):
        print("There are %d students based on their GPA(Ascendingly) in Columbia College as following:"%(len(self._registeredStudents)))
        self._registeredStudents.sort(key=lambda x:x.getGTranscript().getGPA(), reverse=False)
        for i in range(len(self._registeredStudents)):
            student=self._registeredStudents[i]
            firstName=student.get_student_profile().get_first_name()
            lastName=student.get_student_profile().get_last_name()
            GPA=student.getGTranscript().getGPA()
            print("%d)   %s %s: %d" % (i+1, firstName, lastName,GPA))
    
    #Display list of students who is registered with the college in given format
    def getAllStudent(self):
        print("There are %d students in Columbia College as following:"%(len(self._registeredStudents)))
        for i in range(len(self._registeredStudents)):
            student=self._registeredStudents[i]
            firstName=student.get_student_profile().get_first_name()
            lastName=student.get_student_profile().get_last_name()
            studentId=student.get_student_profile().get_studen_Id()
            print("%d)   %s %s: %s" % (i+1, firstName, lastName,studentId))
    
    def addCourse(self, collegeCourse):
        self._collegeCourses.append(collegeCourse)
    
    
    #Register Menu for Student
    def registerMenu(self):
        print("*******************************************")
        print("Welcome to Columbia College: Please Register ")
        print("*******************************************")
        firstName=input("Please enter your first name: ")
        lastName=input("Please enter your last name: ")
        gender=""
        while not (gender.lower() in ["m","f","o"]):
            gender=input("Please enter your gender [M/F/O]: ")
        address=input("Please enter your address: ")
        country=input("Please enter your country of origin: ")
        admissionYear=""
        while(not admissionYear.isdigit()):
            admissionYear=input("Please enter the year of admission: ")
        age=""
        while(not age.isdigit()):
            age=input("Please enter your age: ")
        print()
        username=""
        while not (len(username)>=6 and username.isalpha()):
            username=input("Please enter a username [At least 6 characters]: ")
        password=""
        while not (len(password)>=6 and self.hasNumbers(password)):
            password=input("Please enter a password [At least 6 characters with at least one digit]: ")
        
        newStudentProfile = StudentProfile(firstName, lastName,gender,address, country, int(age))
        newStudent = Student(newStudentProfile, int(admissionYear))
        self.addRandomCoursesToStudent(newStudent)
        print()
        print()
        print("Thanks, your account and profile has been created successfully. Welcome Aboard %s %s"%(newStudentProfile.get_first_name(),newStudentProfile.get_last_name()))
        
        Account.createAccount(username, password)
        self.registerStudent(newStudent)
        Account.set_user_student_account(username, newStudent)
        self.addRandomCoursesToStudent(newStudent)
        return newStudent
    def hasNumbers(self, inputString):
        return any(char.isdigit() for char in inputString)
    
    #Log in Manu for Student
    def loginMenu(self):
        print("*******************************************")
        print("Please enter your account to login:")
        print("*******************************************")
        print("Username: ")
        print("Password: ")
        print()
        print("-------------------------------------------")
        
        print("Not registered yet? Type \"Register\" and press enter to start the registration process!")
        register=input()
        if register.lower()=="register":
            return self.registerMenu()
        else:
            username=register
            password=input()
            account=Account()
            if account.checkLogin(username, password):
                print("************************************************************")
                print("Welcome to Genisis College!")
                print("************************************************************")
                return Account.get_user_student_account(username)
            print("************************************************************")
            print("Your account does not exist. Please try again!")
            print("************************************************************")
            return None
    
    def studentProfile(self,student):
        student.get_student_profile().displayProfile()
        print("Year of Admission: %d"%(student.getAdmissionYear()))
        print("Overall GPA: %2f"%(student.getGTranscript().getGPA()))
        courseTaken=student.getCourseTaken()
        print("Courses Taken So far: %s"%(courseTaken))
        
    # class this method to add some random courses to a student - You don't need to understand how this method works. Just call it and it will add some courses
    # to the student and to different semesters
    def addCoursesToStudent(self, student, course, semesterNo, year, grade):
        for c in self._collegeCourses:
            if course == c.getCourseName():
                semester = Semester(semesterNo, year)
                student.registerCourse(c, semester, grade)
                
    def addRandomCoursesToStudent(self, student):
        for course in self._collegeCourses:
            rand = random.uniform(0, 1)
            admissionYear = student.getAdmissionYear()
            currentSemester = Portal.getCurrentSemester()

            if currentSemester.getYear() == admissionYear:
                numberOfSemesterBetweenCurrentSemesterAndAdmission = currentSemester.getSemesterNo()
            else:
                numberOfSemesterBetweenCurrentSemesterAndAdmission = 2 * (currentSemester.getYear() - admissionYear) + currentSemester.getSemesterNo()

            randomSemster = random.randint(1, numberOfSemesterBetweenCurrentSemesterAndAdmission)

            year = randomSemster // 2
            semesterNo = (randomSemster % 2) + 1
            semester = Semester(semesterNo, student.getAdmissionYear() + year)

            randomGrade = random.randint(30, 100)

            if rand <= .5:
                student.registerCourse(course, semester, randomGrade)
    # static/class method
    @staticmethod
    def getCurrentSemester():
        currentSemester = Semester(1, 2020)  # Static/class property. Suppose the current semester is first semester 2020
        return currentSemester


class PortalManager:
    def __init__(self):
        self._portal = Portal()

    def createATestPortal(self):

        # create all courses offered
        self._createAllCollegeCourses()
        
        #create a Managaer for College
        Manager()

        # create a sample student For test the code
        self.createASampleStudent()
        
        exitFlag=False
        while not exitFlag:    
            #login student
            login=False
            while not login:
                #Login Menu for student
                student=self._portal.loginMenu()
                if student == None:
                    input()
                    continue
                input()
                
                #Menu diplay and selection of choice
                menu=Menu()
                choice=0
                while choice<=8 or choice==11:
                    menu.displayMenu()
                    choice=menu.callChoice()
                    if choice == 1:
                        student.getEnrollmentCertificate()
                    elif choice==2:
                        student.getMyCourses()
                    elif choice==3:
                        student.getMyTranscript()
                    elif choice==4:
                        student.getMyGPA()
                    elif choice==5:
                        self._portal.getRankNGPA(student)
                    elif choice==6:
                        self._portal.getAllCourses(student)
                    elif choice==7:
                        self._portal.getAllStudent()
                    elif choice==8:
                        self._portal.studentProfile(student)
                    elif choice==9:
                        login=True
                    elif choice==11:
                        self._portal.elevenOption(menu)
                    elif choice==10:
                        exitFlag=True
                        print()
                        print()
                        print("----------------------THE END---------------------")
                    else:
                        print("You have Entered wrong option.........")
                        print()
                    if choice<=8:
                        input()
                if  exitFlag:
                    break      
    
    
    
    #create a sample student and assign them to random course
    def createASampleStudent(self):
        sampleStudentProfile = StudentProfile("Peter", "Sand", "M", "Vancouver", "Irland", 21, 8012321)
        student = Student(sampleStudentProfile, 2019)
        Account.createAccount("Student1", "111111")
        self._portal.registerStudent(student)
        Account.set_user_student_account("Student1", student)
        self._portal.addCoursesToStudent(student, "Python", 1, 2019, 80)
        self._portal.addCoursesToStudent(student, "Object-Oriented Programming", 2, 2019, 76)
        self._portal.addCoursesToStudent(student, "Problem Solving", 1, 2020, 67)
        self._portal.addCoursesToStudent(student, "Project Management", 1, 2019, 82)
        self._portal.addCoursesToStudent(student, "Java Programming", 2, 2019, 73)
        
        sampleStudentProfile = StudentProfile("Sheila", "Rogers", "F", "Surrey", "India", 19, 8014525)
        student = Student(sampleStudentProfile, 2018)
        Account.createAccount("Student2", "222222")
        self._portal.registerStudent(student)
        Account.set_user_student_account("Student2", student)
        self._portal.addCoursesToStudent(student, "Python", 1, 2018, 65)
        self._portal.addCoursesToStudent(student, "Object-Oriented Programming", 2, 2018, 67)
        self._portal.addCoursesToStudent(student, "Problem Solving", 2, 2018, 85)
        self._portal.addCoursesToStudent(student, "Project Management", 1, 2019, 56)
        self._portal.addCoursesToStudent(student, "Java Programming", 1, 2019, 75)
        self._portal.addCoursesToStudent(student, "Web Development", 2, 2019, 76)
        self._portal.addCoursesToStudent(student, "Android Programming", 2, 2019, 80)
        self._portal.addCoursesToStudent(student, "iOS Applications", 1, 2020, 74)
        
        
        sampleStudentProfile = StudentProfile("Edward", "Richards", "M", "Burnaby", "China", 20, 8011111)
        student = Student(sampleStudentProfile, 2019)
        Account.createAccount("Student3", "333333")
        self._portal.registerStudent(student)
        Account.set_user_student_account("Student3", student)
        self._portal.addCoursesToStudent(student, "Problem Solving", 1, 2019, 78)
        self._portal.addCoursesToStudent(student, "Project Management", 1, 2019, 87)
        self._portal.addCoursesToStudent(student, "No Course", 2, 2019, 56)
        self._portal.addCoursesToStudent(student, "Web Development", 1, 2020, 77)
        
                
        sampleStudentProfile = StudentProfile("Souzan", "Robson", "F", "Surrey", "India", 20, 8033344)
        student = Student(sampleStudentProfile, 2019)
        Account.createAccount("Student4", "444444")
        self._portal.registerStudent(student)
        Account.set_user_student_account("Student4", student)
        self._portal.addCoursesToStudent(student, "Project Management", 1, 2019, 89)
        self._portal.addCoursesToStudent(student, "Java Programming", 1, 2019, 87)
        self._portal.addCoursesToStudent(student, "Web Development", 2, 2019, 71)
        self._portal.addCoursesToStudent(student, "Android Programming", 2, 2019, 69)
        self._portal.addCoursesToStudent(student, "iOS Applications", 1, 2020, 75)
        
        sampleStudentProfile = StudentProfile("Jeff", "Cooper", "M", "Vancouver", "England", 21, 8012322)
        student = Student(sampleStudentProfile, 2018)
        Account.createAccount("Student5", "555555")
        self._portal.registerStudent(student)
        Account.set_user_student_account("Student5", student)
        self._portal.addCoursesToStudent(student, "Web Development", 1, 2018, 78)
        self._portal.addCoursesToStudent(student, "Android Programming", 2, 2018, 56)
        self._portal.addCoursesToStudent(student, "iOS Applications", 2, 2018, 89)
        self._portal.addCoursesToStudent(student, "Project Management", 1, 2019, 66)
        self._portal.addCoursesToStudent(student, "Java Programming", 1, 2019, 77)
        self._portal.addCoursesToStudent(student, "Object-Oriented Programming", 2, 2019, 87)
        self._portal.addCoursesToStudent(student, "Problem Solving", 2, 2019, 67)
        self._portal.addCoursesToStudent(student, "No Course", 1, 2020, 78)
    
    # create college course
    def _createAllCollegeCourses(self):
        python = CollegeCourse("Python", "CSCI101", 3)
        objectOrientedProgramming = CollegeCourse("Object-Oriented Programming", "CSCI102", 2)
        problemSolving = CollegeCourse("Problem Solving", "CSCI201", 1)
        projectManagement = CollegeCourse("Project Management", "CSCI202", 3)
        javaProgramming = CollegeCourse("Java Programming", "CSCI301", 3)
        webDevelopment = CollegeCourse("Web Development", "CSCI302", 2)
        androidProgramming = CollegeCourse("Android Programming", "CSCI401", 2)
        iOSApplication = CollegeCourse("iOS Applications", "CSCI402", 3)

        self._portal.addCourse(python)
        self._portal.addCourse(objectOrientedProgramming)
        self._portal.addCourse(problemSolving)
        self._portal.addCourse(projectManagement)
        self._portal.addCourse(javaProgramming)
        self._portal.addCourse(webDevelopment)
        self._portal.addCourse(androidProgramming)
        self._portal.addCourse(iOSApplication)


def main():
    portalManager = PortalManager()
    portalManager.createATestPortal()


main()
