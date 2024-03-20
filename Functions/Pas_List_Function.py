
def count(list):
    even =0
    odd =0
    for i in list:
        if i%2 ==0:
            even+=1
        else:
            odd+=1
    return even,odd

list =[20,25,32,89,17,90,31,37,52,11,23,100]
even,odd =count(list)
print("Even : {} and odd : {}".format(even,odd))
print(even)
print(odd)