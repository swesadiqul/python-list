# Programmer Sadiq
# By@Sadiqul Islam
# List advance-04


# Built in function and method

# all function
list1 = [1,2,3,5,6,9]
print(all(list1))

# all value  false
list2 = [0, False]
print(all(list2))

# One false value
list3 = [1,3,4,0]
print(all(list3))

# One true value
list4 = [0,False,5]
print(all(list4))

# Empty iterable

list5 = []
print(all(list5))

print("__________________________________")

# any function
list1 = [1,3,4,5]
print(any(list1))

list1 = [0,False]
print(any(list1))

list1 = [1,3,4,0]
print(any(list1))

list1 = [0,False,5]
print(any(list1))
list1 = []
print(any(list1))

print("_____________________________________")
# max function
list1 = [4,5,6,7,1,9]
print(max(list1))

# min function
list1 = [4,5,6,7,1,9]
print(min(list1))
# Sorted function
vowels = ["e","i","a","o","u"]
print(sorted(vowels))
# sum function
nums = [2.5,3,4,-5]
print(sum(nums))
# pop function
list1 = ["Naim","Redoy","Rana","Baijit","Ibrahim"]
list1.pop(1)
print(list1)
# clear function
list1 = ["Python","Java","C++","Cobol","C"]
list1.clear()
print(list1)
# index function
vowels = ["e","i","a","o","u"]
index = vowels.index("a")
print(index)
# count function
vowels = ["e","u","i","a","o","u","u"]
count = vowels.count("u")
print(count)
# reverse function
list1 = ["Naim","Redoy","Rana","Baijit","Ibrahim"]
list1.reverse()
print(list1)
