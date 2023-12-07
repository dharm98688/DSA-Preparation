def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                #swap
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr        
#driver code
arr=[70,20,30,78,90,45,67]
result=bubblesort(arr)
print("Here is the sorted arrar:", result)
