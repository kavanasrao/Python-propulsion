# Python Strings 

# String - str( Text Type ): 

A string is a data type used to store a sequence of characters, including letters, numbers, symbols, or spaces. Strings are enclosed within quotation marks, either single (') or double ("), in Python and many other programming languages.
    
                example : 

                name         =   "Python_Coding"      # A string containing letters
                greeting     =   'Hello!'             # A string with punctuation
                num_as_text  =   "123"                # Numbers stored as a string

**Quotes Inside Quotes :**
we can use quotes inside a string, as long as they don't match the quotes surrounding the string

                Example :

                print("It's alright")

<hr>

**Key Features of String :**
- Strings are *Immutable* : 
        - Means Once string is created, it cannot be modified
        - Every operations, actually creates a new String

- Strings are *Ordered Sequences* :
        Means they support indexing and slicing. Index starts at 0

- String Support *Concatenation*
- Strings are *Case_Sensitive* 
- Strings Supports *Iteration*

<hr>

**Multiline Strings**
We can Assign a multiline string to a variable by using three quotes

                examples :

                 a = """ Lorem ipsum dolor sit amet,
                        consectetur adipiscing elit,
                        sed do eiusmod tempor incididunt
                        ut labore et dolore magna aliqua.."""
                print (a)

<hr>

**String Slicing**
We can return the range of characters by using the slice syntax

Specify the the start index and end index, separated by a colon, to return a part of the string 

**Note :** In Python, and almost every coding languages index start with 0 and count space 

                alp = "A, B, C, D, E, F, G, H, I, J, K, L,M, N, O, P, Q, R"
                print(alp[:51]) # to get all the string
                # Slice from start(index 0)

<hr>

**Negative Indexing :**
Use negative indexes to start the slice from the end of the string:

                alp = "A, B, C, D, E, F, G, H, I, J, K, L,M, N, O, P, Q, R"
                print(alp[-50:-2])

<hr>

**String Concatenation :**
To Concatenate, or combine, two strings we can use the + operator.

                Merge variable a with variable b into C:

                a = "Hello"
                b = "World"
                c = a + b
                print(c)
                # output - Hello World

<hr>

**String Format :**
we cannot combine String and numbers using Concatenation
but we can combine strings and numbers by using f-string or the format() method!

                age = 36
                txt = "My name is Jhon, I am " + age # throws error

**F-Strings :**
F-String was introduced in python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

                age = 36
                txt = f"My name is Jhon, I am {age}"
                print(txt)

                # output ~ My name is Jhon, I am 36

**Modifiers :**
A Modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals

                price = 59 
                txt = f"The price is {price:.2f} ₹"
                print(txt)
