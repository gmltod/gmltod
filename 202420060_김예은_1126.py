#구구단...
def print_dan(mul):
    for i in range(1, 10):
        print(mul, 'x', i, '=', mul*i)
         
mul = int(input("숫자를 입력하세요. "))
print_dan(mul)


#내가 그릴 수 있는 가장 멋있는 도형... 오륜기...
import turtle
import time
turtle.pensize(4)

turtle.pencolor("blue")
turtle.penup()
turtle.goto(-120, 0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("black")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("red")
turtle.penup()
turtle.goto(120, 0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("yellow")
turtle.penup()
turtle.goto(-60, -50)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("green")
turtle.penup()
turtle.goto(60, -50)
turtle.pendown()
turtle.circle(50)

time.sleep(2)