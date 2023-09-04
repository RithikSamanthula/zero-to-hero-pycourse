print('')
print('Welcome to Calculator')

print('')

def num_selection():

    global num1
    global num2

    num1 = input('Type in your first number: ')
    print('')
    num2 = input('Type in your second number: ')
    print('')

def operation():

    operation = input('Type your operation (+,-,*,/,%): ')

    if operation == '+':
        print('')
        print(f"Result = {int(num1) + int(num2)}")
        print('')

    elif operation == "-":
        print('')
        print(f"Result = {int(num1) - int(num2)}")
        print('')

    elif operation == "*":
        print('')
        print(f"Result = {int(num1) * int(num2)}")
        print('')

    elif operation == "/":
        print('')
        print(f"Result = {int(num1) / int(num2)}")
        print('')

    elif operation == "%":
        print('')
        print(f"Result = {int(num1) % int(num2)}")
        print('')


num_selection()
operation()
