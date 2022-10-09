# Write a python program to multiply all the numbers in a list.
def function(a):
    prod=1
    for e in a:
        prod=e*prod
    return(prod)
l,n,i=[],int(input("Enter how many numbers that you want to store in a list : ")),0
while(i<n):
    l.append(int(input("Enter the number please : ")))
    i=i+1
print("Given list is : ",l)
print("The product of all elements in the given list is : ",function(l))