#Programmer Sadiq
#By@Sadiqul Islam
#Use of enumerate() function


#enumerate() function
#Syntax of enumerate() function : enumerate(iterable, start=0)




#Example 1

b = ['bread','milk','butter']

ext = enumerate(b)
print(type(ext))
#converting to list
print(list(b))


#changeing the default counter
ext = enumerate(b,10)
print(list(ext))
