# Tuple 

A tuple is a collection which is ordered  and unchangeable. Which are written with round brackets. 
Once tuple are created cannot change its value it is called as immutable

                my_tuple = ("apple","banana","cherry")
                print(my_tuple)

Tuple items are indexed, the first item has indexed [0], the second item has index[1] etc.

<hr>

**Access tuple items by indexing :**
- *Index method :*

                fruits = ("apple","banana","cherry")
                print(fruits[1])
                # output ~ apple

- *using negative Indexing :*

                fruits = ("apple","banana","cherry")
                print(fruits[-1])
                # output ~ "cherry"

- *Range of index :*

            fruits = ("apple", "banana","cherry","orange","kiwi","melon","mango")
            print(fruits[2:5])
            # output ~ ("cherry","orange","kiwi")

<hr>

**Methods of Tuple :**

- append("item") 
- can add two tuples using "+"
- remove("item")
- del()  ~ del keyword can delete the tuple completely 
- count() 
- index()

<hr>

# Note : 

If the Number of variables is less than the number of values, an **ASTERISK** (*) can be added to the variable name and the values will be assigned to the variable as a list  

