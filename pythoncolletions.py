'''Python Collections(Arrays)
------ ----------- ----------

There are four collection data types in the python programming language..

* List : is a collection which is ordered and changeable. Allows duplicate members..
* Tuple : is a collection which is ordered and unchangeable. Allows duplicate members..
* Set :is a collection which is unordered and unchangeable,and unindexed.No duplicate members..
* Dictionary :is a collection which is ordered and changeable.No duplicate members..

1.List[] =>
  ----
  Allow Duplicate
  Any type of data can be stored.
  We can  modify the list item.we can add or remove
  insert(),append(),extend(),pop().

2.Tuple() =>
  ----
  Allow Duplicate
  Any type of data can be stored.
  We cannot modify the tuple item.We cannot add or remove..

3.Set{} =>
  ---
  Do Not Allow Duplicate,Duplicate Values will be removed..
  Any type of data can be stored.
  We cannot modify the set item.But We can add or remove items..
  Sets are unordered..
  add(),update(),remove(),pop()

4.Dictionary{} =>
  ----------
  Do Not allow Duplicate,Duplicate value will Overwrite  Existing  Value..
  Any Type of data can be stored
  Key: Value pair{"name":"murugan"}
  get(),keys(),values(),items(),update({"year":2020}),thisdict["color"]="red",
                        thisdict.pop("model"),del,
Eg:'''

#1. Creating a List:
my_list = [1, 2, 3, 4, 5]
print(my_list) #Output: [1, 2, 3, 4, 5]

#2. Accessing Elements:
print(my_list[0])  # Output: 1

#3. Appending Elements:
my_list.append(6)
print(my_list) #Output:[1, 2, 3, 4, 5, 6]

#4. Inserting Elements:
my_list.insert(2, 10)  # Inserts 10 at index 2 
print(my_list) #Output:[1, 2, 10, 3, 4, 5, 6]

#5. Removing Elements:
my_list.remove(3)  # Removes the first occurrence of 3
print(my_list) #Output:[1, 2, 10, 4, 5, 6]

#6. Popping Elements:
popped_element = my_list.pop(2)  # Removes and returns the last element of the list
print(popped_element) #Output:10

#7. Slicing Lists:
sliced_list = my_list[1:3]  # Returns elements from index 1 to 2
print(sliced_list)   #Output:[2, 4]

#8. Length of List:
length = len(my_list)
print(length)    #Output:5

#9. Iterating Over a List:
for item in my_list:
    print(item)  #Output:1 2 4 5 6

#10. List Comprehension:
squared_list = [x**2 for x in my_list]
print(squared_list) #Output:[1, 4, 16, 25, 36]

#11. Sorting a List:
my_list.sort()  # Sorts the list in ascending order
print(my_list)   #Output:[1, 2, 4, 5, 6]

#12. Reversing a List:
my_list.reverse()  # Reverses the elements in the list
print(my_list)  #Output:[6, 5, 4, 2, 1]

#13. Copying a List:
new_list = my_list.copy()
print(new_list) #Output:[6, 5, 4, 2, 1]

#14. Clearing a List:
my_list.clear()  # Removes all elements from the list
print(my_list)  #Output:[]

#15. Checking if an Item Exists:
if 10 in my_list:   #Check item into the list...
    print("10 exists in the list")

#16. Extend a list:
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)

print("------------------------------------------------------------------------")

#1. Creating a Tuple:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)   # Output: (1, 2, 3, 4, 5)

#2. Accessing Elements:
print(my_tuple[0])  # Output: 1

#3. Slicing Tuples:
sliced_tuple = my_tuple[1:3]  # Returns elements from index 1 to 2
print(sliced_tuple)  # Output: (2, 3)

#4. Length of Tuple:
length = len(my_tuple)
print(length)    # Output:5

#5. Iterating Over a Tuple:
for item in my_tuple:
    print(item)     # Output:1 2 3 4 5

#6. Tuple Packing and Unpacking:
tuple_packing = 1, 2, 3
a, b, c = tuple_packing  # Tuple unpacking
print(tuple_packing)    # Output:(1, 2, 3)
print(a, b, c)  # Output:(1 2 3)

#7. Checking if an Item Exists:
if 3 in my_tuple:
    print("3 exists in the tuple")  # Output:3 exists in the tuple

#8. Counting Occurrences:
count = my_tuple.count(3)  # Returns the number of occurrences of 3 in the tuple
print(count)    # Output:1

#9. Finding Index:
index = my_tuple.index(3)  # Returns the index of the first occurrence of 3
print(index)    # Output:2

#10. Converting Tuple to List:
tuple_to_list = list(my_tuple)
print(tuple_to_list)    # Output:[1, 2, 3, 4, 5]

#11. Converting List to Tuple:
list_to_tuple = tuple([1, 2, 3, 4, 5])
print(list_to_tuple)    # Output:(1, 2, 3, 4, 5)

#12. Concatenating Tuples:
concatenated_tuple = my_tuple + (6, 7, 8)
print(concatenated_tuple)   # Output:(1, 2, 3, 4, 5, 6, 7, 8)

#13. Repeating Tuples:
repeated_tuple = my_tuple * 2
print(repeated_tuple)   # Output:(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

#14. Nested Tuples:
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple) # Output:((1, 2), (3, 4), (5, 6))

#15. Tuple Membership Test:
if (1, 2) in nested_tuple: # Output:(1, 2) exists in the nested tuple
    print("(1, 2) exists in the nested tuple")

print("------------------------------------------------------------------------")
        #Do Not Allow Duplicate,and unindexed,Duplicate Values will be removed..
         
set1 = {1, 2, 3}    
set2 = {3, 4, 5}

# Union     
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)  # Output: {3}

# Difference
print(set1 - set2)  # Output: {1, 2}

# Symmetric Difference
print(set1 ^ set2)  # Output: {1, 2, 4, 5}

# Set(eg program)
a={1,2,3,4,1}
print(a)     # Output:{1, 2, 3, 4}

#Add
a={1,2,3,4}
a.add(10)
print(a)    # Output:{1, 2, 3, 4, 10}

#Remove
a.remove(4)
print(a)    # Output:{1, 2, 3, 10}

#Pop
a={4,3,5,1} # Removes and returns the First element of the Set
a.pop()     # Sets are unordered..
print(a)    # Output:{2, 3, 4}

#update
a.update({0,10})
print(a)

print("------------------------------------------------------------------------")

# Creating a dictionary
my_dict = {
    "name": "Murugan",
    "age": 30,
    "city": "New York"
}
print(my_dict.keys())
print(my_dict.values())

# Accessing values using keys
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York

# Adding a new key-value pair
my_dict["gender"] = "Male"

# Modifying a value
my_dict["age"] = 32 #modify the age
my_dict.update({"age":32})

#pop
my_dict.pop("age")

# Removing a key-value pair
del my_dict["city"]

# Iterating over keys and values
for key, value in my_dict.items():
    print(key, ":", value)

#clear
my_dict.clear()
print(my_dict)

print("------------------------------------------------------------------------")

multilevel_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(multilevel_list[2])  # Output: [7, 8, 9]
print(multilevel_list[1][2])  # Output: 12

del multilevel_list[1]
print(multilevel_list)   # Output:[[1, 2, 3], [7, 8, 9]]









