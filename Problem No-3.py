# Write a python program to create a function which expects an unknown number of arguments.
def function(*t):    # argument of this function takes actual arguments as a tuple object (iterable).
    for e in t:
        print(e,end=" ")
    print()
print("The first time function called : ")
function(2)
print("The second time function called :")
function(2,3)
print("The third time function called : ")
function(2,3,4)
print()