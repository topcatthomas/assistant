def add(num1, num2):
    return(num1 + num2)
def subtract(num1, num2):
    return(num1 - num2)
def multiply(num1, num2):
    return(num1 * num2)
def divide(num1, num2):
    return(num1 / num2)#
def power(num1, num2):
    return(num ** num2)
def help():
    return("to add, say num plus num. to subtract, say num minus num, to multiply, say num times num. to divide, say num divided by num. to find a power, say num to the power of num")
def calc(opp, num1, num2):
    if opp == "plus":
        add(num1, num2)
    elif opp == "minus":
        subtract(num1, num2)
    elif opp == "times":
        multiply(num1, num2)
    elif opp == "divided by":
        divide(num1, num2)
    elif opp == "to the power of":
        power(num1, num2)