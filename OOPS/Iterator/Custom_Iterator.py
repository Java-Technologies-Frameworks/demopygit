class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Example usage
my_list = [1, 2, 3, 4, 5]
reverse_iterator = ReverseIterator(my_list)

for item in reverse_iterator:
    print(item)
