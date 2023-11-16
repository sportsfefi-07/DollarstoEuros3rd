#Dollars to Euro


#step 1
'''Title of Program
 Purpose of Program and Version #
 Programmer Credit
 '''
print("DollarstoEuros")
print("this program converts dollars to euros")
print("version 1.0")




#step 2:
'''Declare a local variable.
 Use the input function with the prompt "Enter dollar amount to be converted:"
 Save input from the input function and convert to a float.'''
answer = input("Do you want to convert?")

while answer == "y":
    dollars = float(input("Enter dollar amount to be converted:"))


    #step 3:
    ''' Create a local variable to store euros
    Use the equation euro = dollar * .94540'''
    euro = dollars * .94540


    #step 4:
    '''Use the print() to output the new euro amount with a label beforehand.'''
    print("Euro_amount:" +  str(euro))

    #step 5:
    '''Use a while loop around the data collection and output logic.
    Add a prompt using the input() that states Would you like to convert dollars to euros?
    Only allow the loop to continue if the user says they want to convert again.
    Use a break statement to end the loop when a no is entered by the user.'''



    

#step 6:
'''Create a Pull Request from the Development Branch to the Main Branch.
 Merge Pull Request into Main branch.'''

