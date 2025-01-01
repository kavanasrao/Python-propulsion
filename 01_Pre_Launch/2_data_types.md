# Data_Type 

"Data types are like the material or shape of the jars in your kitchen that determine what they can hold. For example, a steel jar might be ideal for storing grains, a glass jar for spices, and a plastic jar for dry snacks. In programming, data types define what kind of data a variable can store, such as numbers, text, or true/false values."
<hr>

**Built-in Data types**

In programming, data type is an important concept

Variables can store data of different types, and different types do different things 

 Text Type      :        str <br>
 Numeric type   :        int, float, complex <br>
 Sequence Type  :        list, tuple, range <br>
 Mapping type   :        dict <br>
 set type       :        set, frozen_set <br>
 Boolean type   :        bool <br>
 Binary type    :        bytes, byte_array, memory_view <br>
 None type      :        NoneType <br>

# Numeric Type:

## Complex 

Complex numbers are written with a "j" as the imaginary part

## Type Conversion :

You can convert from one type to another with the int(), float() and complex() methods

<hr>

## Python Casting :

In Python Casting refers to converting a variable from one data type to another. Python provide built-in functions to perform these conversion 

- Implicit Casting(Automatic Conversion):

    Python automatically Converts one data type to another when it is safe to do 

                x = 5
                y = 3.5
                add = x + y      # implicitly converted to  float
                print(add)       # output : 8.5
                print(type(add)) #Output : <class float>


- Explicit Casting(Manual Conversion):
we can manually convert one data type to another using Python's type casting functions

                x = 3.14
                print(type(x)) # output: <class float>
                y = int(x)
                print(y)       # output : 3
                print(type(y)) # output: <class int>

             

