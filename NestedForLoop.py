
#normal for demo 
for i in range(7):  
    for j in range(i):     
        print("*", end="") 
    print()  # Move to the next line

#iteration 1
#i=1
#for j in range(1) execute j loop one time print("*") it one time
#*
#iteration 2
#i=2
#for j in range(2) execute j loop two time print("*") it one time
#**
#iteration 3
#i=3
#for j in range(3) execute j loop three time print("*") it one time
#***

print("===============================#####=========================================")
'''Q1
-----------------------
*******
******
*****
****
***
**
*
'''

# Loop for rows starting at 7 down to 1
for i in range(7, 0, -1):  
    for j in range(i):     
        print("*", end="") 
    print()# Move to the next line

#iteration 1
#i=7
#for j in range(7) execute j loop 7 time print("*") it 7 time
#*******
#iteration 2
#i=6(7-1)
#for j in range(6) execute j loop 6 time print("*") it 6 time
#******
#iteration 3
#i=5(6-1)
#for j in range(5) execute j loop 5 time print("*") it 5 time
#*****
    
print("===============================#####=========================================")

'''Q2
----*
---**
--***
-****
*****
'''

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")  
    for k in range(i):
        print("*", end="")  
    print() # Move to the next line 

print("===============================#####=========================================")

'''Q3
1
10
101
1010
10101
'''
for i in range(1, 6):
    for j in range(i):
        print(j % 2, end="")
    print()# Move to the next line

print("===============================#####=========================================")

'''Q4
____1
___01
__101
_0101
10101
'''
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")  
    for k in range(i):
        print(k % 2, end="") 
    print()# Move to the next line

print("===============================#####=========================================")

'''Q5
*********
-*******
--*****
---***
----*
'''
for i in range(5):
    for j in range(i):
        print(" ", end="")  
    for k in range(9 - 2 * i):
        print("*", end="")  
    print()  # Move to the next line



