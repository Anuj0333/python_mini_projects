from turtle import Turtle,Screen
from snake import Snake 
import time

s=Screen()
s.setup(width=750,height=750)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)

snake=Snake()

s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")
    
game_is_on=True
while game_is_on:
    s.update()
    time.sleep(.1)
    snake.move()





s.exitonclick()