# numbers = [1,2,3,4]
# #using map() to square each number
# squared = map(lambda x: x**2,numbers)
# #convert the iterator to a list to see the results
# print(list(squared))

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
my_screen = Screen()
print(my_screen.canvheight)

timmy.shape("turtle")
timmy.color("red","green")
timmy.circle(150)
my_screen.exitonclick()
print ("code executed successfully")