def HelloWorld():
    print("Hello World")

HelloWorld()   # this calls the function


# getting a parameter
def Greeting(name):
    print("Hi " + name + "!")

Greeting("Avi")    # prints  Hi Avi!

# getting two parameters
def Add(num1, num2):
    print(num1 + num2)

Add(10,12)         # prints 22


#returning a value
def returnAdd(num1, num2):
    return(num1 + num2)

print( returnAdd( 11, 12 ))   # Prints 23





