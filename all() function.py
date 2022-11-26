#Programmer Sadiq
#By@Sadiqul Islam
#Use of all() function





#all() function
#Syntax of all() function : all(iterable)
#All values are true: True
#All values are false: False
#One value is true(others are false): False
#One value is false(others are true): False
#Empty Iterable : True



#Example 1
ex1 = [1,2,6,7,9] #all values are true

result = all(ex1) #use of all() function
print(result) #update list


#Example 2
ex2 = [0,False] #all values are false

print(all(ex2)) #use of all() function


#Example 3
ex3 = [3,4,5,8,0] #one value is false

print(all(ex3)) #use of all() function


#Example 4
ex4 = [False,4,0] #one value is true

print(all(ex4))


#Example 5
ex5 = [] #empty iterable

print(all(ex5)) #use of all() function
