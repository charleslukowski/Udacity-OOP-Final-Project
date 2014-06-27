import turtle

def draw_square():
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('green')
	brad.speed(1)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)

def draw_circle():
	angie = turtle.Turtle()
	angie.shape('arrow')
	angie.color('blue')
	angie.circle(100)

def draw_triangle():
	tom = turtle.Turtle()
	tom.forward(50)
	tom.left(120)
	tom.forward(50)
	tom.left(120)
	tom.forward(50)
	tom.color('yellow')

def main():
	window = turtle.Screen()
	window.bgcolor('red')
	draw_square()
	draw_circle()
	draw_triangle()
	window.exitonclick()

if __name__ == '__main__':
	main()