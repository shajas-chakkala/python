# WAP to create a list of elements by taking input from user.

Numberofelements = int(input("Enter the number of elements: "))
LIST=[]
for x in range(Numberofelements):
    element=int(input(f"Enter the {x} element: "))
    LIST.append(element)
print(LIST)
