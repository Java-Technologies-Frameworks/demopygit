try:
    # ZeroDivisionError
    result = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError occurred:", e)

try:
    # ValueError
    num = int("abc")
except ValueError as e:
    print("ValueError occurred:", e)

try:
    # TypeError
    result = 10 + "5"
except TypeError as e:
    print("TypeError occurred:", e)

try:
    # NameError
    print(x)
except NameError as e:
    print("NameError occurred:", e)

try:
    # FileNotFoundError
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print("FileNotFoundError occurred:", e)

try:
    # IndexError
    my_list = [1, 2, 3]
    print(my_list[3])
except IndexError as e:
    print("IndexError occurred:", e)

try:
    # KeyError
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError as e:
    print("KeyError occurred:", e)

try:
    # AttributeError
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list.append)
except AttributeError as e:
    print("AttributeError occurred:", e)

try:
    # IOError (Python 2) / FileNotFoundError (Python 3)
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except IOError as e:
    print("IOError occurred:", e)

try:
    # SyntaxError
    eval("print('Hello world'")
except SyntaxError as e:
    print("SyntaxError occurred:", e)
