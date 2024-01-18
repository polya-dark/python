class Box:
	def __init__(self, length, width, height):
		self.length = length;
		self.width = width;
		self.height = height;

	def volume(self):
		return self.length * self.width * self.height
	
	def area(self): 
		return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
	
box1 = Box(5, 3, 4)
print(box1.volume())
