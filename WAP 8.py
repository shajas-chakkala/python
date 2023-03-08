# WAP to print the largest number in the list

LIST=[10,20,30,40,200,800,693,6,367,-39,25,22]
largestnumber=LIST[0]
for i in LIST:
    if i>largestnumber:
        largestnumber=i
print(f"The largest number is {largestnumber}")