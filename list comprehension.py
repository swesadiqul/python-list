names = ['raju', 'rubayet', 'bokkor', 'bokul', 'kulsum', 'golenur']
newlist = []

for x in names:
    if 'a' in x:
        newlist.append(x)

print(newlist)

#newlist = [expression for item in iterable if condition == True]
#uses list-comprehension

#The return value is a new list, leaving the old list unchanged.
#The condition is like a filter that only accepts the items that valuate to True.
#The condition is optional and can be omitted

newlist2 = [x for x in names if 'a' in x]

print(newlist2)


#With no if statement
#newlist = [expression for item in iterable]

newlist3 = [x for x in  names]
print(newlist3)

#The iterable can be any iterable object, like a list, tuple, set etc.
#You can use the range() function to create an iterable:

newlist4 = [x for x in range(10)]

print(newlist4)

#Accept only numbers lower than 5:

newlist5 = [x for x in range(10) if x < 5]

print(newlist5)

#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

#Set the values in the new list to upper case

newlist6 = [x.upper() for x in names]
print(newlist6)

#You can set the outcome to whatever you like
#Set all values in the new list to 'hello'

newlist7 = ['hello' for x in names]

print(newlist7)


#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
newlist8 = [x if x != 'rubayet' else "raju" for x in names]
print(newlist8)

