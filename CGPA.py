#student Details
s_name=input("Enter Student Name: ")
s_number=str(input("Enter Student Matriculation Number(e.g 2013/112): "))
s_level=int(input("Enter Student Level(e.g 100): "))
s_department=str(input("Enter Student Department: "))
s_course=str(input("Enter Student Course: "))
print()
print("\033[34mPlease Confirm The Information Below Before You Proceed!!\033[0m")
print()
print("Student Name: ",s_name)
print("Student Matriculation Number: ",s_number)
print("Student Level: ",s_level)
print("Student Department: ",s_department)
print("Student Course: ",s_course)
print()
print()
print()
#calculate student's cpga
'''We create four lists to help us do our calculations easily because we can't sum strings with integers,
These lists are;
C = This is where the courses are stored
CU = This is where the Course units are stored
S = This is where the scores are stored
GP = This is where the product of grade point and credit unit are stored'''
C=[]
CU=[]
S=[]
GP=[]
S_M=int(input("How many semester(s) taken:"))
for i in range(S_M):
    print("Semester {}".format(str(i+1)))
    n=int(input("How many course(s) taken:"))
    for j in range(n):
        #c=The user input the score he or she is offerring
        c=str(input("course code{}:".format(str(j+1))))
        C.append(c)
        #cu=The user input the course unit of the course he or she is offering
        cu=int(input("course unit:"))
        CU.append(cu)
        #sc=The user input his or her score
        sc=int(input("Enter score:"))
        S.append(sc)
        #A=70-100
        #B=60-69
        #C=50-59
        #D=45-49
        #E=40-44
        #F=0-39
        if 70<=sc<=100:
            print('Grade: A')
            print()
        elif 60<=sc<=69:
            print('Grade: B')
            print()
        elif 50<=sc<=59:
            print('Grade: C')
            print()
        elif 45<=sc<=49:
            print('Grade: D')
            print()
        elif 40<=sc<=44:
            print('Grade: E')
            print()
        elif 0<=sc<=39:
            print('Grade: F')
            print()
        #If the users enter an invalid score
        else:
            sc=int(input("\033[31mINVALID SCORE\033[0m\n""PLEASE ENTER THE CORRECT SCORE:"))
            S.append(sc)
            if 70 <= sc <= 100:
                print('Grade: A')
                print()
            elif 60 <= sc <= 69:
                print('Grade: B')
                print()
            elif 50 <= sc <= 59:
                print('Grade: C')
                print()
            elif 45 <= sc <= 49:
                print('Grade: D')
                print()
            elif 40 <= sc <= 44:
                print('Grade: E')
                print()
            elif 0 <= sc <= 39:
                print('Grade: F')
                print()
        #Grade points: GradeA=5points, GradeB=4points, GradeC=3points, GradeD=2points, GradeE=1point, GradeF=0points
        for s in S: 
            if 70 <= sc <= 100:
                f = int(cu * 5)
            elif 60 <= sc <= 69:
                f = int(cu * 4)
            elif 50 <= sc <= 59:
                f = int(cu * 3)
            elif 45 <= sc <= 49:
                f = int(cu * 2)
            elif 40 <= sc <= 44:
                f = int(cu * 1)
            elif sc <= 39:
                f = int(cu * 0)
        GP.append(f)
Total_units = sum(CU)
Total_Grade_points = sum(GP)
GPA = Total_Grade_points/Total_units
CGPA = round(GPA, 2)
print("Total of Units: ", Total_units)
print("Total Grade Points: ", Total_Grade_points)
print("CGPA: ", CGPA)