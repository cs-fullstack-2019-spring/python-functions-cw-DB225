def main():
    problem1()
    #problem2()
    #problem3()
    #problem4()


#PROBLEM1
#Create a function in your program that counts from 0 to [NUMBER]
def problem1():
    number = int(input("put a number: "))
    for num in range(0,number+1):
        print(num)
def functionCount(number):
    print(number)
################################################################################################
#PROBLEM2
#Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def problem2():
    userInput = " "
    while(userInput != 'q'):
        userInput = input("Keep talking to me: ")
################################################################################################
#PROBLEM3
#Create 4 functions called add, subtract, multiply, and divide.
# Create them to allow a user to perform the name of the function to the two numbers and return the result.
def problem3():

    num1 = int(input("Put the first number: "))
    num2 = int(input("Put the second number: "))
    userInput = input("Choose you operation: add,substract\nmultiply,divide: ")
    if(userInput == "add"):
        print(add(num1,num2))
    elif(userInput == "substract"):
        print(substract(num1,num2))
    elif(userInput == "multiply"):
        print(multiply(num1,num2))
    elif(userInput == "substract"):
        print(divide(num1,num2))
def add(num1,num2):
    return (num1+num2)

def substract(num1,num2):
    return (num1-num2)

def multiply(num1,num2):
    return  (num1*num2)

def divide(num1,num2):
    return (num1/num2)

##################################################################################################
#PROBLEM4
#Create a function that will ask the user for a number.
# Use the function to get two numbers, then pass the two numbers to a function and ask a user if they want to add, subtract, multiple, or divide them.
# Return a string that prints the two numbers, which operation it did, and the result.
def problem4():
    num1 = int(input("Put the first number: "))
    num2 = int(input("Put the second number: "))
    userInput = input("Do you want to add,substract, multiply or divide? ")
    if(userInput == "add"):
        print(f"You did a addition of {num1} and {num2} and the result is {add(num1,num2)}")
    elif(userInput == "substract"):
        print(f"You did a substraction of {num1} from {num2} and the result is {substract(num1,num2)}")
    elif(userInput == "multiply"):
        print(f"You multiplied {num1} by {num2} and the result is {multiply(num1,num2)}")
    elif(userInput == "substract"):
        print(f"You divided {num1} by {num2} and the result is {divide(num1,num2)}")
def add(num1,num2):
    return num1+num2

def substract(num1,num2):
    return (num1-num2)

def multiply(num1,num2):
    return  (num1*num2)

def divide(num1,num2):
    return (num1/num2)


##############################################################################################


if __name__ == '__main__':
    main()