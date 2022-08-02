# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
l1=[2,3,4]
l2=[[num+index] for index in range(0,3) for num in l1]
print(l2)