#Programmer Sadiq
#By@Sadiqul Islam
#Use of any() function



#any() function
#Syntax of any() function : any(iterable)
#All values are true: True
#All values are false: False
#One value is true(others are false): True
#One value is false(others are true): True
#Empty Iterable: False



#Example 1
ex1 = [1,2,6,7,9] #all values are true

result = any(ex1) #use of any() function
print(result) #update list


#Example 2
ex2 = [0,False] #all values are false

print(any(ex2)) #use of any() function


#Example 3
ex3 = [3,4,5,8,0] #one value is false

print(any(ex3)) #use of any() function


#Example 4
ex4 = [False,4,0] #one value is true

print(any(ex4))


#Example 5
ex5 = [] #empty iterable

print(any(ex5)) #use of any() function

