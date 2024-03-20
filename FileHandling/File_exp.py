

f=open('MyData','r')
#print(f.read())
print(f.readline(4),end="#")
print(f.readline())
print(f.readline())

f1=open('abc','w')
f1.write("Prasanna")
f1.write("Running machine")