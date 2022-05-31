class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.last = None

	# This function is only for empty list
	def addToEmpty(self, data):

		if (self.last != None):
			return self.last

		# Creating the newnode temp
		temp = Node(data)
		self.last = temp

		# Creating the link
		self.last.next = self.last
		return self.last

	def addBegin(self, data):

		if (self.last == None):
			return self.addToEmpty(data)

		temp = Node(data)
		temp.next = self.last.next
		self.last.next = temp

		return self.last

	def addEnd(self, data):

		if (self.last == None):
			return self.addToEmpty(data)

		temp = Node(data)
		temp.next = self.last.next
		self.last.next = temp
		self.last = temp

		return self.last

	def addAfter(self, data, item):

		if (self.last == None):
			return None

		temp = Node(data)
		p = self.last.next
		while p:
			if (p.data == item):
				temp.next = p.next
				p.next = temp

				if (p == self.last):
					self.last = temp
					return self.last
				else:
					return self.last
			p = p.next
			if (p == self.last.next):
				print(item, "not present in the list")
				break

	def traverse(self):
		if (self.last == None):
			print("List is empty")
			return

		temp = self.last.next
		while temp:
			print(temp.data, end = " ")
			temp = temp.next
			if temp == self.last.next:
				break

# Driver Code
if __name__ == '__main__':

	llist = CircularLinkedList()

	last = llist.addToEmpty("Frappe (110) ||")
	last = llist.addBegin("Americano (150) ||")
	last = llist.addBegin("Cappucino (180) ||")
	last = llist.addEnd("Espresso (150) ||")
	last = llist.addEnd("Ice Coffee (100)")
	last = llist.addAfter("Machiatto (210) ||","Espresso (150) ||")

print("WELCOME TO WWW.COFFEESHOP")
print("Menu: ")

llist.traverse()

# This code is contributed by
# Aditya Singh
#Based on: https://www.geeksforgeeks.org/circular-singly-linked-list-insertion/