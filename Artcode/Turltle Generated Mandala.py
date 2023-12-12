import turtle
import random

# Get user input
age = int(input("What is your age? A close number is acceptable: "))
favorite color = input("What is your favorite color? ")
favorite movie = input("What is your favorite Movie, Book, or Video game? ")
favorite song = input("What is your favorite Song? ")
Pet = input("What is your pet's name? (You can make a name up if needed) ")
skill = input("If you could instantly master any skill, what would it be? ")
hobby = input("What is your favorite Hobby? ")

# Calculate lengths
favoriteColor2 = len(favorite color)
favoriteMovie2 = len(favorite movie)
favoriteSong2 = len(favorite song)
Pet2 = len(Pet)
skill2 = len(skill)
hobby2 = len(hobby)

# Set up turtle
wn = turtle.Screen()
bob = turtle.Turtle()
turtle.speed(0)

# Draw a pattern based on user input
for _ in range(age):
    bob.right(20 + Pet2)
    bob.forward(20 + skill2)
    bob.left(25 + hobby2)
    bob.forward(100 + favoriteColor2)
    bob.left(180 + favoriteMovie2)
    bob.forward(50 + favoriteSong2)
    bob.right(20 + Pet2)
    bob.forward(20 + skill2)
    bob.left(25 + hobby2)
    bob.forward(100 + favoriteColor2)
    bob.left(180 + favoriteMovie2)
    bob.forward(50 + favoriteSong2)

# Finish drawing
turtle.done()










