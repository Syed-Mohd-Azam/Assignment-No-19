# Write a python program to create a function that finds a maximum of four numbers.
def function(a,b,c,d):
    m1=a if a>b else b
    m2=c if c>d else d
    return(m1 if m1>m2 else m2)
print("Enter four numbers: ")
x,y,z,w=int(input("Enter first number: ")),int(input("Enter second number : ")),int(input("Enter third number : ")),int(input("Enter fourth number :"))
print("Maximum value is : ",function(x,y,z,w))