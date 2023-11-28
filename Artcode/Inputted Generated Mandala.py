import turtle
import random






print("It is said the Mandala is a symbol of the self, the lines and shapes are universal among mankind")
print("Tell me about yourself. type A then enter to skip")
age = int(input("What is your age? A close number is acceptable: "))
dreamJob = input("What was your dream job as a kid?")
favoriteCharacter = input("What is your favorite fictional or real character")
favoriteMovie = input("What is your favorite Movie, Book, or Video game")
favoriteSong = input("What is your favorite Song?")
Pet = input("What is your pet's name (You can make a name up if needed)")
skill = input("If you could instantly master any skill, what would it be?")
hobby = input("What is your favorite Hobby?")
month = int(input("Number of the month you were born, Cannot be skipped"))
day = int(input("Number of the day of the month you were born Cannot be Skipped"))
#Converts the strings into numbers using the len() function
favoriteMovie2 = len(favoriteMovie)
favoriteSong2 = len(favoriteSong)
favoriteCharacter2 = len(favoriteCharacter)
dreamJob2 = len(dreamJob)
Pet2 = len(Pet)
skill2 = len(skill)
hobby2 = len(hobby)
x = 0

wn = turtle.Screen()
bob = turtle.Turtle()
turtle.speed(0)


wn = turtle.Screen()
bob = turtle.Turtle()
turtle.speed(0)
#Takes a users color 
colors_dict = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "purple" : (75, 0, 130),
    "cyan" : (0, 206, 209),
    "light_green" : (50, 205, 50),  
    "orange" : (255, 140, 0),
    # Add more colors as needed
}


def set_turtle_color(input_color):
    # Check if the input color is in the dictionary
    color_names = ["red", "green", "blue", "yellow", "purple", "cyan", "orange", "lightgreen"]  # Adjusted color names
    if input_color.lower() in color_names:
        turtle.color(input_color.lower())
    else:
        print("Color not found in dictionary.")


print("Out of these colors what is your favorite: Color Options: red, light_green, blue, yellow, cyan, orange, green, purple,")
user_input = input("Enter a color: ")
set_turtle_color(user_input)

# ... (the rest of your code)

#Draws turtles based on the various inputs. 



for _ in range(age):
    bob.right(month * Pet2 + x)
    bob.forward(month * skill2 + x)
    bob.left(month * hobby2 + x)
    bob.forward(month * dreamJob2 + x)
    bob.left(month * favoriteMovie2 + x) 
    bob.forward(month * favoriteSong2 + x)
    bob.right(month * Pet2 + x)
    bob.forward(month * skill2 + x)
    bob.left(month * hobby2 + x)
    bob.forward(month * dreamJob2 + x)
    bob.left(month * favoriteMovie2 + x)
    bob.forward(month * favoriteSong2 + x)
    bob.right(month * Pet2 + x)
    bob.forward(month * skill2 + x)
    bob.left(month * hobby2 + x)
    bob.forward(month * dreamJob2 + x)
    bob.left(month * favoriteMovie2 + x)
    bob.forward(month * favoriteSong2 + x)
    bob.right(month * Pet2 + x)
    bob.forward(month * skill2 + x)
    bob.left(month * hobby2 + x)
    bob.forward(month * dreamJob2 + x)
    bob.left(month * favoriteMovie2 + x)
    bob.forward(month * favoriteSong2 + x)
    x = x + month + day
turtle.done()









