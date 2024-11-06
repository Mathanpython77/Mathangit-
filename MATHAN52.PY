#
roll_no = int(input("enter the roll number:"))
sud_name=input("enter the student name:")
m1=int(input("enter the mark1:"))
m2=int(input("enter the mark2:"))
m3=int(input("enter the mark3"))
m4=int(input("enter the mark4"))
m5=int(input("enter the mark"))
total=m1+m2+m3+m4+m5
Percentage=total/5
if Percentage>=80:
    Grade="A"
elif Percentage >=70 and Percentage<80:
    Grade="B"
elif Percentage >=60 and Percentage<70:
    Grade="C"
elif Percentage >=40 and Percentage<60:
    Grade="D"
else:Grade="E"
print("Roll Number :",roll_no)
print("Student Name :",sud_name)
print("mark1 :",m1)
print("mark2 :",m2)
print("mark3 :",m3)
print("mark4 :",m4)
print("mark5 :",m5)
print("total :",total)
print("Average :",Percentage)
print("Grade :",Grade)