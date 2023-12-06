# finding the index of the number through linear search
def linearsearch(arr,x):
     for i in range(len(arr)):
         if arr[i]==x:
             return i
     return -1

#Driver code
arr=[20,45,27,47,55,67,75,88,90] # given array
x=65 # target value
#Function calling
result = linearsearch(arr,x)
print("Index of the number is :", result)

# Time complexity = O(n) bcz only one loop
# Space complexity =O(1) we are not using extra space
