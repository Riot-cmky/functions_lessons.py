from  determineEligibility import determineEligibilty_toGraduate, listOfMovies

# functions are ways to wrap your code into reusable units

# define a functuion with def
# only define the function once
# when I pass in a parameter, I am passing in a placeholder for future information
# def say_hello():
#     print("Hello!")
#     print("How are you?")

# def say_hello(name): # (name) is a parameter
#     print(f"Hello! {name}")
#     print(f"How are you? {name}")
    

#call the function also known as invoking 
# pass in information called an argument
# say_hello("Alice")
# say_hello("paul")
# say_hello("Bob")
# say_hello("Altair")

# def say_hello(name,age, address):
#     print(f"Hello! {name}")
#     print(f"How are you? {name}")
#     print(f"{name} are {age} years old")
#     print(f"{name} live in {address} years old")

# say_hello("Alice",22,"123 Main St")
# say_hello("paul",34,"456 Main St")
# say_hello("Bob", 56,"789 Main St")
# say_hello("Altair", 45, "101 Main St")


#-------------------------------------------------------------
determineEligibilty_toGraduate("Alice", 120, 2.0, 800)
determineEligibilty_toGraduate("Bob",119, 1.9, 799)
#--------------------------------------------------------------
listOfMovies("The Matrix", 10, "action")
listOfMovies("The Hangover", 5, "comedy")
listOfMovies("The Ring", 3, "horror")
listOfMovies("Mufasa", 2, "animated")
#-------------------------------------------------------------

# the return statement is used to return a value from a function
# return = statement used to end a function and send a result back to the caller

def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))