def two_sum(arr, target_sum):
    left = 0
    right = len(arr)-1
    while left < right:
        if (arr[left]+arr[right]==target_sum):
            return left,right
        elif (arr[left]+arr[right]<target_sum):
            left+=1
        else:
            right-=1
    return -1,-1
#driver code
arr=[2,7,11,15]
target_sum = 9
result = two_sum(arr, target_sum)
print("Here is sum of two :",result)
