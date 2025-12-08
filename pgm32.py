x= [1,2,3,2,4,3]
n=len(x)
for i in set(x):
    if x.count(i)>1:
        print(i,end=" ")

#OR

x=[1,2,3,2,4,3]
y=set()
z=set()
for i in x:
    if i in y:
        z.add(i)
    else:
        y.add(i)
print(list(z))

