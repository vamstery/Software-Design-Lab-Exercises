class Node(object):
    # Singly linked node
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, value):
        # Append an item
        new_item = Node(value, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1

    def iter(self):
        # Iterate the list
        current = self.head
        while current:
            item_val = current.value
            current = current.next
            yield item_val

    def print_foward(self):
        for node in self.iter():
            print(node)

    def search_item(self, val):
        for node in self.iter():
            if val == node:
                return True
        return False

    def delete(self, value):
        # Delete a specific item
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
            print("Doubly Linked List is empty can't delete!")


        elif current.value == value:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.value == value:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next


        if node_deleted:
            self.count -= 1



print("WWW Online Shop")
items = doubly_linked_list()
items.append_item('WWW #231')
items.append_item('WWW #111')
items.append_item('WWW #234')
items.append_item('WWW #112')
items.append_item('WWW #109')
items.append_item('WWW #101')

print("Items Code:")
items.print_foward()
print("\n")

while True:

    print("\nPress/Type (x) if you want to exit.")
    user = input("What item is out of stock? ")

    if user == 'x':
            print('You exit the system')
            exit()

    items.delete(user)
    print("\nResult:")
    items.print_foward()


#items.delete("ITEM")