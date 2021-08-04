"""This problem is about binary search using python"""

def binarySearch(arr,data):
    if(len(arr)==0):
        return 0
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=l+r
        mid=mid>>1
        if(arr[mid]==data):
            return mid
        elif(arr[mid]<data):
            l=mid+1
        elif(arr[mid]>data):
            r=mid-1

arr=[1,2,3,4,5,6]
data=5
print(binarySearch(arr,data))