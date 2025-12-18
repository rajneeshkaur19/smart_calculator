print("SMART CACLCULATOR STARTED")
history = []
valid_ops = ("+","-","*","/","**","%")
while True:
    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number:"))
    op = input("enter operation:")
    if op not in valid_ops:
        print("invalid operation!!!!! try again!!")
        continue
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1*num2
    elif op == "/":
        if num2 == 0:
            print("it is not possible to divide by zero")
            continue
        result = num1/num2
    elif op == "**":
        result = num1**num2
    elif op == "%":
        result = num1%num2
    
    expression = f"{num1} {op} {num2}"
    history.append((expression, result))
    print(f"result:{result}")

    choice = input("do you want to use calculator again?(yes/no/history):").lower()
    if choice == "history":
        print("caclculation history:")
        for expression, result in history:
            print(f"{expression} = {result}")
        break
    elif choice == "no":
        print("smart caclculator closed")
        break
    elif choice == "yes":
        continue
    
