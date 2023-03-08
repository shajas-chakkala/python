#WAP to accept n numbers and return the sum of it
def add_input(x,*y)
    x=int(input("Enter the number of inputs: "))
    sum=0
    for i in range(x):
        y=int(input("Enter the inputs: "))
        sum=sum+y
    print(sum)

print(add_input(2,20,30))