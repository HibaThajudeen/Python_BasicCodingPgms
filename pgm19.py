for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

                                            # * * * * *
                                            # * * * * *
                                            # * * * * *
                                            # * * * * *
                                            # * * * * *

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

                                            # *
                                            # * *
                                            # * * *
                                            # * * * *
                                            # * * * * *

for i in range(1,6):
    for j in range(6-i):
        print("*",end=" ")
    print()

                                            # * * * * *
                                            # * * * *
                                            # * * *
                                            # * *
                                            # *

for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

                                            # 1
                                            # 2 2
                                            # 3 3 3
                                            # 4 4 4 4
                                            # 5 5 5 5 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

                                            # 1
                                            # 1 2
                                            # 1 2 3
                                            # 1 2 3 4
                                            # 1 2 3 4 5

for i in range(1,6):
    for j in range(6-i):
        print(i,end=" ")
    print()

                                            # 1 1 1 1 1
                                            # 2 2 2 2
                                            # 3 3 3
                                            # 4 4
                                            # 5


for i in range(1,6):
    for j in range(6-i):
        print(5,end=" ")
    print()

                                            # 5 5 5 5 5
                                            # 5 5 5 5
                                            # 5 5 5
                                            # 5 5
                                            # 5


for i in range(5):
    for j in range(i+1):
        print(((2*i)+1),end=" ")
    print()

                                            # 1
                                            # 3 3
                                            # 5 5 5
                                            # 7 7 7 7
                                            # 9 9 9 9 9

