# OOP
'''from unicodedata import name

class User:
    def __init__(self,name,password):
        self.name=name
        self.password=password
    def change_password(self,password):
        self.password=password

class BankUser(User):
    def __init__(self,name,password):
        super().__init__
        self.balance=0
    def checkBalance(self):
        print(f'Balance: {self.balance}')

bank_user1=BankUser("pat","password")
bank_user1.checkBalance()'''


# CC: Linked List Prepend Method
'''class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print(f"Head Node created: {new_node.value}")
        else:
            new_node.next = self.head
            self.head = new_node
            print(f"Prepended new Head Node with value: {new_node.value}")
        print(f"Node following Head is: ",end="")
        print(self.head.next.value if self.head.next else "None")

    def print(self):
        ptr = self.head
        while ptr is not None:
            print(f"{ptr.value}", end="")
            if ptr.next is not None:
                print("-> ", end="")
            ptr = ptr.next


list = LinkedList()
list.prepend(0)
list.print()'''

# CC: Ice Cream Shop Order Queue

class Queue:
    def __init__(self) -> None:
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def get_queue(self):
        return self.items

class IceCreamShop:
    def __init__(self, flavors) -> None:
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
            return
        if scoops not in (1, 2, 3):
            print("Choose between 1-3 scoops\n")
            return
        print("Order Created")
        order = {
            "customer": customer,
            "flavor": flavor,
            "scoops": scoops
        }
        self.orders.enqueue(order)

    def show_all_orders(self):
        list_of_orders = self.orders.get_queue()
        if len(list_of_orders) == 0:
            print("No Orders")
        else:
            print("All Pending Ice Cream Orders:")
            for order in self.orders.get_queue():
                print(f"Customer: {order['customer']} -- Flavor: {order['flavor']} -- Scoops: {order['scoops']}")
            print("\n")

    def next_order(self):
        next_order=self.orders.dequeue()
        if next_order is None:
            print("No Orders")
            return
        else:
            print("Next Order Up!")
            print(f"Customer: {next_order['customer']} -- Flavor: {next_order['flavor']} -- Scoops: {next_order['scoops']}\n")

            self.show_all_orders()

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()