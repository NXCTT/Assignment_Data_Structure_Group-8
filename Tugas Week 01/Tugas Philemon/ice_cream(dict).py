
Store_Data = {
    "chocolate" : 10000,
    "vanilla" : 10000,
    "strawberry" : 10000
}

def Add():
    Key = input("Enter Ice Cream's Flavor : ")
    Value = int(input("Enter Ice Cream's Price : "))
    Key = Key.lower()
    Store_Data[Key] = Value

def Delete():
    Delete_key = input("Enter Flavor That You'll like to Remove : ")
    Store_Data.pop(Delete_key)

def Read():
    print(Store_Data)

while True:
    try:
        Op = int(input("Command List (1 : Add , 2 : Delete , 3 : Read , 4 : Exit ) = "))
        if Op == 1:
            Add()
        elif Op == 2:
            Delete()
        elif Op == 3:
            Read()
        elif Op == 4:
            print("Program Ended , Thank You ")
            break
        else :
            print("Error Command , Please ReTry ")
    except:
        print("Error Input , Please ReTry ")

