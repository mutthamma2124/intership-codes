l=list(map(int,input("enter the list value").split(" ")))
key=int(input("enter the key value:"))
for i in range(len(l)):
    if l[i]==key:
        print(f"the value found at{i}th index")
        break
    #if key not in l:
        #print("value not found")
       # print(i)
if i==len(l)-1:
    print('not found')

