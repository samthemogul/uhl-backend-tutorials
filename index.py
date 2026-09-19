# # import math

# # # VARIABLES - This is way of giving information to the computer for storage
# # age = 15
# # name = "Samuel"
# # is_married = False

# # print(math.sqrt(144))


# # # LOOPS
# # # for loop
# # # for i in range(5):
# # #     print(name, i)

# # # While loop
# # def print_name_x_times(name, times):
# #     stop = times
# #     while stop > 0:
# #         print(name)
# #         stop = stop - 1

# # # print_name_x_times("Joshua", 3)
# # # print_name_x_times("Israel", 2)

# # # DATA STRUCTURES
# # # Array / List
# # # Dictionary

# # # PIP Package manager


# # DAY - 2 UHL BACKEND
# list_of_numbers = [1, 2, 3, 4, 6]
# list_of_numbers.pop(2)
# print(list_of_numbers)

# # Dictionary
# samuel_data = {"name": "Samuel", "age": 15, "is_married": False}

# # TUPLE
# samuel_data_unmutable = (1,2,3, True, "Samuel")
# samuel_data_unmutable


shopping_list_1 = [
    {
        "name": "milk",
        "price": 50,
        "amount": 2
    },
    {
        "name": "sugar",
        "price": 10,
        "amount": 4
    },
    {
        "name": "butter",
        "price": 20,
        "amount": 1
    },
    {
        "name": "water",
        "price": 5,
        "amount": 10
    },
]

shopping_list_2 = [
    {
        "name": "garri",
        "price": 30,
        "amount": 1
    },
    {
        "name": "juice",
        "price": 10,
        "amount": 5
    }
]


# Function to calculate total needed price
# def total_price(shopping_list, tax):
#     total = 0
#     for item in shopping_list:
#         total = total + (item["price"] * item["amount"])
#     total = total + tax
#     return total

# total_1 = total_price(shopping_list_1, 20)
# total_2 = total_price(shopping_list_2, 10)
# print("Total 1 price: ", total_1, " Total 2 price: ", total_2)

# Object Oriented Programming groups eveything into entities that have data, and capabilities.
# data -> attributes
# capabilities -> methods
# entities -> Classes

class ShoppingManager:
    def __init__(self):
        pass
    
    def total_price(self, shopping_list, tax):
        total = 0
        for item in shopping_list:
            total = total + (item["price"] * item["amount"])
        total = tax + total
        self.print_total_price(total)

    def print_total_price(self, total):
        print("Total price is: ", total)

shopping_manager = ShoppingManager()

shopping_manager.total_price(shopping_list_1, 20)
shopping_manager.total_price(shopping_list_2, 15)


# DATABASES
# 1. SQL - Structured Query language
# 2. NoSQL 

# | ID.  |.  Name |.  Email
# |1.    | Sam.   |. sam@gmail.com  -----> ROW
# | 2.    | Dan.  |. dan@gmail.com
#          ^
#          COLUMN
        
        
    