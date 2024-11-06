def count_attendance():
    department=input("Enter the Department name:")
    total_strength=int(input("Enter the total strength in the department: "))
    student_names=[]
    attendance_records={}
    for _ in range(total_strength):
        name=input("Enter student name:")
        student_names.append(name)
        attendance_records[name] ={'Present':0, 'Absent':0}
    total_working_days=int(input("Enter the total working days:"))
    for day in range(1, total_working_days+1):
        print(f"Day {day}:")
        for student in student_names:
            attendance=int(input(f"Enter attendance for {student}(1 for present,0 for absent):"))
            if attendance == 1:
                attendance_records[student]['Present']+=1
            elif attendance ==0:
                attendance_records[student]['Absent']+=1
            else:
                print("Invalid Input. Please enter elther 1 or 0.")

    print("\nAttendance Sumary:")
    for student in student_names:
        present_days=attendance_records[student]['Present']
        absent_days=attendance_records[student]['Absent']
        print(f"{student}: Present-{present_days}, Absent-{absent_days}")
count_attendance()
