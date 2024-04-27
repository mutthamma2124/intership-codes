a=0
b=8
print(a)
print(b)
for i in range(0,8):
    print(a+b)
    temp=a
    a=b
    b=temp+a
