# ------------------------------PYTHON IMPORT EXERCISES----------------------------------

# You will need to use imports to complete each exercise
# in addition, these exercise will strengthen your problem solving and python coding skills.

# You will be directed to create specific files in part 1, for the rest you may do your work in either import_exercises.py or import_exercises.ipynb.

# 1). Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

#       a). Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
from functions_exercises import calculate_tip as tip_calculator
from itertools import combinations
from itertools import permutations
from functions_exercises import is_vowel as vowels_functions

vowels_functions('H')

#       b). Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.
# import functions_exercises 
tip_calculator(0.7, 100)

#       c). Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function 
#           and give it an alias. Test this function in your notebook.
from functions_exercises import get_letter_grade as grade_score

grade_score(78)

#   DIRECTIONS == Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in.

 
# 2). Read about and use the itertools module from the python standard library to help you solve the following problems:

#   --> How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import permutations

my_list = 'abc123'

p = permutations(my_list)

for i in list(p):
    print(i)

#   --> How many different combinations are there of 2 letters from "abcd"?

letter = 'abcd'

letter_2_combinations = combinations(letter, 2)

ltr = [' '.join(i) for i in letter_2_combinations]

print(ltr)


#   --> How many different permutations are there of 2 letters from "abcd"?

letters = 'abcd'

permute_letters = permutations(letters, 2)

for index in list(permute_letters):

    print(index)

# [ 12 Combinations ]


# 3). Save this file as profiles.json inside of your exercises directory(right click -> save file as...).

# Use the load function from the json module to open this file.

import json
json.load(open('profiles.json'))


# Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

#   --> Total number of users
#   --> Number of active users
#   --> Number of inactive users
#   --> Grand total of balances for all users
#   --> Average balance per user
#   --> User with the lowest balance
#   --> User with the highest balance
#   --> Most common favorite fruit
#   --> Least most common favorite fruit
#   --> Total number of unread messages for all users
