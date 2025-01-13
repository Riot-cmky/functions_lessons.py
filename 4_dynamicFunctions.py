# def check_3_digits(number):
#     return number in range(100,1000) #olny 3 digits

# result = check_3_digits(68)
# print(result)

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             print (True) # returnsend sit once and stops, print will keek going
#         else:
#             print (False)

# result = check_3_digits([55, 99, 600])
# print(result)
# print(type(result)) # shows class type

# def check_3_digits(list1):

#     three_digits_list = []    

#     for n in list1:
#         if n in range(100,1000):
#             three_digits_list.append(n)
#         else:
#             pass

#     return three_digits_list

# result = check_3_digits([555, 99, 600])
# print(result)

# coffee_prices = [("cappuccion", 1.5),
#                  ("espresso", 1.2),
#                  ("mocha", 1.9)]

# def most_expensive_coffe(list_of_prices):

#     highest_price = 0
#     my_most_expenisve_coffee =  ''

#     for coffee, price in list_of_prices:
#         if price > highest_price:
#             highest_price = price
#             my_most_expenisve_coffee = coffee
#         else:
#             pass
#     return(my_most_expenisve_coffee,highest_price)

# coffee, price = most_expensive_coffe(list_of_prices=)


# print(most_expensive_coffe(coffee_prices))


#___________________________________________________________________________________________________________________________
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

def all_positives(values): # (values) is the parameter
    for a in values:  # Iterate through each value in the list
        if a <= 0: # if a is less than or queal to 0 if will return false
            return False
        else:
            return True

result = all_positives([-1,5,9])
print(result) # will reslut in False because -1 makes it so

# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.


def sum_less(numbers): # (numbers) is the parameter

    total = 0 # sets the total to 0

    for n in numbers:  # Iterate through each number in the list
        if 0 < n < 1000: # this only allows numbers that are between 1 and 999 to be added to vthe total 
            total += n
    return total

numbers = [50, 500, 2000, -10, 999, 1000] #list of numbers
result = sum_less(numbers)
print(result) # will result in 1549



# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
    

def count_even(numbers):  # (numbers) is the parameter
    count = 0
    for num in numbers:  # Iterate through each number in the list
        if num % 2 == 0: # if the number is divisible by 2 (even) it will be counted
            count += 1
    return count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # list of numbers
result = count_even(numbers)
print(result) 