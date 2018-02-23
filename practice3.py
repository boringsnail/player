class stack():
	def __init__(self):
		self.items = []
		self.empty = (self.items == [])
	def peek(self):
		return self.items[len(self.items) -1]
	def push(self,x):
		self.items.append(x)
	def pop(self):
		if self.empty:
			print ("underflow")
		else :
			return self.items.pop()
S = stack()
S.push(1)
S.push(2)
print (S.peek())
S.pop()
S.pop()
class queue():
	def __init__(self):
		self.items = []
		self.length = len(self.items)
		self.head = 0
		self.tail = 0
	def enqueue(self,x):
		self.items.append(x)
		self.tail += 1
		if self.tail == self.length:
			self.tail = 0
		else:
			self.tail += 1
	def dequeue(self):
		x = self.items[self.head]
		if self.head == self.tail:
			self.heaf = 0
		else:
			self.head += 1
		return x
	def see(self):
		print (self.items[self.head])
Q = queue()
Q.enqueue(3)
Q.enqueue(5)
Q.enqueue(10)
Q.dequeue()
Q.dequeue()

Q.see()
