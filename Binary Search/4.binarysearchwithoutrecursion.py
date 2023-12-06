# finding the index of the number through binary search-  Searching Algorithm without recursion
def binarysearch(arr,x,i,j):
    while i<=j:
        #lower bound while division
        mid=i+(j-1)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:# for the right side
            i=mid+1#search space -mid+1 to j and recursion- calling the same function again inside the method definition
        else: # for the right side
            j=mid-1 #search space -i to mid-1
    return -1

#Driver code
arr = [20,30,40,50,60,70,80,90]
x=80 # target value
i=0
j=len(arr)-1
result=binarysearch(arr,x,i,j)
print("Search element present on this index :",result)
