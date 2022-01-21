# --------------------------------PYTHON FUNCTIONS EXERCISES----------------------------

# Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.

# 1). Define a function named is_two. It should accept one input and return True if the passed input is either 
# the number or the string 2, False otherwise.

from zmq import constants


def is_two(data_in):
    "This function compares the data types to string and integer and return True or false"
    if type(data_in) == int or type(data_in) == str:
    
        return True
    #Else statement is above is incorrect
    else:
        return False
# Call to the function
is_two(4) 

# 2). Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise. ********************
vowels = ['a', 'e', 'i', 'o', 'u']    

def is_vowel(vowels):
    "Function to evaluate if input is a vowel or not"
    for v in vowels:
        # compares iterations with each individual vowels
        if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
            
            return True
        else:
            return False 
# call to the function
is_vowel('a')

# 3). Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this. ************* not utilizing is_vowel()******************
def is_consonant(str_input):
    " Function to compare where the listed items are consonant"
    if str_input not in is_vowel(vowels):
        return True
    
    else:
        return False
    
is_consonant('')
    


# consonants = ['b', 'c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

# def is_consonant(consonants):
    
#     for cns in consonants:
        
#         if cns not in consonants:
            
#             return True
#         else:
#             return False 
        
# is_vowel('a')
        
    
# 4). Define a function that accepts a string that is a word. The function should capitalize the first 
# letter of the word if the word starts with a consonant.******************

def captalize_consonants(words):
    
    constants =  is_consonant()
   
    word_split = words.split()
    
    if word_split[0] in constants:
        
        return True
    
    else:
        return False
  
captalize_consonants('Hello there')


# 5). Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.

def calculate_tip(tip, bill):
    
    if tip > 1 or tip < 0:
        
        print('Tip has to be between 0 and 1')
    else:
        
        return ("The total bill is: $",tip * bill)
    
calculate_tip(0.5, 56)
    
    
# 6). Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.
def apply_discount(original_price, discount_percentage):
    
    discount = (discount_percentage / original_price)
    
    total_price = discount + original_price
    
    return ("The price including discount is: $",round(total_price, 2) )
    
apply_discount(56.67, 0.6)


# 7). Define a function named handle_commas. It should accept a string that is a number that contains commas 
# in it as input, and return a number as output.
def handle_commas(stringed_number):
    
    convert_string_to_num = int(stringed_number)
    
    add_commas = format(convert_string_to_num, ',.2f' )
    
    return add_commas

handle_commas('23435')


# 8). Define a function named get_letter_grade. It should accept a number and return the letter grade associated 
# with that number (A-F).
def get_letter_grade(num_input):
    if num_input < 60:
        return 'F'
    elif num_input >= 60 and num_input <= 69:    
            return 'E'                
    elif num_input >= 70 and num_input <= 79:         
           return 'D'  
    elif num_input >= 80 and num_input <= 89:       
            return 'C'              
    elif num_input >= 90 and num_input <= 95: 
      return 'B'
    elif num_input >= 96 and num_input <= 100:         
            return 'A'        
    else: 
        print('Score has to be between 0 and 100')
            
get_letter_grade(67)
    
# 9). Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string_input):
    
    vowels = ('a','e','i','o','u')
    
    letter_char = list(string_input)
    
    for i in string_input.lower():
        
        if i in vowels:
            
            new_string = string_input.replace(i, '')
            
    return new_string
       
           
remove_vowels('fsdnsdnsdsd asdsdasas')
    

# 10). Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:


#   -> anything that is not a valid python identifier should be removed
#   -> leading and trailing whitespace should be removed
#   -> everything should be lowercase
#   -> spaces should be replaced with underscores

def normalize_name(string_input):
    
    py_identifier  = ('_','0','1','2','3','4','5','6','7','8','9','b', 
                      'c','d','f','g','h','j','k','l','m','n','p','q',
                      'r','s','t','v','w','x','y','z', 'a', 'e', 'i', 'o', 'u',
                      'B','C','D','F','G','G','H','K','L','M','N','P','Q',
                      'R','S','T','V','W','X','Y','Z', 'A', 'E', 'I', 'O', 'U', '#', '.','`','"','""', '')
    
    for items in string_input:
        
        if items not in  py_identifier:
            
            remove_non_identifier = string_input.replace(items, '')

    string_lower = remove_non_identifier.lower()
    
    replace_white_space = string_lower.replace(" ", "_")
    
    strip_leading_trail_space = replace_white_space.strip(" ")
  
    return strip_leading_trail_space
    
    
normalize_name('SssdsferD sdsda')
# 
#   for example:
#       -> Name will become name
#       -> First Name will become first_name
#       -> % Completed will become completed
# 
# 11). Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#   -> cumulative_sum([1, 1, 1]) returns [1, 2, 3]

#   -> cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
num_list = [1, 2, 3, 4, 6, 8, 9, 23, 4, 1, 86]


import itertools

def cummulative_sum(num_list):
    
    return list(itertools.accumulate(num_list))

        
cummulative_sum(num_list)
    
    
# 
# 
# ------------------------Additional Exercise------------------------------

# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.
# Bonus




# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27


