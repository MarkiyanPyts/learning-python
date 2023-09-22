# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, TurtleScreen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')


screen = TurtleScreen()
screen.exitonclick()