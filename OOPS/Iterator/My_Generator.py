# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
#
# # Create a generator object
# gen = my_generator()
#
# # Iterate over the generator object to yield values
# for value in gen:
#     print(value)


def top_ten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = top_ten()
for i in values:
    print(i)

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator function
gen = count_up_to(5)
for value in gen:
    print(value)



