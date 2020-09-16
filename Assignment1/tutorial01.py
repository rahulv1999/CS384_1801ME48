# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
    #Multiplication Logic
    try:
        multiplication = num1 * num2
    except: 
        print("error in multiplication")
        multiplication =0
    return multiplication

# Function to divide two numbers 



def divide(num1, num2):
    #Devide logic
    try:
        if num2!=0:
            division = num1/num2
        else:
            print("can't devide with zero")
            division =0
    except :
        print("error in division")
        division = 0 
    return division

# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2): #num1 ^ num2
	#DivisionLogic 
    try:
        power = 1
        for i in range(int(num2)):
            power *= num1
    except :
        print("error in power")
        power = 0

    return power