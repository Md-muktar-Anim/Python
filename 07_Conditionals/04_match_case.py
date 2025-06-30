a = int(input("Enter a number between 1 and 50000:"))

match a:
    case 1371:
        print("You won a iphone")
    case 54:
        print("You won $2")
    case 124: 
        print("You won a perfume")
    case _:
        print("Better luck next time")