# Create a class Counter that keeps track of how many objects have been created.
# Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)

# Objects create karte hain
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Show count
Counter.show_count()
