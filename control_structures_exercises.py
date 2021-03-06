# _________________________________PYTHON CONTROL STRUCTURES_______________________________

# Do your work for this exercise in a file named control_structures_exercises.py.


# 1. ---------------------------------Conditional Basics-----------------------------------
# a). prompt the user for a day of the week, print out whether the day is Monday or not
from turtle import position
from numpy import square


day = input('Enter day of the week: \n\t')

if day == 'Monday' or day == 'MONDAY':
    
    print(f'The day chosen is {day}') 
    
else:
    print('The day chosen is not monday')

# b). prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# week = ['Monday', 'Tuesday', 'Wednesday', 'Thusday', 'Friday','Satuday','Sunday']

day = input('\t\n Weekend or Weeekday? Enter a day of the week: \n\t')
                    
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
                
    print(f'The day: [ {day} ] is a weekday. Go to class/ Work:')
        
elif day == 'Tuesday':
                
    print(f'The day: [ {day} ] is a weekday. Go to class/ Work:')
        
        
elif  day == 'Wednesday':
                
    print(f'The day: [ {day} ] is a weekday. Go to class/ Work:')
        
elif day == 'Thursday':
                
    print(f'The day: [ {day} ] is a weekday. Go to class/ Work:')
        
elif day == 'Friday':
        
    print(f'The day: [ {day} ] is a weekday. Go to class/ Work:')

                
elif day == 'Saturday':
                
    print(f'{day} is a weeekend . You may sleep in.')
        
elif day == 'Sunday':
        
    print(f'{day} is a weeekend . You may sleep in.')
                
else:
                
    print('Data entered is neither weekday or weekend.')

# c). create variables and make up values for
#       -> the number of hours worked in one week
weekly_hours_worked = 0

#       -> the hourly rate
hourly_rate = 0.0

#       -> how much the week's paycheck will be
weekly_pay = weekly_hours_worked * hourly_rate

# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
print(''' [------- WEEKLY PAY CALCULATOR -------]
      
        This program calculates weekly employee pay.''')

hourly_rate = float(input('Enter pay rate: '))

weekly_hours_worked = int(input('Enter hours worked in a week: '))

if weekly_hours_worked > 40:
    
    overtime_hourly_rate = 1.5 * hourly_rate
    
    weekly_pay = overtime_hourly_rate * weekly_hours_worked
    
    print(f'Pay including overtime pay: {weekly_pay}')
    
else: 

    # weekly_hours_worked = int(input('Enter number of hours worked this week: '))

    # hourly_rate = float(input('Enter hourly rate: '))

    weekly_pay = (weekly_hours_worked * hourly_rate)

    print(f'You have worked {weekly_hours_worked} hours this week at the hourly rate of $: {hourly_rate}. Your total pay is: $ {weekly_pay}')

    print('[-------PROGRAM END -------]')

# 2. ------------------------------------Loop Basics---------------------------------------
# [A]. WHILE LOOPS

# -> Create an integer variable i with a value of 5.
i = 5

# -> Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:
    
# -> Each loop iteration, output the current value of i, then increment i by one.
    print(i)
    
    i += 1

# Your output should look like this:

# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15


# -> Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
count = 0

while count <= 100:
    
    print(count, '\n')
    
    count += 2


# -> Alter your loop to count backwards by 5's from 100 to -10.
count = 100

while count >= -10:
    
    print(count, '\n')
    
    count -= 5


# -> Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
initial_num = 2
final_num = 1000000

while initial_num <= final_num:
        
    print(initial_num)
    
    initial_num = (initial_num * initial_num)
    
    
    
#  2
#  4
#  16
#  256
#  65536


# -> Write a loop that uses print to create the output shown below.

num = 100

end_num = 5


while end_num <= num:
    
    print(num)
    
    num -= 5



# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5


# [B]. FOR LOOPS
# i). Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

number = int(input('Enter a number'))

for n in range(1, number):
    
    count = int(n)
    
    print(f'{number} X {n}  = {number * count}')

# For example, if the user enters 7, your program should output:

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# ii). Create a for loop that uses print to create the output shown below.



num = int(input('Enter size: '))

for n in range (1, num):
    
    print(int(str(n) * n))    
    
    
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# [ ------ Not Correct result---------]
num = int(input('Enter size: '))

for n in range(num):
    
    for c in range (n + 1):
        
        print(f'{n}', end ='')
    
    print()
    
# [ ------ Not Correct result---------]



# [C]. BREAK AND CONTINUE

# i). Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user 
# if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue 
# statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# Your output should look like this:

num = input('Enter an odd number between 1 and 50: ')

while num.isdigit():
    
    num = num
    
    while num in range(1, 50):
            
        if num % 2 == 1:
       
            print(f'Here is the odd number: {num}')
                
            num += 1
                
            if num == num:    
                print(f'Yikes! Skipping number {num}')
                    
                continue
            else:
                
                print('Entered number must be odd and a digit')
        else:
            print('Number must be between 1 and 50. Enter odd number between 1 and 50: \n')
            
            print('----------- Re-run the code and enter the corrent range of numbers-----------')
            
            break
    else:
        
        print('The number entered is not in the range 1 : 50. Enter number within 1 & 50: ')
        
        num = input('Try again: Number must be between 1 and 50:')                
