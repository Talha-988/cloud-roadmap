first_number = int(input("enter number 1: "))
second_number = int(input("enter number 2: "))
operator = input("enter operator: ")
if operator=="+":
    print (f"sum is {first_number+second_number}")
elif operator=="-":
    print (f"diff is {first_number-second_number}")
elif operator=="*":
    print (f"multi is {first_number*second_number}")
elif operator == "%":
    print(f"Remainder is {first_number % second_number}")
elif operator == "/":
    if second_number != 0:
        print(f"div is {first_number / second_number}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")