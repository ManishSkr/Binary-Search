"""Peak element is the element which is greater than its two neighbours, this is also a variation of binary
search, so if the element is peak element then we have to return its index."""

def peakElement(arr):
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=(l+r)//2
        if(mid>0 and mid<len(arr)-1):
            if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                # return peak element
                return mid
            elif(arr[mid-1]>arr[mid]):
                r=mid-1
            elif(arr[mid+1]>arr[mid]):
                l=mid+1
        elif(mid==0):
            if(arr[0]>arr[1]):
                return 0
            else:
                return 1
        elif(mid==len(arr)-1):
            if(arr[len(arr)-1]>arr[len(arr)-2]):
                return len(arr)-1
            else:
                return len(arr)-2

arr=[5,10,20,15]
print(peakElement(arr))