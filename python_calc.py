try:
    num1 = float(input("Please input the first number: "))  
    num2 = float(input("Please input the second number: "))
    op = input("Please input the operator (/,*,+,-): ")

    if op == '/':
        if num2 == 0:
            print("Invalid! Can't divide by 0!")
        else:
            result = num1 / num2
            print("Result is:", result)  
    elif op == '*':  
        result = num1 * num2
        print("Result is:", result)
    elif op == '+':
        result = num1 + num2
        print("Result is:", result)
    elif op == '-':
        result = num1 - num2
        print("Result is:", result)
    else:
        print("Illegal symbol, please enter correctly!")

except ValueError:  
    print("Error: Please enter valid numbers!")
except Exception as e:  
    print("An error occurred:", e)