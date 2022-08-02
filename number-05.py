# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

a=[1,2,3]
b=[0,1,2]
l1=[(index,item) for item in [1,2,3] for index in range(1,4)]
print(l1)

# for item in a:
    # for i in range(1,4):
        # l1.append((i,item))
