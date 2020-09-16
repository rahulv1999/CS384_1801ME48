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

# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function





def printGP(a, r, n): 
    gp=[]
    try:
        if n>0:
            gp.append(round(a,3))
            for i in range(n-1):
                a *= r
                gp.append(round(a,3)) 
        else:
            print("error in printGp n should be >0")
            gp.append(0)
    except:
        print("error in printGp")
        gp.clear
        gp.append(0)
    return gp 


def printAP(a, d, n):
    ap =[]
    try:
        if n>0:
            ap.append(a)
            for i in range(n-1):
                a +=d
                ap.append(a)
        else:
            print("error in printAp n should be >0")
            ap.append(0)           
    except :
        print("error in printAp")
        ap.clear
        ap.append(0)
    return ap