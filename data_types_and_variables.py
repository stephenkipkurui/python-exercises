# Python code Exercise Data Types, Operators, and Variables

# ---------------------------------------------------------(A)---------------------------------------------------------------

# [Q]:Identify the data type of the following values:


# 99.9   [ Float ]

# "False" [ String ] 

# False [ Boolean ]

# '0' [ String literal ]

# 0 [ Integer ]

# True [ Boolean ]

# 'True' [ Boolean ]

# [{}]   [ List with nested dictionary ]

# {'a': []} [ dictionary ]

# ---------------------------------------------------------(B)---------------------------------------------------------------
#  [Q]: What data type would best represent:

# A term or phrase typed into a search box?  [ String ]
# If a user is logged in?  [ Booleans ]
# A discount amount to apply to a user's shopping cart?  [ Float ]
# Whether or not a coupon code is valid?  [ Booleans  ]
# An email address typed into a registration form?  [  string ]
# The price of a product?  [ Float ]
# A Matrix?  [ List ]
# The email addresses collected from a registration form?  [  String ]
# Information about applicants to Codeup's data science program?  [  Dictionary  ]

# ---------------------------------------------------------(C)---------------------------------------------------------------
# For each of the following code blocks, read the expression and predict what the result 
# of evaluating it would be, then execute the expression in your Python REPL.


from atexit import register


'1' + 2  # [invalid SyntaxError] TypeError

6 % 4 # 0

type(6 % 4) # [ Int ]

type(type(6 % 4))  # Type

'3 + 4 is ' + 3 + 4  # TypeError

0 < 0  # False

'False' == False  # False

True == 'True' # False

5 >= -5 # True

True or "42"  # True

6 % 5   #1

5 < 4 and 1 == 1  # False

'codeup' == 'codeup' and 'codeup' == 'Codeup' #True

4 >= 0 and 1 !== '1' # Syntax Error / Invalid syntax

6 % 3 == 0 # True

5 % 2 != 0  # True

[1] + 2   # TypeError: can only concatenate list (not "int") to list

[1] + [2]  # [1,2]

[1] * 2 #[1,1]

[1] * [2] # TypeError: can't multiply sequence by non-int of type 'list'

[] + [] == []  # True

{} + {}  #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'


# ---------------------------------------------------------(D)---------------------------------------------------------------

# You have rented some movies for your kids: The little mermaid (for 3 days),  
# # Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know 
# yet if they're going to like it). If price for a movie per day is 3 dollars, how 
# much will you have to pay?


MOVIE_PRICE_PER_DAY = 3

days_little_mermaid =3

days_brother_bear = 5

days_hercules = 1


total_movies_price = ((MOVIE_PRICE_PER_DAY * days_little_mermaid) + (MOVIE_PRICE_PER_DAY * days_brother_bear) + (MOVIE_PRICE_PER_DAY * days_hercules))

print(total_movies_price)

#[ TOTAL PRICE: 27 ] 

# ---------------------------------------------------------(E)---------------------------------------------------------------
# [Q]: Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they
# pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook
# 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.

total_salary = 0

weekly_google_hours = 6
weekly_facebook_hours = 10
weekly_amazon_hours = 4
total_hours_worked = (weekly_facebook_hours + weekly_amazon_hours + weekly_google_hours)

google_pay_rate = 400
amazon_pay_rate = 380
facebook_pay_rate = 350

total_weekly_pay_google = (weekly_google_hours * google_pay_rate)

total_weekly_pay_facebook = (weekly_facebook_hours * facebook_pay_rate)

total_weekly_pay_amazon = (weekly_amazon_hours * amazon_pay_rate)

total_salary = (total_weekly_pay_google + total_weekly_pay_amazon +  total_weekly_pay_facebook)

print(f"The total salary earned is $:  {total_salary}.")

# $7420


# ---------------------------------------------------------(F)---------------------------------------------------------------
# A student can be enrolled to a class only if the class is not full and the class schedule 
# does not conflict with her current schedule.
CLASS_FULL = True
CLASS_NOT_FULL = False

CONFLICT_SCHEDULE = True
NON_CONFLICT_SCHEDULE = False

if CLASS_NOT_FULL == True and NON_CONFLICT_SCHEDULE == True:
    
    register_student()
    
elif CLASS_FULL and CONFLICT_SCHEDULE:
    
    deny_registeration()
        
elif CLASS_NOT_FULL and CONFLICT_SCHEDULE:
    
    print('Class is not full but there is a conflict in the schedule. Please check the schedule again.')
    
elif CLASS_FULL and NON_CONFLICT_SCHEDULE:
    
    print('Class is full, you cannont be added to this class.')

else:
    
    print('You did not choose any class or schedule. You must choose both')


def register_student(name, student_id, subject, grade):
    name = input('Enter student name: ')
    student_id = input('Enter student ID: ')
    subject = input('Enter student Subject: ')
    grade = input('Enter grade: ')
    
    return name, student_id, subject, grade
    
    
def deny_registration(student_id):    
    print('Student cannot register this class. Contact course register.')
    return student_id
# ---------------------------------------------------------(G)---------------------------------------------------------------
# A product offer can be applied only if people buys more than 2 items, and the offer has not
# expired. Premium members do not need to buy a specific amount of products.
product_bought_count = 0

OFFER_EXPIRED = True
OFFER_CURRENT = True

if product_bought_count > 2 and OFFER_CURRENT:
    
    offer_product_discount()
        
elif premium_member(): 
    
    offer_product_discount()

elif product_bought_count <= 2:
    
    no_offers() 
        
else:
    
    print('To qualify for offers, you need to buy 2 or more items or upgrade to premium customer.')    


def offer_product_discount():
    
    print('You qualify for product offer')
    
def no_offers():
    
    print('No special offers at this time')
# ---------------------------------------------------------(H)---------------------------------------------------------------
username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
if len(password)  >= 5:
    
    password_length = True

# the username must be no more than 20 characters
if len(username) >= 20:
    username = False
else:
    username = True

# the password must not be the same as the username
if password == username:
    
    unacceptable_password = True
else:
    
    unacceptable_password = False

# bonus neither the username or password can start or end with whitespace

stripped_password = password.strip()
stripped_username = username.strip

if (stripped_password or stripped_username) == True:
    
    password_and_username = password
    
else:
    
    password_and_username != password 