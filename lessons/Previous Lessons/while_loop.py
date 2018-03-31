keep_going = "y"
while keep_going == "y":
    num = int(input("How many numbers?"))
    for x in range(1,num+1):
        print(x)
    keep_going = input("Do you want to go again? (y) (n)")