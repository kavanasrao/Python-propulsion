basket = ("apple","orange","tomato","potato","curd","milk")

# 1. Access tuple items :

        # Method 1 by indexing :

bill_item_1 = basket[4]
print(bill_item_1)

        # Method 2 Negative Indexing :
        
bill_item_2 = basket[-1]
print(bill_item_2)

        # Method 3 Range of indexing :
        
bill_item_3 = basket[2:5]
print(bill_item_3)

        # Method 4 range of negative indexing  :
        
bill_item_4 = basket[-4 : -1]
print(bill_item_4)

        # check if item exits 
        
if "potato" in basket :
    print("Yes, 'potato' is in the basket ")
    
    

# *********************************************************************************

# 2 Tuples are immutable to update it this are some method 

        # changing the Tuple to list again to Tuple
        
        
        

X = ("apple","banana","cherry")

y = list(X)

y[1] = "kiwi"
 
X = tuple(y)

print(X)


        # Add tuple to another tuple 
        
        
z = ("melon",)

X += z

print(X)




# ********************************************************************************************************************************

# Similarly we can't remove the items from tuple so convert it to list remove item again convert it to tuple 

# or we can delete entire tuple using {del}


# *********************************************************************************************************************************


# 3 unpacking tuple using variables 

A = ("Apple","banana","melon")

(alpha,beta,gamma) = A


# or  using Asterisk which creates list 

(zeta,*delta) = A       # for more  refer tuple.md


print(alpha,beta, gamma)

 
 # *********************************************************************************************************************
 
# 4. Join Tuples :

        # using '+' operator
        
        
tuple_1 = ("a","b","c","d")

tuple_2 = (1,2,3,4,5)

tuple_3 = tuple_1 + tuple_2

print(tuple_3)


        # using '*' operator 
    
my_tuple = tuple_1*3

print(my_tuple)   


# ***************************************************************************************************


 