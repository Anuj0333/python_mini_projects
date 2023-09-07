from turtle import Turtle,Screen
from paddle import Paddle

s=Screen()
s.setup(width=800,height=600)
s.bgcolor("black")
s.title("Pong Game")
s.tracer(0)


r_paddle=Paddle((380,0))
l_paddle=Paddle((-390,0))


s.listen()
s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down")    
s.onkey(l_paddle.go_up,"W")
s.onkey(l_paddle.go_down,"S")

game_is_on=True
while game_is_on:
    s.update( )





















s.exitonclick()
