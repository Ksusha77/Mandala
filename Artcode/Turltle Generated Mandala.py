import turtle
age = int(input("What is your age? A close number is acceptable: "))
favoriteColor = input("What is your favorite color")
favoriteMovie = input("What is your favorite Movie, Book, or Video game")
favoriteSong = input("What is your favorite Song?")
Pet = input("What is your pet's name (You can make a name up if needed)")
skill = input("If you could instantly master any skill, what would it be?")
hobby = input("What is your favorite Hobby?")
favoriteColor2 = len(favoriteColor)
favoriteMovie2 = len(favoriteMovie)
favoriteSong2 = len(favoriteSong)
Pet2 = len(Pet)
skill2 = len(skill)
hobby2 = len(hobby)


wn = turtle.Screen()
bob = turtle.Turtle()
turtle.speed(0)

for _ in range(age):
    import random;
    x = age
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
    x = x + 30
turtle.done()









