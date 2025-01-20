# Condition statement

A Condition statement is a logical expression used to determine whether a particular block of code should execute.<br>
It evaluates to a boolean value, either True or False, 

<hr>

## if_statement :

An if statement is written by using 'if Keyword'

                a = 40
                b = 30
                if a > b :
                    print(f'a = {a} is greater than b = {b}')

<hr>

## if_else_statement :

The Else Keyword  catches anything which isn't caught by preceding conditions('if / elif ')

                age = int(input("Enter Your age : "))
                if age > 18 :
                    print("You can have voter_ID")
                else :
                    print("You are eligible")



<hr>

## if_elif_else_statements(if_elif ladder):

The 'elif' keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

                marks = float(input(" Enter the marks : "))
                if marks < = 30 :
                    print("Better luck Next Time....")

                elif marks >=30 :
                    print(" Cleared but not selected " )

                elif marks >= 50 :
                    print(" Congrats ! selected to next round ")

                else :
                    print("try again ")

<hr>

## Nested If :

if statement inside if statement, this is called nested if statement.

                age = 41 

                if age > 10:
                    print(" Above Ten ")

                    if age > 20 :
                        print("and also above 20! ")

                    else :
                        print(" but not above 20 ")


<hr>

## Short Hand If :

If only one statement to execute, we can put it on the same line as the if statement

                example :

                    if a > b : print(" a is greater than b")


<hr>

## Short Hand If_else :

The one_line if_else statement is called a Ternary Operator or Conditional Expression.
It's concise way too perform an action based on a condition 

                Syntax :

                <true_value> if <condition> else <false_value>

                a = 20
                b = 330
                print(f'A is greater {a}') if a > b else print(f'B is greater {b}')

