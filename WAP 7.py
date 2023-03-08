# WAP to print the smallest number in the list

LIST=[10,20,30,40,200,800,693,6,367,-39,25,22]
smallestnumber=LIST[0]
for i in LIST:
    if i<smallestnumber:
        smallestnumber=i
print(f"The smallest number is {smallestnumber}")