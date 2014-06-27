choices = [1, 2, 3, 4, 5]
print choices.index(3)

for index, value in enumerate(choices):
	print 'index:' + str(index)
	print 'value:' + str(value)
	print '*' * 20

for i in range(len(choices)):
	print i