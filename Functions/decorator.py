def div(a,b):
    if a<b:
        a,b =b,a
    print(a/b)
div(2,4)

# it doesnot matter the sequence , if i am passing a value is less then swap and do
# if a < b:
#     a, b = b, a
#Imagine the division code which was written is not present with us its in some other file.I dont want to touch
#because its used by some other file for logic.
#use decorator without chnaging the logic ,add additional logic on top of existing logic


def smart_div(func):
    def inner(a,b):
        if(a<b):
            a,b =b,a
        return func(a,b)
    return inner
div=smart_div(div)
div(2,4)