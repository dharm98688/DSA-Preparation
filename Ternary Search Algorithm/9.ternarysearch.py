def ternarysearch(arr,i,j,key):
    mid1=i+(j-i)//3
    mid2=j-(j-i)//3
    while i<=j:
        if arr[mid1]==key:
            return mid1
        elif arr[mid2]==key:
            return mid2
        elif key<arr[mid1]: # first part of ternary search
            return ternarysearch(arr, i,mid1-1,key)
        elif key>arr[mid2]:# this is the 3rd part of ternary search
            return ternarysearch(arr, mid2+1,j,key)
        else:# 2nd part of ternary search
            return ternarysearch(arr,mid1+1,mid2-1,key)
    return -1


#Driver code
arr = [20,25,47,56,63,65,79,82]
#key=79
key= int(input("Enter the value :"))
i=0
j=len(arr)-1
result=ternarysearch(arr,i,j,key)
print("Here is the value of ternary search:",result)
