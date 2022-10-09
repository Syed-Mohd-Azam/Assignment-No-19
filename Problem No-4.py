# Write a python program to create a function which expects kwargs arguments.
def function(**kwargs):       # formal argument of this function takes keyword arguments as a dictionary object (iterable).
    sum=0
    for e in kwargs.values():
        sum=sum+e
    return(sum)
print("First time function  called and sum is : ",function(a=10,b=20,c=30))
print("Second function called and sum is : ",function(a=12,b=13,c=15,d=20,e=25))