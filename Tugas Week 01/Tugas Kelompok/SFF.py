
def Sum():
    n = int(input("How Many Numbers that you want to sum? : "))
    number_list = []
    for i in range(n):
        x = int(input(f"Enter Number ({i+1}) = "))
        number_list.append(x)
    result = sum(number_list)
    print(result)

def Factorial(n):
    if n <= 1:
        return 1
    while n > 1:
        return n * Factorial(n-1)

def Fibonacci(n):
    lists = [1]
    for i in range(n):
        if i == 0:
            lists.append(1)
        elif i > 0:
            a = lists[i] + lists[i-1]
            lists.append(a)
    print(lists[n-1])

while True:
    try:
        Operation = int(input("Choose A Operation (1 = Sum , 2 = Factorial , 3 = Fibonacci) : "))
        list = [1,2,3]
        if Operation not in list:
            print("Please Enter 1,2,or 3")
        else :
            break
    except:
        pass

if Operation == 2 or 3:
    n = int(input("What number's factorial / fibonnaci's number you want to know? : "))

if Operation == 1:
    Sum()
elif Operation == 2 :
    result = Factorial(n)
    print(result)
elif Operation == 3 :
    Fibonacci(n)

