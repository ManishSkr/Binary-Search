"""Here given a softed array of alphabets and a key alphabet and we need to find the next of the alphabet
which is present in the array"""

def NextAlphabet(arr,key):
    l=0
    r=len(arr)-1
    val=""
    while(l<=r):
        mid=l+r
        mid>>1
        if(arr[mid]==key):
            l=mid+1
        elif(arr[mid]<key):
            r=mid-1
        elif(arr[mid]>key):
            val+=arr[mid]
            l=mid+1
    return val
arr='acfh'
key='f'
print(NextAlphabet(arr,key))