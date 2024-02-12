
dict = {}
credit_list = []
gpa_list = []
result_list = []

def add():
    subject = input("Input Subject : ")
    credit = int(input(f"Input {subject}'s Credit : "))
    grade = int(input(f"Input {subject}'s Grade (0-100) : "))
    dict[subject] = grade
    credit_list.append(credit)

def GPA_count():
    for i in dict:
        if dict[i] >= 91:
            GPA = 4.00
            gpa_list.append(GPA)
        elif 86 <= dict[i] < 91:
            GPA = 3.67
            gpa_list.append(GPA)
        elif 81 <= dict[i] < 86:
            GPA = 3.33
            gpa_list.append(GPA)
        elif 76 <= dict[i] < 81:
            GPA = 3.00
            gpa_list.append(GPA)
        elif 71 <= dict[i] < 76:
            GPA = 2.67
            gpa_list.append(GPA)
        elif 61 <= dict[i] < 71:
            GPA = 2.33
            gpa_list.append(GPA)
        elif 51 <= dict[i] < 61:
            GPA = 2.00
            gpa_list.append(GPA)
        elif 46 <= dict[i] < 51:
            GPA = 1.67
            gpa_list.append(GPA)
        elif 41 <= dict[i] < 46:
            GPA = 1.33
            gpa_list.append(GPA)
        elif dict[i] < 41:
            GPA = 1.00 
            gpa_list.append(GPA)

    for i in range(len(credit_list)):
        result = credit_list[i] * gpa_list[i]
        result_list.append(result)

    Final_GPA = sum(result_list) / sum(credit_list)
    print(f"Your IPK Now is {Final_GPA}")

def info():
    print("This is Your Temporary Data : ")
    for i in dict:
        print(f"Subject {i} => {dict[i]}")

print("========GPA Count System========")

while True:
    try:
        command = int(input("Input Your Command (1 : Add Subject & Grade , 2 : Count GPA , 3 : Info , 4 : Exit) = "))
        if command == 1:
            add()
        elif command == 2:
            GPA_count()
            print("Thank You")
            break
        elif command == 3:
            info()
        elif command == 4:
            print("Thank You")
            break
        else:
            print("Please Re-input Your Command")
    except:
        print("Please Re-input Your Command")