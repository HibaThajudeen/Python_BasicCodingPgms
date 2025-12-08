l = [2, 0, 4, 3, 7, 0, 5, 6, 0, 7]
x=[]
y=[]
for i in range(0, len(l)):
    if l[i] == 0:
        x.append(l[i])
    else:
        y.append(l[i])
print(y+x)
                                    #y.extend(x)
                                    #print(y)

l = [2, 0, 4, 3, 7, 0, 5, 6, 0, 7]
x=[]
y=[]
count=0
for i in range(0, len(l)):
    if l[i] != 0:
        x.append(l[i])
    else:
        count=count+1
for i in range(0, count):
    x.append(0)
print(x)