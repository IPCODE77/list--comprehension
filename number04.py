# [[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]

l1=[2,3,4,5]
l2=[[num+index for num in l1] for index in range(0,4)]
print(l2)