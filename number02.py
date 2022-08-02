# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] 
l1=['x','y','z']
l2=[index*item for index in range(1,5) for item in l1]
print(l2)
