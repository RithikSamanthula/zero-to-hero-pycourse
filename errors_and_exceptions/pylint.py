""""
This is a very simple function
"""

def samplefunc(num1,num2):

    """
    This functions adds both parameters passed in by the user.
    Uses f string literals
    """

    print(f'{num1+num2} is the result')

""""
Runs the function.
Both parameters are added in this case.
"""

def anotherfunc():
    
    """
    This functions concactenates both parameters passed in by the user.
    """

    result1 = input("Enter a string")
    result2 = input("Enter another string")

    output = result1+result2

    return output

samplefunc(1+1)
anotherfunc()
