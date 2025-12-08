# st=input("Enter string: ")
# count=set()
# x=[]
# for i in set(st):
#     print(i, st.count(i))
#     count=st.count(i)
#     x.append(st.count(i))
# n=len(x)
# for j in range(n):
#     if x[j-1]>x[j]:
#         x[j-1],x[j]=x[j],x[j-1]
# print(x)

st= int(input("Enter string: "))
for i in set(st):
    print(sorted(f"{i}"*st.count(i), end="")
    