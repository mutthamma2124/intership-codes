l=[8,7,3,5,1,0]
n=len(l)
for i in range (1,len(l)) :    
    key=l[i]
    j=i-1
    while j>=0 and l[j]>key:
         l[j+1]=l[j]
         j=j-1
         l[j+1]=key
print(l)