def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
numbers=[22,64,34,25,1,88]
print("original list",numbers)
bubble_sort(numbers)
print("sorted list",numbers)

