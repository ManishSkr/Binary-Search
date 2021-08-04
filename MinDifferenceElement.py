"""Minimum difference element, this question is also one of the variation of binary search
Here we've given an array and a key and we need to find the element that has a minimum difference with key."""

def MinDiff(arr,key):
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=(l+r)//2
        if arr[mid]==key:
            return arr[mid]
        elif(arr[mid]<key):
            l=mid+1
        elif(arr[mid]>key):
            r=mid-1
    
    a=abs(arr[l]-key)
    b=abs(arr[r]-key)
    if(a<b):
        return arr[l]
    else:
        return arr[r]

    

arr=[1,3,8,10,15]
key=12
print(MinDiff(arr,key))