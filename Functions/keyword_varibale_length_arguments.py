
def person(name,*data):
    print(name)
    print(data)

person('prasanna',28,'bengaluru',88907804807)

#Variable length of keywords with help of keyword
def person1(name,**data):
    print(name)
    print(data)

person1('prasanna',age=28,city='bengaluru',phone=88907804807)

# print in key value pair
print("Print in key value pair ................")
def person2(name,**data):
    print(name)

    for i,j in data.items():
        print(i,j)

person2('prasanna',age=28,city='bengaluru',phone=88907804807)