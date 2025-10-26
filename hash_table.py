class Contact:
   
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        # Simple hash: sum of character codes % table size
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

        if self.data[index] is None:
            self.data[index] = new_node
        else:
            current = self.data[index]
            while current:
                if current.key == key:
                    current.value.number = number  # Update existing
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node  # Add to end of chain

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i, node in enumerate(self.data):
            print(f"Index {i}:", end=" ")
            if node is None:
                print("Empty")
            else:
                current = node
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


# ---------- TESTING ----------
if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()
    print("\nAdding contacts...")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.insert("Rebecca", "999-444-9999")

    table.print_table()

    print("\nSearch result:", table.search("John"))
    print("Search result:", table.search("Chris"))


# ---------- DESIGN MEMO ----------
'''
For this assignment, I used a hash table because it lets us look up contacts quickly.
When we know someones name, the hash function can turn it into an index in the table
so we dont have to search through every contact like we would in a list.
This makes finding and updating contacts much faster.

To handle collisions, I used separate chaining. This means if two names hash to the
same spot, we store them in a small linked list at that index. Then, when searching,
we just move through the small chain to find the right contact.

A software engineer might pick a hash table when fast lookups are needed, like
searching usernames, phone numbers, or IDs. A list would be slower because it needs
to check each item, and a tree could be more complex to balance and manage.
Hash tables are great when we have unique keys and want constant-time search,
insert, and update operations.
'''
