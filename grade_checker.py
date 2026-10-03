print("================== STUDENT REPORT CARD ====================")
Student_name = input("Enter Student name : ")
Student_score = float(input("Enter Student score (0-100) : "))
attendance_percentage = float(input("Enter Student attendance percentage (0-100) : "))

print("==================   REPORT   ==================")
if Student_score >=90 and attendance_percentage >= 90:
    print(f"Student name : {Student_name}")
    print(f"Student score : {Student_score}")
    print(f"attendance percentage : {attendance_percentage}")
    print("Grade : A")
    print("Honors : Monors Certificate Awarded")
    print("Status : Pass")
elif Student_score >=80 and attendance_percentage >=80:
    print(f"Student name : {Student_name}")
    print(f"Student score : {Student_score}")
    print(f"attendance percentage : {attendance_percentage}")
    print("Grade : B")
    print("Honors : Certificate Awarded")
    print("Status : Pass")
elif Student_score >=70 and attendance_percentage >=70:
    print(f"Student name : {Student_name}")
    print(f"Student score : {Student_score}")
    print(f"attendance percentage : {attendance_percentage}")
    print("Grade : C")
    print("Honors : Certificate Awarded")
    print("Status : Pass")
elif Student_score >=60 and attendance_percentage >=60:
    print(f"Student name : {Student_name}")
    print(f"Student score : {Student_score}")
    print(f"attendance percentage : {attendance_percentage}")
    print("Grade : D")
    print("Honors : Certificate Awarded")
    print("Status : Pass")
elif Student_score >=50 and attendance_percentage >=50:
    print(f"Student name : {Student_name}")
    print(f"Student score : {Student_score}")
    print(f"attendance percentage : {attendance_percentage}")
    print("Grade : E")
    print("Honors : Certificate Awarded")
    print("Status : Pass")
else :
    print(f"Student name : {Student_name}")
    print(f"Student score : {Student_score}")
    print(f"attendance percentage : {attendance_percentage}")
    print("Grade : F")
    print("Fail")

#range For Loop

for i in range (10,30,3):
    print(i)


    
    