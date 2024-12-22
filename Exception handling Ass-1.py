# Q1.What is an Exception in python? Write the difference between Exceptions and Syntax errors.
# Answer-
"""An Exception is an error that occurs during the execution of a program that disrupts its normal flow. It is a runtime error that arises
due to unexpected conditions, such as dividing by zero, accessing a non-existent file, or trying to use an undefined variable.
understand with the help of diagram:

                                                           NO
    start code > execute code > exception occured                            > continue execution > end  
                                                    YES > handle exception                               
                                                                                                             """
# the difference between Exceptions and Syntax errors.
"""Exception - 
       1. Exceptions are errors that occur during the execution of a program.
       2. It is Detected while the program is running.
       3. It Can be handled using try and except blocks.
       4. The program can continue running if the exception is handled.
       5. example-Division by zero, file not found, index out of range.
       Syntax - 
       1. Syntax errors occur due to incorrect syntax in the code.
       2. It is Detected before the program is executed, at compile time.
       3. It Cannot be handled,the code must be corrected.
       4. The program won’t run until syntax errors are fixed.
       5. example- Missing colon, unmatched parentheses, wrong indentation.   """
       
# Q2.What happens when an exception is not handled? Explain with an example.
# Answer-
"""If an exception is not handled, the program stops running immediately when the error occurs. This is called a program crash.
it shows an error message (called a traceback) on the screen, telling you what went wrong and where in the code the error happened.

example:
when an exception is not handled:
a = 10/0      , here it is not divisible so it gives an error and not reaches to the next line           
print("The result is :",a)  """
# Preventing the Crash with Exception Handling using a try and except
try :
   10/0
except ZeroDivisionError as e:  
   print(e)
   
# Q3.Which Python statements are used to catch and handle exceptions? Explain with an example.
"""the following statements are used to catch and handle exceptions:

1. try: This block contains the code that might raise an exception.
2. except: This block handles the exception, You can specify the type of exception to catch specific errors.
3. else (optional): This block runs if no exceptions occur in the try block.
4. finally (optional): This block always runs, whether or not an exception occurred."""
# example-
try:
   num1 = 8#int(input("Enter the first number:"))
   num2 = 6#int(input("Enter the Second number:"))
   
   result = num1/num2
except ValueError as e:
   print("Please enter valid numbers" , e)
except ZeroDivisionError as e:
   print("Division by zero is not allowed",e)
except Exception as e:
   print("An unexcepted error occured")
else :
   print("The result of the division is :", result)
finally:
   print("Program execution completed")
   
# Q4.Explain with an example:
#a.try and else
#b.finally
#c.raise
# Answer-
class EmptyFileError(Exception):
    pass

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not content.strip():  # Check if file is empty
                raise EmptyFileError
    except FileNotFoundError:
        print("The file is missing. Please check the file path")
    except EmptyFileError as e:
        print("File is empty")
    else:
        print("The file was read successfully")
    finally:
        print("Finished trying to process the file")

# Example Usage
try:
    process_file("example.txt")
except FileNotFoundError:
    print("File is not found")
except EmptyFileError:
    print("File is empty")
    
#Q5.What are Custom Exceptions in python? Why do we need Custom Exceptions? Explain with an example.
# Answer-
"""Custom Exceptions- Custom exceptions are user-defined exceptions that allow developers to create specific error types tailored to their
application or use case.These exceptions are derived from the base class Exception and enable more meaningful error handling in programs.
Example -   """
# Defining a custom exception
class insufficientbalanceerror(Exception):
    def __init__(self , balance , withdraw):
        self.balance = balance
        self.withdraw = withdraw
        
        
def withdraw (balance , amount):
    if amount > balance :
        raise insufficientbalanceerror(balance , amount)
    balance -= amount 
    return balance 

 #Using the custom exception    
try :
    current_balance = 1000
    withdraw_amount = 1500
    new_balance = withdraw(current_balance , withdraw_amount)
    print("transaction successfull,New balance is ",new_balance)
except insufficientbalanceerror as e:
    print("Insufficient balance error ")
finally:
    print("transaction process completed")
    
#Q6.Create a custom exception class. Use this class to handle an exception.
# Answer-
"""here's an example of creating a custom exception class and using it to handle an exception:"""

# Define a custom exception class
class NegativeNumberError(Exception):
    def __init__(self, number):
        self.number = number

def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError(number)  # Raise custom exception
    return number ** 0.5

try:
    num = -12
    result = calculate_square_root(num)
    print("The square root is",result)
except NegativeNumberError as e:  # Handle the custom exception
    print("Error:", e)
finally:
    print("Program execution completed.")
