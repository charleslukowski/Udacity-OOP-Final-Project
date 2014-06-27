class Parent():
	def __init__(self, last_name, eye_color):
		self.last_name = last_name
		self.eye_color = eye_color
		print 'Parent Constructor Called'

class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys
		print 'Child Constructor Called'

p = Parent('Jones', 'green')
c = Child('Jones', 'green', 5)
print c.last_name
print c.number_of_toys