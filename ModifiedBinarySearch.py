"""Here we need to search an element with a nearly sorted array, ie the element may present in the ith postion
or i-1 position or i+1 position"""

def ModifiedBS(arr,ele):
    l=0
    r=len(arr)
    while(l<=r):
        mid=l+(r-l)//2
        if(arr[mid]==ele):
            return mid
        #we check the boundary condition for last left element
        elif(arr[mid-1]==ele and mid-1>l ):
            return mid-1
        #we check the boundary condition for last right element
        elif(arr[mid+1]==ele and mid+1<r):
            return mid+1
        elif(ele<arr[mid]):
            r=mid-2
        elif(ele>arr[mid]):
            l=mid+2

arr=[5,10,30,20,40]
ele=20
print(ModifiedBS(arr,ele))