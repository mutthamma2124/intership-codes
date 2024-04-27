list=[1,2,5,8,9,11,12]
l=0
r=len(list)-1
key=6
while l<=r:
   mid=(l+r)//2
   if list[mid]==key:
       print(f"key find at the index of{mid}")
       break
   elif list[mid]>key:
       r=mid-1
   else:
       l=mid+1
if key not in list:
    print("value not found")


