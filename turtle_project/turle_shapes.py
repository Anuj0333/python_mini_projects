from turtle import Turtle,Screen
import turtle as t
import random
import turtle 
tim=t.Turtle()
color=["chocolate1","brown2","azure2"]
s=Screen()
def draw_shapes(num_sides):
        
    for i in range(num_sides):
            
        angle =360/ num_sides
        tim.forward(100)
        tim.right(angle)
for shape_side_n in range(3,11):
     tim.color(random.choise(color))
     draw_shapes(shape_side_n)


s.exitonclick()
