# Bubble sort = 3 function (input , sort , print)

def input_list(list):
    Number = int(input("Enter a number that you like to add = "))
    list.append(Number)

def sort_list(list):
    for i in range(len(list)):
        for j in range((len(list)-i-1)):
            if list[j] > list[j+1]:
                list[j] , list[j+1] = list[j+1] , list[j]
    return list

def print_list(list):
    print(f"Your list now => {list}")

n = int(input("Number Of Operation You'll like to have = "))
list = []

for i in range(n):
    while True:
        try:
            Command = int(input("Please Choose an Operation (1 = Input, 2 = Sort, 3 = Print) = "))
            validate = [1,2,3]
            if Command in validate:
                break
            else:
                print("Please Enter Number 1,2,or 3")
        except:
            print("Error Happened , Please Re-enter Your Command")

    if Command == 1:
        input_list(list)
    elif Command == 2:
        sort_list(list)
    elif Command == 3:
        print_list(list)

print(f"Well Done , Your Final List = {list}")
