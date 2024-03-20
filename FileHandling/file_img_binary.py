
f =open('Pic.jpg','rb')
file1=open('MyPic.jpeg','wb')

for i in f:
    file1.write(i)

for i in f:
    print(i)