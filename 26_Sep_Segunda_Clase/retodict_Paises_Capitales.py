# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:33:59 2023

@author: LCO
"""

COUNTRY =  {"Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"}
          

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3
 capitals. Therefore, we embed a list inside
the dictionary.
"""

CAPITALS = {"Brazil": "Brasilia",
            "Russia": "Moscow",
            "India": "New Delhi",
            "China": "Beijing",
            "South Africa": 
                        
                        {"Pretoria",
                        "Cape Town",
                        "Bloemfontein"}
           }

#Print the list and dictionary
print( COUNTRY )
print( CAPITALS)
"""
What response did you get?
Why did the list and dictionary
 contents not print?
Fix the code and run the script again.
"""

print( CAPITALS["South Africa"](1))
"""
Why did you get an error for the
 2nd capital of South Africa?
Hint: Check the syntax for the 
index value.
"""