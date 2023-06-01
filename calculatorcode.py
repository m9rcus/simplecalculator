while True:
    
    operator = input("Enter the number that coralates with your desired operation ( 1 : ADD | 2 : SUBRACT | 3 : MULTIPLY | 4 : DIVIDE ) : ")
    
    if operator in ["e","E"]:
        continue

    if operator.isnumeric():
        e_message = print("(Enter \"e\" at any time to restart the calculator)")
    
    if not operator.isnumeric():
        print("Operator is not valid, please try again.")
    
    if operator == "1":
        num1a = input("1 : ADD | Enter the first number: ")
        if num1a in ["e","E"]:
            continue
        if not num1a.isnumeric():
            print("Not a valid number, please try again.")
            continue
        
        num2a = input("1 : ADD | Enter the second number: ")
        if num2a in ["e","E"]:
            continue
        if not num2a.isnumeric():
            print("Not a valid number")
            continue

        if num1a.isnumeric():
            num1af = float(num1a)

        if num2a.isnumeric():
            num2af = float(num2a)
            result_a = num1af + num2af
            print(result_a)
    
    if operator == "2":
        num1s = input("2 : SUBTRACT | Enter the first number: ")
        if num1s in ["e","E"]:
            continue
        if not num1s.isnumeric():
            print("Not a valid number, please try again.")
            continue
        
        num2s = input("1 : ADD | Enter the second number: ")
        if num2s in ["e","E"]:
            continue
        if not num2s.isnumeric():
            print("Not a valid number")
            continue

        if num1s.isnumeric():
            num1sf = float(num1s)

        if num2s.isnumeric():
            num2sf = float(num2s)
            result_s = num1sf - num2sf
            print(result_s)
    
    if operator == "3":
        num1m = input("3 : MULTIPLY | Enter the first number: ")
        if num1m in ["e","E"]:
            continue
        if not num1m.isnumeric():
            print("Not a valid number, please try again.")
            continue
        
        num2m = input("1 : ADD | Enter the second number: ")
        if num2m in ["e","E"]:
            continue
        if not num2m.isnumeric():
            print("Not a valid number")
            continue

        if num1m.isnumeric():
            num1mf = float(num1m)

        if num2m.isnumeric():
            num2mf = float(num2m)
            result_m = num1mf * num2mf
            print(result_m)

    if operator == "4":
        num1d = input("4 : DIVIDE | Enter the first number: ")
        if num1d in ["e","E"]:
            continue
        if not num1d.isnumeric():
            print("Not a valid number, please try again.")
            continue
        
        num2d = input("1 : ADD | Enter the second number: ")
        if num2d == "0":
            print("You cannot divide by 0, please try again")
            continue
        if num2d in ["e","E"]:
            continue
        if not num2d.isnumeric():
            print("Not a valid number")
            continue

        if num1d.isnumeric():
            num1df = float(num1d)

        if num2d.isnumeric():
            num2df = float(num2d)
            result_d = num1df / num2df
            print(result_d)
