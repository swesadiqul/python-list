#Programmer Sadiq
#By@Sadiqul Islam
#Use of sum() function



#sum() function
#Syntax of sum() function : sum(iterable,start)
#If you want to add all  element of list.So you use it



#Example 1

list1 = list(range(0,11)) #list



app = sum(list1,0) #use of sum() function
print(app) #add element of list




#Example 2

numbers = [2.5,3,4,-5]

sum1 = sum(numbers) #start parameter is not provided
print(sum1)

sum2 = sum(numbers,10) #use of start parameter
print(sum2)
