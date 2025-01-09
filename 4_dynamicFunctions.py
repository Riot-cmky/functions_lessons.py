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

coffee_prices = [("cappuccion", 1.5),
                 ("espresso", 1.2),
                 ("mocha", 1.9)]

def most_expensive_coffe(list_of_prices):

    highest_price = 0
    my_most_expenisve_coffee =  ''

    for coffee, price in list_of_prices:
        if price > highest_price:
            highest_price = price
            my_most_expenisve_coffee = coffee
        else:
            pass
    return(my_most_expenisve_coffee,highest_price)

coffee, price = most_expensive_coffe(list_of_prices)


print(most_expensive_coffe(coffee_prices))


#___________________________________________________________________________________________________________________________
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.






# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.






# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.