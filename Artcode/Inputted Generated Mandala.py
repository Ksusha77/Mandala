import turtle
import random
#Takes inputs in the form of a string or intergers
def UserInfom():
print("It is said the Mandala is a symbol of the self, the lines and shapes are universal among mankind")
print("Tell me about yourself")
age = int(input("What is your age? A close number is acceptable: "))
favoriteColor = input("What is your favorite color")
favoriteMovie = input("What is your favorite Movie, Book, or Video game")
favoriteSong = input("What is your favorite Song?")
Pet = input("What is your pet's name (You can make a name up if needed)")
skill = input("If you could instantly master any skill, what would it be?")
hobby = input("What is your favorite Hobby?")
month = int(input("Number of the month you were born"))
day = int(input("Number of the day of the month you were born"))
#Converts the strings into numbers using the len() function
favoriteColor2 = len(favoriteColor)
favoriteMovie2 = len(favoriteMovie)
favoriteSong2 = len(favoriteSong)
Pet2 = len(Pet)
skill2 = len(skill)
hobby2 = len(hobby)
x = 0

wn = turtle.Screen()
bob = turtle.Turtle()
turtle.speed(0)

#Draws turtles based on the various inputs. 



for _ in range(age):
    bob.right(month * Pet2 + x)
    bob.forward(month * skill2 + x)
    bob.left(month * hobby2 + x)
    bob.forward(month * favoriteColor2 + x)
    bob.left(month * favoriteMovie2 + x) 
    bob.forward(month * favoriteSong2 + x)
    bob.right(month * Pet2 + x)
    bob.forward(month * skill2 + x)
    bob.left(month * hobby2 + x)
    bob.forward(month * favoriteColor2 + x)
    bob.left(month * favoriteMovie2 + x)
    bob.forward(month * favoriteSong2 + x)
    bob.right(month * Pet2 + x)
    bob.forward(month * skill2 + x)
    bob.left(month * hobby2 + x)
    bob.forward(month * favoriteColor2 + x)
    bob.left(month * favoriteMovie2 + x)
    bob.forward(month * favoriteSong2 + x)
    bob.right(month * Pet2 + x)
    bob.forward(month * skill2 + x)
    bob.left(month * hobby2 + x)
    bob.forward(month * favoriteColor2 + x)
    bob.left(month * favoriteMovie2 + x)
    bob.forward(month * favoriteSong2 + x)
    x = x + month + day
turtle.done()









