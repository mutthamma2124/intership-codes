'''l=[1 ,2, 3, 4, 5]
n=len(l)
mid=n//2
left=l[:mid]
right=l[mid:]
print(left)
print(right)'''


lis=list(map(int,input("enter the list value").split(" ")))
def merge(lis):
    if len(lis)>1:
        mid=len(lis)//2
        left=lis[:mid]
        right=lis[mid:]
        merge(left)
        merge(right)
        L=0
        R=0
        K=0
        while L<len(left) and R<len(right):
            if left[L]>right[R]:
                lis[K]=right[R]
                R=R+1
            else:
                lis[K]=left[L]
                L=L+1
                K=K+1
        while L<len(left):
            lis[K]=left[L]
            L=L+1
            R=R+1
        while R<len(right):
            lis[K]=right[R]
            R=R+1
            K=K+1
merge(lis)
print(lis)
#sorted_lis=merge(lis)
#print(sorted_lis)

                