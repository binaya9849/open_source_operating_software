# 1. Sort characters in a string
def sort_characters():
    """
    1>Sort characters
    Write a program that takes a single string as its input and sort its characters 
    from the lowest Unicode value to the highest Unicode value. The program should 
    print the new string.

    The output from your program, when called with the code in the Test column, 
    should be exactly as shown in the Result column:

    For example:

    Input	Result
    wikipedia	adeiiikpw
    assume	aemssu
    """
    s = input("Enter a string to sort: ")
    sorted_string = ''.join(sorted(s))
    print("Sorted string:", sorted_string)


# 2. Arithmetic operations
def arithmetic():
    """
    2>Arithmetic
    Write a program that takes two integers, a and b, as input.
    Your program should compute and display:
    The sum of a and b
    The difference when b is subtracted from a
    The product of a and b
    The quotient when a is divided by b
    The remainder when a is divided by b
    The result of a ** b

    The output from your program, when called with the code in the Test column, 
    should be exactly as shown in the Result column

    For example:

    Input	Result
    10
    2
    10 + 2 is 12
    10 - 2 is 8
    10 * 2 is 20
    10 / 2 is 5.0
    10 % 2 is 0
    10 ^ 2 is 100
    """
    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            break
        except ValueError:
            print("Please enter valid integers!")

    print(f"{a} + {b} is {a + b}")
    print(f"{a} - {b} is {a - b}")
    print(f"{a} * {b} is {a * b}")
    print(f"{a} / {b} is {a / b}")
    print(f"{a} % {b} is {a % b}")
    print(f"{a} ^ {b} is {a ** b}")


# 3. Squares dictionary
def sum_squares():
    """
    Squares
    Write a program that prints a dictionary where the keys are numbers between 1 and N,
    and the values are square of keys.

    Input Specification
    The first line of input contains N
    Output Specification
    Print the dictionary

    For example:
    Input	Result
    10	{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    """
    while True:
        try:
            N = int(input("Enter N: "))
            break
        except ValueError:
            print("Please enter a valid integer!")

    squares_dict = {i: i**2 for i in range(1, N+1)}
    print("Squares dictionary:", squares_dict)


# 4. Sum of first n positive integers
def sum_first_n():
    """
    Sum of the First n Positive Integers
    Write a program that takes a positive integer, n, as input and then displays the sum 
    of all of the integers from 1 to n. The sum of the first n positive integers can be 
    computed using the formula: sum = n*(n+1)/2

    For example:
    Input	Result
    10	The sum of the first 10 positive integers is 55
    4	The sum of the first 4 positive integers is 10
    """
    while True:
        try:
            n = int(input("Enter n: "))
            break
        except ValueError:
            print("Please enter a valid integer!")

    total = n * (n + 1) // 2
    print(f"The sum of the first {n} positive integers is {total}")


# 5. Count vowels
def count_vowels():
    """
    Count vowels
    Assume s is a string of lower case characters.
    Write a program that counts up the number of vowels contained in the string s. 
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

    For example:
    Input	Result
    Restaurant	Number of vowels: 4
    Air	        Number of vowels: 2
    """
    s = input("Enter a string: ")
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels: {count}")


# 6. Sum a collection of numbers
def sum_collection():
    """
    Sum a Collection of Numbers
    Write a program that sums all of the numbers taken as input, while ignoring any input 
    that is not a valid number. Your program should display the current sum after each 
    number is entered. It should display an error message after each non-numeric input, 
    and then continue to sum any additional numbers entered by the user. The program 
    exits when the user enters 0.

    For example:
    Input	Result
    12
    6
    11
    0
    The total is now 12.0
    The total is now 18.0
    The total is now 29.0
    The grand total is 29.0
    """
    total = 0.0
    print("Enter numbers to sum (enter 0 to stop):")
    while True:
        user_input = input()
        try:
            num = float(user_input)
        except ValueError:
            print("That wasn’t a number.")
            continue
        if num == 0:
            break
        total += num
        print(f"The total is now {total}")
    print(f"The grand total is {total}")


