def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i-1
        key=arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
#Driver code
arr =[80,70,83,58,98]
result = insertion_sort(arr)
print("Sorted array is here :", result)

# time complexity:O(n2)
