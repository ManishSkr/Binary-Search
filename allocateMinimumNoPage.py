""" This is the best variation of binary search algorithm so far, here we have given the number of book pages
 and students , we have to reduce the number of pages that each student read"""
def isValid(arr,key,mid):
    n=len(arr)
    if(n<key):
        return -1
    st=1
    sum=0
    for i in range(n):
        sum+=arr[i]
        if(sum>mid):
            st+=1
            sum=0
        if(st>key):
            return False
    
    return True

    
def allocateMinimumPage(arr,key):
    start=max(arr)
    print(start)
    end=sum(arr)
    res=-1
    while(start<=end):
        mid=(start+end)//2
        if(isValid(arr,key,mid)):
            res=mid
            end=mid-1
        else:
            start=mid+1
    return res
arr=[10,20,30,40]
key=2

print(allocateMinimumPage(arr,key))