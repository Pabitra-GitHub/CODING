def calculator():
    print("===== Advanced Calculator =====")
    print("Supported operations: +, -, *, /, %, ** (power)")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            num1_input = input("Enter first number (or 'exit' to quit): ")
            if num1_input.lower() == 'exit':
                print("Exiting calculator. Goodbye!")
                break
            num1 = float(num1_input)

            op = input("Choose operation (+, -, *, /, %, **): ")
            if op.lower() == 'exit':
                print("Exiting calculator. Goodbye!")
                break

            num2_input = input("Enter second number: ")
            if num2_input.lower() == 'exit':
                print("Exiting calculator. Goodbye!")
                break
            num2 = float(num2_input)

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
            elif op == '%':
                result = num1 % num2
            else:
                print("❌ Invalid operation.")
                continue

            print(f"✅ Result: {result}\n")

        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.\n")
        except ZeroDivisionError as e:
            print(f"❌ Error: {e}\n")

# Run the calculator
calculator()
