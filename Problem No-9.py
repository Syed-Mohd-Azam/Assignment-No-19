# Write a python program to create a function to check whether a number falls in a given range.
def fun1(x,y):
    n=int(input("Enter the number which you want to check : "))
    for e in range(x,y,1):
        if e==n:
            print("Yes given number is in range !")
            break
        else :
            continue
    else :
        print("Given number is not in range!")
def fun2(x,y):
    n=int(input("Enter the number which you want to check : "))
    for e in range(x+1,y+1,1):
        if e==n:
            print("Yes given number is in range !")
            break
        else :
            continue
    else : 
        print("Given number is not in range!")
def fun3(x,y):
    n=int(input("Enter the number which you want to check : "))
    for e in range(x,y+1,1):
        if e==n:
            print("Yes given number is in range !")
            break
        else :
            continue
    else:
        print("Given number is not in range!")
def fun4(x,y):
    n=int(input("Enter the number which you want to check : "))
    for e in range(x+1,y,1):
        if e==n:
            print("Yes given number is in range !")
            break
        else :
            continue
    else:
        print("Given number is not in range !")
print("Please select the range type(a,b): (1-4)")
print("1-Range in which a is inclusive and b is exclusive :")
print("2-Range in which a is exclusive and b is inclusive :")
print("3-Range in which both a nd b is inclusive : ")
print("4-Range in which both a and b is exclusive : ")
m=int(input())
print("Enter the values of inner limit and outer limits respectively: ")
a,b=int(input("Enter initial limit: ")),int(int(input("Enter outer limit: ")))
match m:
    case 1:
        fun1(a,b)
    case 2:
        fun2(a,b)
    case 3 :
        fun3(a,b)
    case 4:
        fun4(a,b)
    case _:
        exit()
print()