# create your the List 

fruits = ["apple", 'banana',"cherry"]


# 1. get the length of list 

length_of_list = len(fruits)

print(length_of_list)

# *********************************************************************************************************

# 2. access the element index value :

    # Method 1 Using the index():
    
position = fruits.index("banana")
print(position)

    # Method 2 Using the count()
    
if fruits.count("banana") > 0 :
    position = fruits.index("banana")
    print(f"The first occurrence of 'banana' is at the index {position}")

else :
    print("The item is not in the list. ")
# ************************************************************************************************************************


# 3 add fruits to the list at the end of list using different methods

        # Method 1 Using append()

fruits.append("orange")
print(fruits)

        # Method 2 Using extend()
        
fruits.extend("berry")
print(fruits)


# ***************************************************************************************************************************


# 4. add item to the list to specific index 

fruits.insert(1,"mango")
print(fruits)


# **************************************************************************************************************************************

# 5 To delete the items in the list : 

    # method 1 To remove the item in the specified position
removed_item = fruits.pop(0)
print(removed_item)
print(fruits)

     # Method 2 using remove() for specified position :
     
fruits.remove("banana")
print(fruits)

    # Method 3 to Remove all the elements from the list :
    
fruits.clear()
print(fruits)

# *********************************************************************************************************************

# 6. Reverse the list :

new_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_list.reverse()
print(new_list)

#***********************************************************************************************************************************

# 7. Sort the list :
 
new_list.sort()
print(new_list)

# ********************************************************************************************************************************************

# 8. print type of collection

print(type(fruits))
print(type(new_list))


# ********************************************************************************************************************************************

# Output : 

# 3
# 1
# The first occurrence of 'banana' is at the index 1
# ['apple', 'banana', 'cherry', 'orange']
# ['apple', 'banana', 'cherry', 'orange', 'b', 'e', 'r', 'r', 'y']
# ['apple', 'mango', 'banana', 'cherry', 'orange', 'b', 'e', 'r', 'r', 'y']
# apple
# ['mango', 'banana', 'cherry', 'orange', 'b', 'e', 'r', 'r', 'y']
# ['mango', 'cherry', 'orange', 'b', 'e', 'r', 'r', 'y']
# []
# [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# <class 'list'>
# <class 'list'>



