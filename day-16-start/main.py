#
# import turtle
# import another_function
# print(another_function.another_variable)
#
#
# mani = turtle.Turtle()
# # print(mani)
#
# from turtle import Turtle,Screen
# gimmy = Turtle()
# print(gimmy)
# gimmy.shape('turtle')
# gimmy.color('blue1')
# gimmy.forward(100)
#
# my_screen = Screen()
# # print(my_screen)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import  PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name" , ['Pikachu', 'Squirtle','Charmander'])
table.add_column("Type",['Electric', 'Water', 'Fire'])
table.align='l'

print(table)

