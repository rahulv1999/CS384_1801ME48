# Function to add two numbers 
def add(num1, num2):
    addition = float(num1) + num2
    if type(addition) != float and type(addition) != int:
        addition = 0 
        print("not valid inputs for addition")
    return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
    subtraction = num1 - float(num2)
    if type(subtraction) != float and type(subtraction) != int:
        subtraction = 0 
        print("not valid inputs for subtraction")    
    return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
    #Multiplication Logic
    try:
        multiplication = float(num1) * float(num2)
    except: 
        print("error in multiplication")
        multiplication =0
    multiplication = round(multiplication,3)
    return multiplication

# Function to divide two numbers 



def divide(num1, num2):
    #Devide logic
    try:
        if num2!=0:
            division = num1/float(num2)
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
    if float(num2) != float(int(num2)):
        print("numn2 can only be a whole number")
        power = 0
        return power
    try:
        power = 1.0
        if num2>0:
            for i in range(int(num2)):
                power *= float(num1)
        else:
            for i in range(int(abs(num2))):
                power /= num1            
        power = round(power,3)
    except :
        print("error in power")
        power = 0

    return power






# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n): 
    gp=[]
    try:
        if n>0 and float(n) != float(int(n)):
            gp.append(round(float(a),3))
            for i in range(int(n)-1):
                a *= r
                gp.append(round(float(a),3)) 
        else:
            print("error in printGp n should be >0  and a whole number ")
            gp.append(0)
    except:
        print("error in printGp")
        gp.clear
        gp.append(0)
    return gp 


# Python 3 program to print AP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n):
    ap =[]
    try:
        if n>0 and float(n) != float(int(n)):
            ap.append(float(a))
            for i in range(int(n)-1):
                a +=float(d)
                ap.append(a)
        else:
            print("error in printAp n should be >0 and a whole number ")
            ap.append(0)           
    except :
        print("error in printAp")
        ap.clear
        ap.append(0)
    return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n):
    hp = []
    try:
        if n>0 and float(n) != float(int(n)):
            
            for i in range(int(n)):
                if a!=0:
                    hp.append(round(1.0/a,3))
                    a +=d
                else:
                    print(f'{i+1} value of term is becoming 1/0 not allowed')
                    hp.clear
                    hp.append(0)
                    break
        else:
            print("error in printHp n should be >0 and a whole number")
            hp.append(0)           
    except :
        print("error in printHp")
        hp.clear
        hp.append(0)
    return hp    