"""
Data Structures :
1. List - list is a collection which is ordered and 
changeable. Allows duplicate members. List are flexible and can contain different data types.

2. Dictionary - A dictionary is a collection which 
is unordered, changeable and indexed. 
No duplicate members. Dictionaries are written with curly brackets, and have keys and values.

3. Tuple - A tuple is a collection which is ordered and
unchangeable. Allows duplicate members. Tuples are written with round brackets.

4. Set - A set is a collection which is unordered, unchangeable, and unindexed. No duplicate members. Sets are written with curly brackets.

"""

# Creating a List :
my_List = [1,2.1,"Hello",True,[1,2,3]]

my_first_list = [1,2,3,4,5]

my_third_list = my_List.extend(my_first_list)
print(my_third_list) # Output : None

# Creating a Dictionary :
my_Dict = {"Name":"John", "Age":30, "City":"New York"}
print(my_Dict)
print(my_Dict["Name"]) # Output : John