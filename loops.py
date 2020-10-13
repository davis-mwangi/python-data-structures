# Python loops `while` and `for`

#========================== While Loops ===========================#
# while loop - executes a set of statements as long as a condition is true
print("############ While Loops###########3")

i = 1
while i < 6:
    print(i)

    if i == 3:
        break
    i +=1

i = 0
while i <6:
    i += 1
    if i ==3:
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")    

# for loop - iterates over a sequence i.e list, string, dict,sets, string
print("############ While Loops###########3")    
fruits = ["apple","banana","cherry"]
for  i in fruits:
    print(i)

# Loops through strings
for x in "banana":
    print(x)    

# break statement
for x in fruits:
    print(x)    
    if x == "banana":
        break

# Continue statement
print("##### continue stmt #####")
for x in fruits:
    if x ==  "banana":
        continue
    print(x)

# range() function
print("####### range #######")
for x in range(6):
    print(x)

# set increment value default is 1
# 
for x in range(2, 10, 2):
    print(x)

# else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished")        

# Nested loops
adj = ["red","big","taste"]
fruits = ["apple", "banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)