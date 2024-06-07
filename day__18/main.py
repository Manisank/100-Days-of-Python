import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
  r=random.randint(0,200)
  g=random.randint(0,250)
  b=random.randint (0,255)
  random_color  = (r , g , b)
  return random_color


directions=[0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for i in range(200):
  tim.color(random_color())
  tim.forward(30)
  tim.setheading(random.choice(directions))