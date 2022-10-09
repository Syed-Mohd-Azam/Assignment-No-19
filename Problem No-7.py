# Write a python program to sum all the numbers in a list.
def function(a):
    return(sum(a))
l,n,i=[],int(input("Enter how many numbers you want to store in a list : ")),0
while(i<n):
    l.append(int(input("Enter a number : ")))
    i=i+1
print("Given list is : ",l)
print("The sum of elements of given list is : ",function(l))