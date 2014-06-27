import turtle

class Square():
	def __init__(self, turtle, length, color):
		self.turtle = turtle
		self.length = length
	def draw(self):
		for i in range(4):
			self.turtle.forward(self.length)
			self.turtle.right(90)
	def turn(self, amount):
		self.turtle.right(amount)

def main():
	window = turtle.Screen()
	window.bgcolor('red')

	t = turtle.Turtle()
	t.speed(100)
	s = Square(t, 100, 'yellow')
	for i in range(250):
		s.draw()
		s.turn(33)

	window.exitonclick()

if __name__ == '__main__':
	main()