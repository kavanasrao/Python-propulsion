# Dictionary

Dictionaries are used to store the data values in key : value pairs.

A dictionary is a collection which is ordered, changeable and don not  allow duplicates.

Dictionaries are written in curly brackets, and have keys and values

                Example :

                this_dict = {
                    "brand"  : "Ford"
                    "model" : "Mustang"
                    "year" : 1964
                }



<hr>

#  Nested Dictionaries

A dictionary can contain dictionaries, this is called nested dictionaries

            Students = {
                "Stud1" :{
                    "name" : "harry"
                    "age"   : 8
                }

                "stud2" : {

                    "name" : "John"
                    "ag" : 9
                }

                "stud3" : {
                    
                    "name" : "emily"
                    "age"   : 8
                }
            }

            print(Students["stud3"][name])