else:
    
    print(f'{num} is not a number: Try again')  
    
    num = input('Enter ONLY NUMBERS (odd number) between 1 and 50: ')


#--------------------------------Correct Answer Start------------------------------

while True:
    
    pos_num = input('Enter odd number between 1 : 50: ')
    
    if pos_num.isdigit():
        
        if int(pos_num) % 2 == 1 and int(pos_num) <= 50:
            break
pos_num = int(pos_num)

for num in range(1, 50, 2):
    if num == pos_num:
        print('Yikes! skipping number: ', num)
    else:
        
        print('Here is an odd number: ', num)
    
#--------------------------------Correct Answer End--------------------------------

    
# Number to skip is: 27

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49


# d). The input function can be used to prompt for input and use that input in your python code. Prompt the user 
# to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the 
# value the user entered is a valid number, also note that the input function returns a string, so you'll need to 
# convert this to a numeric type.)


number = int(input('Enter number greater than 0: '))


while number > 0:
    
    for c_count in range(0, number):
    
        print(c_count)
        
        c_count += 1
        
        if c_count == number:
        
            break


# e). Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from
# the number the user entered down to 1.
number = int(input('Enter number greater than 0: '))


while number > 0:
    
    for c_count in range(0, number):
    
        print(c_count)
        
        c_count -= 1
        
        if c_count == number:
        
            break


# 3. ---------------------------------------Fizzbuzz----------------------------------------------
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, 
# the test is designed to test basic looping and conditional logic skills.

# -> Write a program that prints the numbers from 1 to 100.
# -> For multiples of three print "Fizz" instead of the number
# -> For the multiples of five print "Buzz".
# -> For numbers which are multiples of both three and five print "FizzBuzz".

for item in range(1, 100 + 1):
    if (item % 3 == 0) and (item % 5 == 0):
        
        print('Fizzbuzz')
        
    elif item % 3 == 0:
        print('Fizz')
        
    elif item % 5 == 0:
        print('buzz')
        
    else:
        print(item)

# 4. ----------------------------------Display a table of powers----------------------------------
# -> Prompt the user to enter an integer.
# -> Display a table of squares and cubes from 1 to the value entered.
# -> Ask if the user wants to continue.
# -> Assume that the user will enter valid data.
# -> Only continue if the user agrees to.
# ----------------------Instructor Code: Exercise Review Start------------------------
while True:
    posited_num = input('Please insert a positive integer: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
proceed = input('Do you want to continue and print a table of powers? :')
if proceed.lower().startswith('y'):
    posited_num = int(posited_num)
    print()
    print('number | squared | cubed')
    print('------ | ------- | -----')
    for i in range(1, posited_num + 1):
        i_squared = i ** 2
        i_cubed = i ** 3
        print(f'{i: <6} | {i_squared: ^7} | {i_cubed: 5}')
        
# ----------------------Instructor Code: Exercise Review End--------------------------


# Example Output

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125
# Bonus: Research python's format string specifiers to align the table


# 5. --------------------------Convert given number grades into letter grades-----------------------
# -> Prompt the user for a numerical grade from 0 to 100.

score = int(input('What is your score: '))

if score <= 59:
    
    print('You scored an F:')
elif score >= 60 and score <=66:
    
    print('Score D')
elif score >= 67 and score <= 79:
    
    print('Scored C')
    
elif score >= 80  and score <= 88:
    print('Scored B')
    
elif score  >= 88 and score <= 100:
    
    print('Scored A')
    
else: 
    print('Invalid entry')
    
    score = int(input('What is your score: '))

# -> Display the corresponding letter grade.
# -> Prompt the user to continue.
# -> Assume that the user will enter valid integers for the grades.
# -> The application should only continue if the user agrees to.
# -> Grade Ranges:
#       A : 100 - 88
#       B : 87 - 80
#       C : 79 - 67
#       D : 66 - 60
#       F : 59 - 0


# ----------------------------------------------BONUS----------------------------------------------
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).




# 6. -----Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. Loop through the list and 
# print out information about each book.-------------------------------------------------------------

# ----------------------Instructor Code: Exercise Review Start--------------------------
bookshelf = [
    {'title': 'Annihilation',
     'author': 'Jeff Vandermeer',
     'genre': 'Science Fiction'},
    {'title': 'Octopus Pie',
     'author': 'Maredeth Gran',
     'genre': 'Comic'},
    {'title': 'Cabin At the End of the World',
     'author': 'Paul Tremblay',
     'genre': 'Horror'},
    {'title': 'Severance',
     'author': 'Ling Ma',
     'genre': 'Science Fiction'},
]
    
for book in bookshelf:
    print('we are living in a single dictionary here')
    [print(key, ': ', book[key]) for key in book]
    print('------')
    
picked_genre = input('Please pick a genre and I will return the titles of that genre on shelf. \n')
   
matches = []
for book in bookshelf:
    if book['genre'].lower() == picked_genre.lower():
        matches.append(book['title'])
if matches == []:
    print('no books in that genre available. please check back later')
else:
    print(f'I have the following titles in the genre {picked_genre}')
    [print(match) for match in matches]


# ----------------------Instructor Code: Exercise Review End----------------------------





# a). Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.