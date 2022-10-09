# Write a python program to create a function to check whether a given number is even or odd.
def function(a):
    if a==0:
        print("Given number is neither odd nor even.")
    else:
        print(" Given number is even number " if a%2==0 else " Given number is odd number ")  
function(int(input("Enter a number to check whether it is even or odd : ")))