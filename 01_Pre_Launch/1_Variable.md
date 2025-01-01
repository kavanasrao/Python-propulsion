# Python Variables

## Variables: 

"Variables are like containers that store data values, where each container (variable) is labeled with a name, much like different types of containers in a kitchen hold specific ingredients."

A variable is created the moment you assign the value to it 

**example**
            X = 5
            print(X)

here X Container which holds the value 5 in memory space
A variable can have short name or descriptive name

**Rules for Python variables :**

- Variables names are case-Sensitive.
- Variables must start with letters or underscore characters
- A Variable name can only contain alpha-numeric  characters and underscores (A-Z, 0-9, and _)
- A variable name cannot be any of the [Python_Keyword](Python_Keyword.md)

**Example :**
 
 *Legal Variable names*

                myvar = "Jhon"
                my_var = "Jhon"
                _my_var = "Jhon"
                myVar = "Jhon"
                MYVAR = "Jhon"
                myvar5 = "jhon"

 *Illegal Variable names*

                2myvar = "Jhon"
                my-var = "jhon"
                my var = "jhon"

**Multi Words  Variable Names**

 
"Variable names with more than one word can be difficult to read, especially when working in a group. Several techniques can address this issue."
 
###  Camel Case:
 Each word, except the first starts with capital letter:

                myVariableName = "ABCD"

###  Pascal Case :
 Each word start with capital letter:

                MyVariableName = "ABCD"

###  Snake Case :
Each word is separated by an underscore Character:

                my_variable_name = "abcd"


## Assign Multiple Values :

**Many Values to Multiple Variables :**

Python allows you to assign values to multiple variables in one line

**Example**

                X, Y, Z = "Orange", "Banana", "Cherry"

***Note :*** 
 *Number of Variables must matches with number of Values*


**Unpack A Collection :**

Python allows to extract the values from collection into variables. This is called *unpacking*
**Example**

                fruits = ["Apple","banana", "cherry"]
                X, Y, Z = fruits
            

**### Global Variables**
Variables that are created Outside *function* are known as Global variable

**Example :**

                X = "Awesome"

                def myfunc():
                    print("python is " + X) 
                
                myfunc()

**### Local Variables**

Variables that are created inside *function* are known as Local variable and it can be used only inside the function

**Example :**

                def myfunc():
                    X = "Awesome"
                    print("python is " + X) 
                
                myfunc()

***Note***
    If we want to use local variable outside the function,*'global'* keyword can be use

                    def myfunc():
                        global X
                        X = "fantastic"

                    myfunc() 
                    print(" Python is" + X)

                    output : Python is fantastic


## Identifiers : 

"Identifiers are like labels on jars in your kitchen. Each label (identifier) helps you recognize what the jar contains, like 'Sugar,' 'Flour,' or 'Salt.' Similarly, in programming, identifiers name variables, functions, or other elements to identify them uniquely."