# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 

l1=['x','y','z']
l3=[i*i2 for i in l1 for i2 in range(1,5)]
print(l3)