# 7. Custom encoder
def custom_encoder_program():
    """
    Custom encoder
    Write a function called "custom_encoder" that accepts a string text as parameter and 
    for each char of the text it calculates its 0-based position in the reference string:
    reference_string = 'abcdefghijklmnopqrstuvwxyz'

    If a char is not found in the reference_string, its position should be -1
    """
    def custom_encoder(text):
        reference_string = 'abcdefghijklmnopqrstuvwxyz'
        return [reference_string.index(c) if c in reference_string else -1 for c in text.lower()]

    text = input("Enter text to encode: ")
    positions = custom_encoder(text)
    print("Positions:", positions)


# 8. Person class
def person_program():
    """
    Write a class Person that has a member function hello()
    For example:
    p = Person('Matti')
    p.hello()
    Output:
    Hello, my name is Matti
    """
    class Person:
        def __init__(self, name):
            self.name = name
        def hello(self):
            print(f"Hello, my name is {self.name}")

    name = input("Enter person's name: ")
    p = Person(name)
    p.hello()


# 9. Restaurant class
def restaurant_program():
    """
    Restaurant
    Make a class called Restaurant. The __init__() method stores restaurant_name and cuisine_type.
    Make describe_restaurant() and open_restaurant() methods.
    """
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"{self.name} serves wonderful {self.cuisine_type}.")
        def open_restaurant(self):
            print(f"{self.name} is open. Come on in!")

    name = input("Enter restaurant name: ")
    cuisine = input("Enter cuisine type: ")
    restaurant = Restaurant(name, cuisine)
    print(restaurant.name)
    print(restaurant.cuisine_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()


# 10. User class
def user_program():
    """
    User
    Make a class called User. Attributes: first_name, last_name, username, email, location.
    Methods: describe_user() and greet_user()
    """
    class User:
        def __init__(self, first_name, last_name, username, email, location):
            self.first_name = first_name
            self.last_name = last_name
            self.username = username
            self.email = email
            self.location = location
        def describe_user(self):
            print(f"Name: {self.first_name} {self.last_name}")
            print(f"Username: {self.username}")
            print(f"Email: {self.email}")
            print(f"Location: {self.location}")
        def greet_user(self):
            print(f"Welcome back {self.username}!")

    first_name = input("First name: ")
    last_name = input("Last name: ")
    username = input("Username: ")
    email = input("Email: ")
    location = input("Location: ")

    user = User(first_name, last_name, username, email, location)
    user.describe_user()
    user.greet_user()


# 11. Combine two sorted lists
def combine_lists_program():
    """
    Write a function to combine two sorted lists into one sorted list
    without using Python's built-in sort()
    """
    def combine_lists(list1, list2):
        combined = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                combined.append(list1[i])
                i += 1
            else:
                combined.append(list2[j])
                j += 1
        while i < len(list1):
            combined.append(list1[i])
            i += 1
        while j < len(list2):
            combined.append(list2[j])
            j += 1
        return combined

    list1 = list(map(int, input("Enter first sorted list (space-separated): ").split()))
    list2 = list(map(int, input("Enter second sorted list (space-separated): ").split()))
    result = combine_lists(list1, list2)
    print("Combined list:", result)

# Menu List
if __name__ == "__main__":
    while True:
        print("\n=== Exercise Menu ===")
        print("1 - Sort Characters")
        print("2 - Arithmetic")
        print("3 - Squares Dictionary")
        print("4 - Sum of First n Integers")
        print("5 - Count Vowels")
        print("6 - Sum Collection of Numbers")
        print("7 - Custom Encoder")
        print("8 - Person Class")
        print("9 - Restaurant Class")
        print("10 - User Class")
        print("11 - Combine Two Sorted Lists")
        print("0 - Exit")

        choice = input("Enter the number of the program to run: ")

        if choice == '1':
            sort_characters()
        elif choice == '2':
            arithmetic()
        elif choice == '3':
            sum_squares()
        elif choice == '4':
            sum_first_n()
        elif choice == '5':
            count_vowels()
        elif choice == '6':
            sum_collection()
        elif choice == '7':
            custom_encoder_program()
        elif choice == '8':
            person_program()
        elif choice == '9':
            restaurant_program()
        elif choice == '10':
            user_program()
        elif choice == '11':
            combine_lists_program()
        elif choice == '0':
            print("Exiting program. Thankyoucd..!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 11.")
