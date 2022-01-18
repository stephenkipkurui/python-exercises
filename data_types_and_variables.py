# Python code Exercise Data Types, Operators, and Variables

# ---------------------------------------------------------(A)---------------------------------------------------------------

# Identify the data type of the following values:


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

#  What data type would best represent:

# A term or phrase typed into a search box?  [  ]
# If a user is logged in?  []
# A discount amount to apply to a user's shopping cart?  []
# Whether or not a coupon code is valid?  []
# An email address typed into a registration form?  []
# The price of a product?  []
# A Matrix?  []
# The email addresses collected from a registration form?  []
# Information about applicants to Codeup's data science program?  []

# You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know 
# yet if they're going to like it). If price for a movie per day is 3 dollars, how 
# much will you have to pay?


MOVIE_PRICE_PER_DAY = 3

days_little_mermaid =3

days_brother_bear = 5

days_hercules = 1


total_movies_price = ((MOVIE_PRICE_PER_DAY * days_little_mermaid) + (MOVIE_PRICE_PER_DAY * days_brother_bear) + (MOVIE_PRICE_PER_DAY * days_hercules))

print(total_movies_price)

