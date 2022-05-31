class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singly_linked_list:
    def __init__(self):
        # Create an empty list
        self.tail = None
        self.head = None
        self.count = 0

    def append_item(self, data):
        # Append items on the list
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

    def __getitem__(self, index):
        if index > self.count - 1:
            return "Sorry your order is unavailable."
        current_val = self.tail
        for n in range(index):
            current_val = current_val.next
        return current_val.data



items = singly_linked_list()
items.append_item('Cappucino')
items.append_item('Coffee')
items.append_item('Frappe')
items.append_item('Hot Choco')
items.append_item('Milk')
items.append_item('Americano')


print("\t***WELCOME TO WWW.COFFEESHOP***\n")

print("Menu: "
      "\n (D1) Milktea || (D2) Coffee || (D3) Ice Tea || (D4) Hot Choco || (D5) Milk || (D6) Water")
print("\n\nWaiter:")
order = input("What is your drink Ma'am/Sir? ")

if order == "D1":
    print("Noted! your order is: ", items[0] )
elif order == "D2":
    print("Noted! your order is: ",items[1])
elif order == "D3":
    print("Noted! your order is: ",items[2])
elif order == "D4":
    print("Noted! your order is: ",items[3])
elif order == "D5":
    print("Noted! your order is: ",items[4])
elif order == "D6":
    print("Noted! your order is: ",items[5])

else:
    print(items[10])

'''
print("Search using index:")
print(items[0])
print(items[1])
print(items[4])
print(items[5])
print(items[10])
'''
#BASED ON: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-4.php
